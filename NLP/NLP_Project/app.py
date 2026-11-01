"""
Multilingual Text Translator Web Application
English to Urdu & Roman Urdu using Hugging Face Transformers & spaCy
Course: Natural Language Processing (Instructor: Fawad Bahadur, Corvit)
"""

# pyrefly: ignore[missing-import]
import streamlit as st
# pyrefly: ignore[missing-import]
import torch
import pandas as pd
# Direct submodule import avoids Streamlit's file-watcher scanning vision modules
# pyrefly: ignore[missing-import]
from transformers.models.marian import MarianMTModel, MarianTokenizer

from preprocessing import preprocess_for_translation, analyze_linguistics_spacy
from transliteration import urdu_to_roman

# Page Configuration
st.set_page_config(
    page_title="Multilingual Translator: EN to Urdu & Roman Urdu",
    page_icon="🌐",
    layout="wide"
)

# Custom Styling for Nastaliq Urdu Font and Modern Cards
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Nastaliq+Urdu:wght@400;700&family=Outfit:wght@300;400;600;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Outfit', sans-serif;
    }
    
    .urdu-text {
        font-family: 'Noto Nastaliq Urdu', serif;
        direction: rtl;
        text-align: right;
        font-size: 1.85rem;
        line-height: 2.3;
        color: #1a4d2e;
        background-color: #f4fbf7;
        padding: 20px 24px;
        border-radius: 12px;
        border: 1px solid #b7e4c7;
        margin-top: 10px;
    }
    
    .roman-text {
        font-size: 1.45rem;
        font-weight: 500;
        color: #1d3557;
        background-color: #f1faee;
        padding: 18px 24px;
        border-radius: 12px;
        border: 1px solid #a8dadc;
        margin-top: 10px;
    }
    
    .badge {
        display: inline-block;
        padding: 4px 10px;
        border-radius: 20px;
        font-size: 0.8rem;
        font-weight: 600;
        text-transform: uppercase;
        margin-bottom: 8px;
    }
    .badge-urdu {
        background-color: #d8f3dc;
        color: #2d6a4f;
    }
    .badge-roman {
        background-color: #e0f2fe;
        color: #0369a1;
    }
</style>
""", unsafe_allow_html=True)

# Cache Model and Tokenizer for Fast Inference
@st.cache_resource(show_spinner="Loading Helsinki-NLP Seq2Seq Transformer model...")
def load_translation_pipeline():
    model_name = "Helsinki-NLP/opus-mt-en-ur"
    tokenizer = MarianTokenizer.from_pretrained(model_name)
    model = MarianMTModel.from_pretrained(model_name)
    device = "cuda" if torch.cuda.is_available() else "cpu"
    model = model.to(device)
    model.eval()
    return tokenizer, model, device

# Header Section
st.title("🌐 Multilingual Text Translator")
st.markdown("### English $\\rightarrow$ Urdu Script & Roman Urdu Using Transformers")
st.caption("Corvit NLP Course Project | Instructor: Fawad Bahadur | Seq2Seq Neural Machine Translation")

# Sidebar for Course Details and Controls
with st.sidebar:
    st.header("Project Details")
    st.info("""
    **Core Pipeline Components:**
    1. **Normalization**: Contractions & Regex noise cleaning.
    2. **spaCy**: Tokenization, POS Tagging, & Lemmatization.
    3. **Transformer**: `Helsinki-NLP/opus-mt-en-ur` (MarianMT Seq2Seq).
    4. **Transliteration**: Lexicon-assisted Urdu to Roman Urdu engine.
    5. **Evaluation**: SacreBLEU & chrF metrics.
    """)
    
    st.markdown("---")
    sample_choice = st.selectbox(
        "Try sample sentences:",
        [
            "Select a sample...",
            "How are you?",
            "I want to learn artificial intelligence.",
            "I'm gonna attend the NLP lecture today, lol!",
            "This is a great computer science project.",
            "Don't worry, we will succeed.",
            "Where are you going with your friend?"
        ]
    )

# Input Area
default_input = "" if sample_choice == "Select a sample..." else sample_choice
user_input = st.text_area(
    "Enter English text to translate:",
    value=default_input,
    placeholder="Type an English sentence here (e.g. 'How are you?')...",
    height=120
)

col_btn, col_info = st.columns([1, 4])
with col_btn:
    translate_clicked = st.button("Translate Now 🚀", type="primary", use_container_width=True)

if translate_clicked or (user_input and sample_choice != "Select a sample..."):
    if not user_input.strip():
        st.warning("Please enter some English text to translate.")
    else:
        # Step 1: Preprocessing & Normalization
        cleaned_text = preprocess_for_translation(user_input)
        
        # Step 2: Translation with Transformer
        try:
            tokenizer, model, device = load_translation_pipeline()
            inputs = tokenizer(cleaned_text, return_tensors="pt", padding=True, truncation=True, max_length=128)
            inputs = {k: v.to(device) for k, v in inputs.items()}
            
            with torch.no_grad():
                generated_tokens = model.generate(
                    **inputs,
                    num_beams=4,
                    max_length=128,
                    early_stopping=True
                )
            urdu_output = tokenizer.decode(generated_tokens[0], skip_special_tokens=True)
            
            # Step 3: Transliteration to Roman Urdu
            roman_output = urdu_to_roman(urdu_output)
            
            # Display Results Side-by-Side
            st.markdown("---")
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown('<span class="badge badge-urdu">Urdu Script (اردو رسم الخط)</span>', unsafe_allow_html=True)
                st.markdown(f'<div class="urdu-text">{urdu_output}</div>', unsafe_allow_html=True)
                
            with col2:
                st.markdown('<span class="badge badge-roman">Roman Urdu (English Alphabets)</span>', unsafe_allow_html=True)
                st.markdown(f'<div class="roman-text">{roman_output}</div>', unsafe_allow_html=True)
            
            # Preprocessing & Linguistic Inspection Accordion (Demonstration of Class Concepts)
            with st.expander("🔍 Inspect NLP Preprocessing & spaCy Linguistic Features"):
                col_pre1, col_pre2 = st.columns(2)
                with col_pre1:
                    st.write("**Raw Input:**", user_input)
                with col_pre2:
                    st.write("**Normalized Input (Contractions & Regex applied):**", cleaned_text)
                    
                st.write("**spaCy Linguistic Analysis (Tokenization, POS, Lemma, Stopword):**")
                tokens_data = analyze_linguistics_spacy(cleaned_text)
                if tokens_data:
                    st.dataframe(pd.DataFrame(tokens_data), use_container_width=True)
                else:
                    st.info("spaCy `en_core_web_sm` model not installed locally. Run `python -m spacy download en_core_web_sm`.")
                    
        except Exception as e:
            st.error(f"Translation Error: {str(e)}")
            st.info("Make sure you have installed requirements: `pip install -r requirements.txt`")
