"""
=============================================================================
  Standalone OpenCV (cv2) + NumPy Desktop Image Processing Studio (v2.0 PRO)
=============================================================================
Pure OpenCV (cv2) and NumPy ONLY. No external GUI frameworks.
"""

import cv2
import numpy as np
import os
import sys
import time

WINDOW_NAME = "OpenCV Interactive Studio v2.0 PRO [Pure cv2 + NumPy]"
HEADER_HEIGHT = 82
STATUS_HEIGHT = 38
CANVAS_WIDTH = 900
CANVAS_HEIGHT = 550

COLOR_CANVAS_BG = (22, 24, 28)
COLOR_HEADER_BG = (32, 35, 40)
COLOR_STATUS_BG = (24, 26, 30)
COLOR_BTN_INACTIVE = (55, 60, 68)
COLOR_BTN_ACTIVE = (46, 204, 113)
COLOR_BTN_HOVER = (85, 92, 102)
COLOR_BTN_TEXT = (255, 255, 255)
COLOR_TEXT_MUTED = (175, 180, 188)
COLOR_CROSSHAIR = (0, 220, 255)
COLOR_STATUS_ACCENT = (0, 215, 255)

ROW1_BUTTONS = [
    {"id": "bg_remove", "label": "Remove BG",  "w": 96},
    {"id": "edge",      "label": "Edge Mode",  "w": 92},
    {"id": "sketch",    "label": "Sketch",     "w": 80},
    {"id": "invert",    "label": "Invert",     "w": 75},
    {"id": "sepia",     "label": "Sepia",      "w": 75},
    {"id": "beauty",    "label": "Beauty Cam", "w": 98},
    {"id": "cartoon",   "label": "Cartoon",    "w": 85},
]

ROW2_BUTTONS = [
    {"id": "facemark",  "label": "Face Mark",  "w": 92},
    {"id": "flip",      "label": "Flip H",     "w": 75},
    {"id": "rotate",    "label": "Rotate 90",  "w": 88},
    {"id": "crop",      "label": "Crop ROI",   "w": 88},
    {"id": "reset",     "label": "Reset All",  "w": 85},
    {"id": "save",      "label": "Save (s)",   "w": 85},
]

class CVStudioApp:
    def __init__(self, initial_image_path=None):
        self.base_dir = os.path.dirname(os.path.abspath(__file__))
        self.output_dir = os.path.join(self.base_dir, "output_results")
        self.cascades_dir = os.path.join(self.base_dir, "resources", "cascades")
        os.makedirs(self.output_dir, exist_ok=True)

        self.face_cascade = self.load_cascade("haarcascade_frontalface_default.xml")
        self.eye_cascade = self.load_cascade("haarcascade_eye.xml")

        self.raw_image = self.load_image(initial_image_path)
        self.original_image = self.fit_to_display(self.raw_image)
        self.current_source = self.original_image.copy()

        self.canvas_w = CANVAS_WIDTH
        self.canvas_h = HEADER_HEIGHT + CANVAS_HEIGHT + STATUS_HEIGHT

        self.filter_states = {
            "bg_remove": False,
            "edge": False,
            "sketch": False,
            "invert": False,
            "sepia": False,
            "beauty": False,
            "cartoon": False,
            "facemark": False,
        }

        self.cached_bg_mask = None
        self.mask_source_signature = None

        self.tb_brightness = 50
        self.tb_contrast = 10
        self.tb_hue = 0
        self.tb_blur = 0
        self.tb_bg_hue = 100
        self.tb_zoom = 100
        self.tb_pan_x = 200
        self.tb_pan_y = 200

        self.hover_btn = None
        self.status_message = "Ready. Drag Mouse for Crosshair | Right-Drag or Arrows to Pan | [s] Save"
        self.status_timestamp = time.time()

        self.crosshair_x = self.canvas_w // 2
        self.crosshair_y = CANVAS_HEIGHT // 2
        self.crosshair_active = False

        self.right_dragging = False
        self.drag_start_x = 0
        self.drag_start_y = 0
        self.pan_start_x = 200
        self.pan_start_y = 200

        self.mouse_inside_image = False
        self.current_pixel_bgr = (0, 0, 0)
        self.setup_buttons()

    def load_cascade(self, xml_name):
        path = os.path.join(self.cascades_dir, xml_name)
        if os.path.exists(path):
            return cv2.CascadeClassifier(path)
        return None

    def load_image(self, path):
        if path and os.path.isfile(path):
            img = cv2.imread(path)
            if img is not None:
                print(f"[CV Studio] Successfully loaded: {path}")
                return img

        fallback_path = os.path.join(self.base_dir, "resources", "boy.jpg")
        if os.path.isfile(fallback_path):
            img = cv2.imread(fallback_path)
            if img is not None:
                print(f"[CV Studio] Loaded default: {fallback_path}")
                return img

        print("[CV Studio] Generating synthetic sample canvas...")
        h, w = 550, 750
        canvas = np.zeros((h, w, 3), dtype=np.uint8)
        for y in range(h):
            r = y / h
            canvas[y, :] = (int(70 + 90 * r), int(50 + 60 * r), int(40 + 40 * r))
        cv2.circle(canvas, (w // 2, h // 2), 140, (190, 210, 245), -1)
        cv2.circle(canvas, (w // 2 - 45, h // 2 - 35), 22, (40, 50, 70), -1)
        cv2.circle(canvas, (w // 2 + 45, h // 2 - 35), 22, (40, 50, 70), -1)
        cv2.ellipse(canvas, (w // 2, h // 2 + 50), (50, 25), 0, 0, 180, (40, 50, 220), 6)
        cv2.putText(canvas, "OpenCV Canvas Fallback", (w // 2 - 180, 60),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.85, (255, 255, 255), 2, cv2.LINE_AA)
        return canvas

    def fit_to_display(self, img):
        h, w = img.shape[:2]
        scale = min(CANVAS_WIDTH / w, CANVAS_HEIGHT / h, 1.0)
        if scale < 1.0:
            nw, nh = int(w * scale), int(h * scale)
            return cv2.resize(img, (nw, nh), interpolation=cv2.INTER_AREA)
        return img.copy()

    def setup_buttons(self):
        self.buttons = []
        curr_x = 12
        y1, h1, gap = 8, 30, 8
        for b in ROW1_BUTTONS:
            self.buttons.append({"id": b["id"], "label": b["label"], "x": curr_x, "y": y1, "w": b["w"], "h": h1})
            curr_x += b["w"] + gap

        curr_x = 12
        y2, h2 = 44, 30
        for b in ROW2_BUTTONS:
            self.buttons.append({"id": b["id"], "label": b["label"], "x": curr_x, "y": y2, "w": b["w"], "h": h2})
            curr_x += b["w"] + gap

    def get_or_compute_bg_mask(self):
        sig = (self.current_source.shape, id(self.current_source))
        if self.cached_bg_mask is not None and self.mask_source_signature == sig:
            return self.cached_bg_mask

        self.set_status("Computing GrabCut background segmentation... (1-2s)")
        h, w = self.current_source.shape[:2]
        sample = self.current_source.copy()

        scale = min(400.0 / max(h, w), 1.0)
        sh, sw = int(h * scale), int(w * scale)
        small = cv2.resize(sample, (sw, sh), interpolation=cv2.INTER_AREA)

        mx, my = int(sw * 0.06), int(sh * 0.06)
        rect = (mx, my, sw - 2 * mx, sh - 2 * my)
        mask = np.zeros((sh, sw), np.uint8)
        bgdModel = np.zeros((1, 65), np.float64)
        fgdModel = np.zeros((1, 65), np.float64)

        try:
            cv2.grabCut(small, mask, rect, bgdModel, fgdModel, 3, cv2.GC_INIT_WITH_RECT)
            fg = np.where((mask == cv2.GC_FGD) | (mask == cv2.GC_PR_FGD), 1.0, 0.0).astype(np.float32)
        except Exception:
            fg = np.zeros((sh, sw), dtype=np.float32)
            cv2.ellipse(fg, (sw // 2, sh // 2), (int(sw * 0.4), int(sh * 0.45)), 0, 0, 360, 1.0, -1)

        full_mask = cv2.resize(fg, (w, h), interpolation=cv2.INTER_LINEAR)
        full_mask = cv2.GaussianBlur(full_mask, (9, 9), 0)
        self.cached_bg_mask = np.clip(full_mask, 0.0, 1.0)
        self.mask_source_signature = sig
        self.set_status("Background segmented! Slide 'BG Color (Hue)' to recolor.")
        return self.cached_bg_mask

    def on_brightness(self, val): self.tb_brightness = val
    def on_contrast(self, val): self.tb_contrast = max(1, val)
    def on_hue(self, val): self.tb_hue = val
    def on_blur(self, val): self.tb_blur = val
    def on_bg_hue(self, val): self.tb_bg_hue = val
    def on_zoom(self, val): self.tb_zoom = max(20, val)
    def on_pan_x(self, val): self.tb_pan_x = val
    def on_pan_y(self, val): self.tb_pan_y = val

    def apply_filters(self):
        out = self.current_source.copy()

        # 1. Background Removal & Dynamic Color Scale
        if self.filter_states["bg_remove"]:
            mask_2d = self.get_or_compute_bg_mask()
            mask_3d = np.repeat(mask_2d[:, :, np.newaxis], 3, axis=2)

            h, w = out.shape[:2]
            hsv_bg = np.zeros((h, w, 3), dtype=np.uint8)
            hsv_bg[:, :] = (self.tb_bg_hue, 220, 230)
            bgr_bg = cv2.cvtColor(hsv_bg, cv2.COLOR_HSV2BGR).astype(np.float32)

            fg = out.astype(np.float32)
            comp = fg * mask_3d + bgr_bg * (1.0 - mask_3d)
            out = np.clip(comp, 0, 255).astype(np.uint8)

        # 2. Blur Intensity
        if self.tb_blur > 0:
            k = self.tb_blur * 2 + 1
            out = cv2.GaussianBlur(out, (k, k), 0)

        # 3. Brightness & Contrast
        alpha = self.tb_contrast / 10.0
        beta = self.tb_brightness - 50
        out = cv2.convertScaleAbs(out, alpha=alpha, beta=beta)

        # 4. Hue Shift (HSV)
        if self.tb_hue > 0:
            hsv = cv2.cvtColor(out, cv2.COLOR_BGR2HSV).astype(np.int32)
            hsv[:, :, 0] = (hsv[:, :, 0] + self.tb_hue) % 180
            out = cv2.cvtColor(hsv.astype(np.uint8), cv2.COLOR_HSV2BGR)

        # 5. Invert Mode
        if self.filter_states["invert"]:
            out = cv2.bitwise_not(out)

        # 6. Sepia Filter
        if self.filter_states["sepia"]:
            sepia_kernel = np.array([
                [0.272, 0.534, 0.131],
                [0.349, 0.686, 0.168],
                [0.393, 0.769, 0.189]
            ])
            out = cv2.transform(out, sepia_kernel)
            out = np.clip(out, 0, 255).astype(np.uint8)

        # 7. Beauty Cam
        if self.filter_states["beauty"]:
            smooth = cv2.bilateralFilter(out, d=15, sigmaColor=85, sigmaSpace=85)
            gray = cv2.cvtColor(out, cv2.COLOR_BGR2GRAY)
            edges = cv2.Canny(gray, 60, 140)
            edges_dilated = cv2.dilate(edges, np.ones((3, 3), np.uint8), iterations=1)
            edge_mask = np.repeat((edges_dilated[:, :, np.newaxis] > 0), 3, axis=2)
            beauty = cv2.addWeighted(out, 0.35, smooth, 0.65, 0)
            beauty[edge_mask] = out[edge_mask]
            out = beauty

        # 8. Cartoon
        if self.filter_states["cartoon"]:
            gray = cv2.cvtColor(out, cv2.COLOR_BGR2GRAY)
            gray_blur = cv2.medianBlur(gray, 7)
            edges = cv2.adaptiveThreshold(gray_blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 7)
            color = cv2.bilateralFilter(out, d=9, sigmaColor=250, sigmaSpace=250)
            edge_3d = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
            out = cv2.bitwise_and(color, edge_3d)

        # 9. Pencil Sketch
        if self.filter_states["sketch"]:
            gray = cv2.cvtColor(out, cv2.COLOR_BGR2GRAY)
            inv = 255 - gray
            blur_inv = cv2.GaussianBlur(inv, (21, 21), 0)
            sketch = cv2.divide(gray, 255 - blur_inv, scale=256)
            out = cv2.cvtColor(sketch, cv2.COLOR_GRAY2BGR)

        # 10. Multi-Color Face Landmarks
        if self.filter_states["facemark"] and self.face_cascade is not None:
            gray = cv2.cvtColor(out, cv2.COLOR_BGR2GRAY)
            faces = self.face_cascade.detectMultiScale(gray, 1.1, 5, minSize=(60, 60))
            for (fx, fy, fw, fh) in faces:
                cv2.rectangle(out, (fx, fy), (fx + fw, fy + fh), (255, 200, 0), 2)
                cv2.putText(out, "Face", (fx, fy - 6), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 200, 0), 2)
                if self.eye_cascade is not None:
                    roi_gray = gray[fy:fy + int(fh * 0.55), fx:fx + fw]
                    eyes = self.eye_cascade.detectMultiScale(roi_gray, 1.1, 4, minSize=(18, 18))
                    for (ex, ey, ew, eh) in eyes[:2]:
                        cv2.rectangle(out, (fx + ex, fy + ey), (fx + ex + ew, fy + ey + eh), (0, 255, 255), 2)
                nx, ny, nw, nh = int(fx + fw * 0.35), int(fy + fh * 0.45), int(fw * 0.30), int(fh * 0.25)
                cv2.rectangle(out, (nx, ny), (nx + nw, ny + nh), (0, 230, 70), 2)
                cv2.putText(out, "Nose", (nx, ny - 4), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 230, 70), 1)
                mx, my, mw, mh = int(fx + fw * 0.25), int(fy + fh * 0.72), int(fw * 0.50), int(fh * 0.18)
                cv2.rectangle(out, (mx, my), (mx + mw, my + mh), (0, 40, 240), 2)
                cv2.putText(out, "Lips", (mx, my - 4), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 40, 240), 1)

        # 11. Canny Edge Mode
        if self.filter_states["edge"]:
            gray = cv2.cvtColor(out, cv2.COLOR_BGR2GRAY)
            t_upper = int(50 + 200 * (self.crosshair_x / max(1, self.canvas_w)))
            t_lower = int(20 + 130 * (self.crosshair_y / max(1, CANVAS_HEIGHT)))
            edges = cv2.Canny(gray, max(10, min(t_lower, t_upper - 10)), max(30, t_upper))
            edge_bgr = np.zeros_like(out)
            edge_bgr[edges > 0] = (255, 220, 0)
            out = edge_bgr

        return out

    def apply_transform_and_place(self, processed_img):
        viewport = np.full((CANVAS_HEIGHT, self.canvas_w, 3), COLOR_CANVAS_BG, dtype=np.uint8)

        scale = self.tb_zoom / 100.0
        h, w = processed_img.shape[:2]
        new_w = max(20, int(w * scale))
        new_h = max(20, int(h * scale))

        interp = cv2.INTER_LINEAR if scale > 1.0 else cv2.INTER_AREA
        scaled_img = cv2.resize(processed_img, (new_w, new_h), interpolation=interp)

        shift_x = self.tb_pan_x - 200
        shift_y = self.tb_pan_y - 200

        center_x = self.canvas_w // 2 + shift_x
        center_y = CANVAS_HEIGHT // 2 + shift_y

        top_left_x = center_x - new_w // 2
        top_left_y = center_y - new_h // 2

        src_x1 = max(0, -top_left_x)
        src_y1 = max(0, -top_left_y)
        src_x2 = min(new_w, self.canvas_w - top_left_x)
        src_y2 = min(new_h, CANVAS_HEIGHT - top_left_y)

        dst_x1 = max(0, top_left_x)
        dst_y1 = max(0, top_left_y)
        dst_x2 = min(self.canvas_w, top_left_x + new_w)
        dst_y2 = min(CANVAS_HEIGHT, top_left_y + new_h)

        if (dst_x2 > dst_x1) and (dst_y2 > dst_y1) and (src_x2 > src_x1) and (src_y2 > src_y1):
            viewport[dst_y1:dst_y2, dst_x1:dst_x2] = scaled_img[src_y1:src_y2, src_x1:src_x2]

        return viewport

    def render_canvas(self, processed_img):
        canvas = np.zeros((self.canvas_h, self.canvas_w, 3), dtype=np.uint8)

        # 1. Header Toolbar
        canvas[0:HEADER_HEIGHT, :] = COLOR_HEADER_BG
        cv2.line(canvas, (0, HEADER_HEIGHT - 1), (self.canvas_w, HEADER_HEIGHT - 1), (60, 65, 75), 1)

        for b in self.buttons:
            bid = b["id"]
            is_active = self.filter_states.get(bid, False)
            is_hover = (self.hover_btn == bid)

            if is_active:
                btn_color = COLOR_BTN_ACTIVE
                text_color = (15, 30, 20)
            elif is_hover:
                btn_color = COLOR_BTN_HOVER
                text_color = COLOR_BTN_TEXT
            else:
                btn_color = COLOR_BTN_INACTIVE
                text_color = COLOR_BTN_TEXT

            cv2.rectangle(canvas, (b["x"], b["y"]), (b["x"] + b["w"], b["y"] + b["h"]), btn_color, -1)
            cv2.rectangle(canvas, (b["x"], b["y"]), (b["x"] + b["w"], b["y"] + b["h"]), (85, 92, 102), 1)

            (tw, th), _ = cv2.getTextSize(b["label"], cv2.FONT_HERSHEY_SIMPLEX, 0.40, 1)
            tx = b["x"] + (b["w"] - tw) // 2
            ty = b["y"] + (b["h"] + th) // 2 - 1
            cv2.putText(canvas, b["label"], (tx, ty), cv2.FONT_HERSHEY_SIMPLEX, 0.40, text_color, 1, cv2.LINE_AA)

        # 2. Viewport
        viewport = self.apply_transform_and_place(processed_img)

        if self.crosshair_active or self.mouse_inside_image:
            cx, cy = self.crosshair_x, self.crosshair_y
            if 0 <= cx < self.canvas_w and 0 <= cy < CANVAS_HEIGHT:
                cv2.line(viewport, (cx, 0), (cx, CANVAS_HEIGHT), COLOR_CROSSHAIR, 1, cv2.LINE_AA)
                cv2.line(viewport, (0, cy), (self.canvas_w, cy), COLOR_CROSSHAIR, 1, cv2.LINE_AA)
                cv2.circle(viewport, (cx, cy), 5, (0, 0, 255), 1, cv2.LINE_AA)

        canvas[HEADER_HEIGHT:HEADER_HEIGHT + CANVAS_HEIGHT, :] = viewport

        # 3. Status Bar
        status_y = HEADER_HEIGHT + CANVAS_HEIGHT
        canvas[status_y:self.canvas_h, :] = COLOR_STATUS_BG
        cv2.line(canvas, (0, status_y), (self.canvas_w, status_y), (50, 55, 62), 1)

        pan_x_rel = self.tb_pan_x - 200
        pan_y_rel = self.tb_pan_y - 200
        info_left = f"X:{self.crosshair_x:3d} Y:{self.crosshair_y:3d} | Zoom:{self.tb_zoom}% | Pan:({pan_x_rel:+d},{pan_y_rel:+d}) | BG-Hue:{self.tb_bg_hue}"
        cv2.putText(canvas, info_left, (12, status_y + 24), cv2.FONT_HERSHEY_SIMPLEX, 0.40, COLOR_STATUS_ACCENT, 1, cv2.LINE_AA)

        (mw, _), _ = cv2.getTextSize(self.status_message, cv2.FONT_HERSHEY_SIMPLEX, 0.38, 1)
        mx = max(self.canvas_w - mw - 15, 500)
        cv2.putText(canvas, self.status_message, (mx, status_y + 24), cv2.FONT_HERSHEY_SIMPLEX, 0.38, COLOR_TEXT_MUTED, 1, cv2.LINE_AA)

        return canvas

    def handle_mouse(self, event, x, y, flags, param):
        self.hover_btn = None
        if y < HEADER_HEIGHT:
            for b in self.buttons:
                if b["x"] <= x <= b["x"] + b["w"] and b["y"] <= y <= b["y"] + b["h"]:
                    self.hover_btn = b["id"]
                    break

        view_y = y - HEADER_HEIGHT
        if 0 <= view_y < CANVAS_HEIGHT:
            self.mouse_inside_image = True
            if event == cv2.EVENT_LBUTTONDOWN or (flags & cv2.EVENT_FLAG_LBUTTON):
                self.crosshair_x = x
                self.crosshair_y = view_y
                self.crosshair_active = True

            # Right Click Drag: Real-Time Pan (Move image left/right/up/down)
            if event == cv2.EVENT_RBUTTONDOWN:
                self.right_dragging = True
                self.drag_start_x = x
                self.drag_start_y = view_y
                self.pan_start_x = self.tb_pan_x
                self.pan_start_y = self.tb_pan_y
                self.set_status("Moving image position with Right-Drag...")

            elif event == cv2.EVENT_MOUSEMOVE and self.right_dragging:
                dx = x - self.drag_start_x
                dy = view_y - self.drag_start_y
                self.tb_pan_x = int(np.clip(self.pan_start_x + dx, 0, 400))
                self.tb_pan_y = int(np.clip(self.pan_start_y + dy, 0, 400))
                cv2.setTrackbarPos("Move X (Pan)", WINDOW_NAME, self.tb_pan_x)
                cv2.setTrackbarPos("Move Y (Pan)", WINDOW_NAME, self.tb_pan_y)
        else:
            self.mouse_inside_image = False

        if event == cv2.EVENT_LBUTTONUP:
            self.crosshair_active = False
            if self.hover_btn:
                self.on_button_clicked(self.hover_btn)

        if event == cv2.EVENT_RBUTTONUP:
            self.right_dragging = False
            self.set_status("Pan updated.")

    def on_button_clicked(self, btn_id):
        if btn_id in self.filter_states:
            self.filter_states[btn_id] = not self.filter_states[btn_id]
            st = "ON" if self.filter_states[btn_id] else "OFF"
            self.set_status(f"[{btn_id.upper()}] toggled {st}")

        elif btn_id == "flip":
            self.current_source = cv2.flip(self.current_source, 1)
            self.cached_bg_mask = None
            self.set_status("Flipped image horizontally.")

        elif btn_id == "rotate":
            self.current_source = cv2.rotate(self.current_source, cv2.ROTATE_90_CLOCKWISE)
            self.cached_bg_mask = None
            self.set_status("Rotated image 90 degrees.")

        elif btn_id == "crop":
            self.trigger_crop()

        elif btn_id == "reset":
            self.reset_all()

        elif btn_id == "save":
            self.save_image()

    def trigger_crop(self):
        self.set_status("Select ROI box on pop-up window, then press SPACE / ENTER.")
        roi = cv2.selectROI(WINDOW_NAME + " - Crop Selection", self.current_source, showCrosshair=True, fromCenter=False)
        cv2.destroyWindow(WINDOW_NAME + " - Crop Selection")
        x, y, w, h = roi
        if w > 15 and h > 15:
            self.current_source = self.current_source[y:y+h, x:x+w].copy()
            self.cached_bg_mask = None
            self.set_status(f"Cropped ROI ({w}x{h}). Press 'Reset All' to restore.")
        else:
            self.set_status("Crop canceled.")

    def reset_all(self):
        for k in self.filter_states:
            self.filter_states[k] = False
        self.current_source = self.original_image.copy()
        self.cached_bg_mask = None

        self.tb_brightness = 50
        self.tb_contrast = 10
        self.tb_hue = 0
        self.tb_blur = 0
        self.tb_bg_hue = 100
        self.tb_zoom = 100
        self.tb_pan_x = 200
        self.tb_pan_y = 200

        cv2.setTrackbarPos("Brightness", WINDOW_NAME, 50)
        cv2.setTrackbarPos("Contrast", WINDOW_NAME, 10)
        cv2.setTrackbarPos("Hue Shift", WINDOW_NAME, 0)
        cv2.setTrackbarPos("Blur", WINDOW_NAME, 0)
        cv2.setTrackbarPos("BG Color (Hue)", WINDOW_NAME, 100)
        cv2.setTrackbarPos("Scale / Zoom", WINDOW_NAME, 100)
        cv2.setTrackbarPos("Move X (Pan)", WINDOW_NAME, 200)
        cv2.setTrackbarPos("Move Y (Pan)", WINDOW_NAME, 200)

        self.crosshair_x = self.canvas_w // 2
        self.crosshair_y = CANVAS_HEIGHT // 2
        self.set_status("All adjustments, positions and filters reset to defaults.")

    def save_image(self):
        processed = self.apply_filters()
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        filename = f"gui_export_{timestamp}.png"
        filepath = os.path.join(self.output_dir, filename)
        cv2.imwrite(filepath, processed)
        self.set_status(f"Saved: {filename} in output_results/")
        print(f"[CV Studio] Successfully exported: {filepath}")

    def set_status(self, msg):
        self.status_message = msg
        self.status_timestamp = time.time()

    def run(self):
        cv2.namedWindow(WINDOW_NAME, cv2.WINDOW_AUTOSIZE)
        cv2.setMouseCallback(WINDOW_NAME, self.handle_mouse)

        cv2.createTrackbar("Brightness", WINDOW_NAME, 50, 100, self.on_brightness)
        cv2.createTrackbar("Contrast", WINDOW_NAME, 10, 30, self.on_contrast)
        cv2.createTrackbar("Hue Shift", WINDOW_NAME, 0, 180, self.on_hue)
        cv2.createTrackbar("Blur", WINDOW_NAME, 0, 25, self.on_blur)
        cv2.createTrackbar("BG Color (Hue)", WINDOW_NAME, 100, 180, self.on_bg_hue)
        cv2.createTrackbar("Scale / Zoom", WINDOW_NAME, 100, 200, self.on_zoom)
        cv2.createTrackbar("Move X (Pan)", WINDOW_NAME, 200, 400, self.on_pan_x)
        cv2.createTrackbar("Move Y (Pan)", WINDOW_NAME, 200, 400, self.on_pan_y)

        print("=" * 70)
        print("  🚀 OpenCV Interactive Studio v2.0 PRO Active!")
        print("=" * 70)
        print("  Toolbar Controls:")
        print("    [Remove BG]   : Removes background + replaces with dynamic color scale!")
        print("    [Beauty Cam]  : Smooths skin / blemishes while keeping eyes sharp")
        print("    [Cartoon]     : Stylized comic art cel-shaded effect")
        print("    [Face Mark]   : Colored landmark bounding boxes (Eyes/Nose/Lips/Face)")
        print("    [Flip H]      : Flip mirror horizontally")
        print("    [Rotate 90]   : Rotate clockwise")
        print("  Position & Zoom Controls:")
        print("    - Trackbars   : 'Scale / Zoom', 'Move X (Pan)', 'Move Y (Pan)'")
        print("    - Arrow Keys  : Left, Right, Up, Down to pan position")
        print("    - [+] / [-]   : Zoom in / Zoom out")
        print("    - Right-Drag  : Drag mouse right-button to pan freely")
        print("  Hotkeys:")
        print("    [s] = Save | [c] = Crop ROI | [r] = Reset | [q] = Exit")
        print("=" * 70)

        while True:
            processed = self.apply_filters()
            canvas = self.render_canvas(processed)

            cv2.imshow(WINDOW_NAME, canvas)
            key = cv2.waitKey(20) & 0xFF

            if key == ord('q') or key == 27:
                break
            elif key == ord('s'):
                self.save_image()
            elif key == ord('c'):
                self.trigger_crop()
            elif key == ord('r'):
                self.reset_all()

            # Arrow keys for moving left / right / up / down
            elif key == 81 or key == 2424832:
                self.tb_pan_x = max(0, self.tb_pan_x - 10)
                cv2.setTrackbarPos("Move X (Pan)", WINDOW_NAME, self.tb_pan_x)
            elif key == 83 or key == 2555904:
                self.tb_pan_x = min(400, self.tb_pan_x + 10)
                cv2.setTrackbarPos("Move X (Pan)", WINDOW_NAME, self.tb_pan_x)
            elif key == 82 or key == 2490368:
                self.tb_pan_y = max(0, self.tb_pan_y - 10)
                cv2.setTrackbarPos("Move Y (Pan)", WINDOW_NAME, self.tb_pan_y)
            elif key == 84 or key == 2621440:
                self.tb_pan_y = min(400, self.tb_pan_y + 10)
                cv2.setTrackbarPos("Move Y (Pan)", WINDOW_NAME, self.tb_pan_y)

            # Zoom keys
            elif key == ord('+') or key == ord('='):
                self.tb_zoom = min(200, self.tb_zoom + 5)
                cv2.setTrackbarPos("Scale / Zoom", WINDOW_NAME, self.tb_zoom)
            elif key == ord('-') or key == ord('_'):
                self.tb_zoom = max(20, self.tb_zoom - 5)
                cv2.setTrackbarPos("Scale / Zoom", WINDOW_NAME, self.tb_zoom)

        cv2.destroyAllWindows()
        print("[CV Studio] Application closed cleanly.")

if __name__ == "__main__":
    print("-" * 65)
    print("Welcome to OpenCV Interactive Studio v2.0 PRO!")
    print("Enter custom image path or press ENTER for default 'resources/boy.jpg':")
    print("-" * 65)
    custom_path = None
    try:
        user_input = input("Enter image path (or press Enter for default): ").strip().strip('"').strip("'")
        if user_input:
            custom_path = user_input
    except Exception:
        pass
    app = CVStudioApp(custom_path)
    app.run()
