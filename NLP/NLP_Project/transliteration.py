"""
Urdu to Roman Urdu Transliteration Engine
Provides both dictionary-assisted natural mapping and rule-based phonetic fallback.
"""

import re

# High-frequency dictionary mapping for accurate and natural Roman Urdu words
COMMON_URDU_WORDS = {
    "آپ": "aap",
    "کیسے": "kaise",
    "کیسی": "kaisi",
    "ہیں": "hain",
    "ہو": "ho",
    "ہے": "hai",
    "ہوں": "hoon",
    "میں": "main",
    "ہم": "hum",
    "تم": "tum",
    "وہ": "woh",
    "یہ": "yeh",
    "کیا": "kya",
    "کیوں": "kyun",
    "کہاں": "kahan",
    "کب": "kab",
    "کون": "kaun",
    "کس": "kis",
    "نہیں": "nahi",
    "نہ": "na",
    "ہاں": "haan",
    "اور": "aur",
    "یا": "ya",
    "پر": "par",
    "سے": "se",
    "کو": "ko",
    "کا": "ka",
    "کے": "ke",
    "کی": "ki",
    "تھا": "tha",
    "تھی": "thi",
    "تھے": "the",
    "کر": "kar",
    "کرنا": "karna",
    "کرتا": "karta",
    "کرتی": "karti",
    "کرتے": "karte",
    "سکتا": "sakta",
    "سکتی": "sakti",
    "سکتے": "sakte",
    "چاہتا": "chahta",
    "چاہتی": "chahti",
    "چاہتے": "chahte",
    "چاہیے": "chahiye",
    "رہا": "raha",
    "رہی": "rahi",
    "رہے": "rahe",
    "گیا": "gaya",
    "گئی": "gayi",
    "گئے": "gaye",
    "والا": "wala",
    "والی": "wali",
    "والے": "wale",
    "بہت": "bohat",
    "زیادہ": "zyada",
    "کم": "kam",
    "اچھا": "acha",
    "اچھی": "achi",
    "اچھے": "ache",
    "برا": "bura",
    "بڑی": "bari",
    "بڑا": "bara",
    "بڑے": "bare",
    "چھوٹا": "chota",
    "چھوٹی": "choti",
    "چھوٹے": "chote",
    "ٹھیک": "theek",
    "شکریہ": "shukriya",
    "خوش": "khush",
    "آمدید": "aamdeed",
    "سلام": "salam",
    "مصنوعی": "masnooi",
    "ذہانت": "zehanat",
    "سیکھنا": "seekhna",
    "پڑھنا": "parhna",
    "لکھنا": "likhna",
    "بولنا": "bolna",
    "سمجھنا": "samajhna",
    "پروجیکٹ": "project",
    "کمپیوٹر": "computer",
    "انگریزی": "angrezi",
    "اردو": "urdu",
    "زبان": "zuban",
    "ترجمہ": "tarjuma",
    "کتاب": "kitaab",
    "سکول": "school",
    "کالج": "college",
    "یونیورسٹی": "university",
    "گھر": "ghar",
    "کام": "kaam",
    "دوست": "dost",
    "محبت": "mohabbat",
    "زندگی": "zindagi",
    "وقت": "waqt",
    "دن": "din",
    "رات": "raat",
    "صبح": "subah",
    "شام": "shaam",
    "آج": "aaj",
    "کل": "kal",
    "اب": "ab",
    "پھر": "phir",
    "ہمیشہ": "hamesha",
    "کبھی": "kabhi",
    "پاس": "paas",
    "ساتھ": "saath",
    "بعد": "baad",
    "پہلے": "pehle",
    "صرف": "sirf",
    "سب": "sab",
    "سبق": "sabaq",
    "استاد": "ustaad",
    "طالب": "talib",
    "علم": "ilm",
    "پاکستان": "Pakistan"
}

# Phonetic character mapping for fallback
URDU_CHAR_MAP = {
    "ا": "a",
    "آ": "aa",
    "ب": "b",
    "پ": "p",
    "ت": "t",
    "ٹ": "t",
    "ث": "s",
    "ج": "j",
    "چ": "ch",
    "ح": "h",
    "خ": "kh",
    "د": "d",
    "ڈ": "d",
    "ذ": "z",
    "ر": "r",
    "ڑ": "r",
    "ز": "z",
    "ژ": "zh",
    "س": "s",
    "ش": "sh",
    "ص": "s",
    "ض": "z",
    "ط": "t",
    "ظ": "z",
    "ع": "a",
    "غ": "gh",
    "ف": "f",
    "ق": "q",
    "ک": "k",
    "گ": "g",
    "ل": "l",
    "م": "m",
    "ن": "n",
    "ں": "n",
    "و": "o",
    "ہ": "h",
    "ھ": "h",
    "ء": "",
    "ی": "i",
    "ئے": "ye",
    "ئ": "i",
    "ے": "e",
    "ۃ": "t",
    "۔": ".",
    "،": ",",
    "؟": "?",
    "؛": ";",
    "٪": "%"
}

# Diacritics to strip
DIACRITICS = re.compile(r"[\u064B-\u065F\u0670]")

def clean_urdu_word(word: str) -> str:
    """Removes diacritics and surrounding punctuation for cleaner lookup."""
    word = DIACRITICS.sub("", word)
    return word.strip(".,!?؛،۔")

def transliterate_word(word: str) -> str:
    """Transliterates a single Urdu word to Roman Urdu."""
    cleaned = clean_urdu_word(word)
    if not cleaned:
        return word

    # 1. Exact dictionary match
    if cleaned in COMMON_URDU_WORDS:
        roman = COMMON_URDU_WORDS[cleaned]
        # Preserve trailing punctuation
        if word.endswith("۔"):
            roman += "."
        elif word.endswith("،"):
            roman += ","
        elif word.endswith("؟"):
            roman += "?"
        return roman

    # 2. Rule-based phonetic transliteration
    res = []
    i = 0
    w_len = len(cleaned)
    while i < w_len:
        ch = cleaned[i]
        # Multi-char combinations
        if i < w_len - 1 and cleaned[i:i+2] in ["ئے"]:
            res.append("ye")
            i += 2
            continue
        if ch in URDU_CHAR_MAP:
            res.append(URDU_CHAR_MAP[ch])
        else:
            res.append(ch)
        i += 1

    trans = "".join(res)
    # Basic post-processing for natural vowels
    trans = re.sub(r"aa+", "aa", trans)
    trans = re.sub(r"ee+", "ee", trans)
    trans = re.sub(r"oo+", "oo", trans)

    # Attach punctuation if present
    if word.endswith("۔"):
        trans += "."
    elif word.endswith("،"):
        trans += ","
    elif word.endswith("؟"):
        trans += "?"

    return trans

def urdu_to_roman(text: str, capitalize_first: bool = True) -> str:
    """
    Converts Urdu script sentence into natural Roman Urdu text.
    Handles punctuation, capitalization, and multi-word sentences.
    """
    if not text:
        return ""

    tokens = text.split()
    roman_tokens = [transliterate_word(tok) for tok in tokens]
    roman_text = " ".join(roman_tokens)

    # Format sentences nicely
    if capitalize_first and roman_text:
        roman_text = roman_text[0].upper() + roman_text[1:]

    # Clean redundant spaces before punctuation
    roman_text = re.sub(r"\s+([.,?!])", r"\1", roman_text)
    return roman_text
