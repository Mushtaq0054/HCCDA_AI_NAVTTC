"""
NLP Preprocessing & Linguistic Analysis Module
Implements techniques from Corvit NLP Lecture 8 (Fawad Bahadur):
- Text Normalization & Contraction Expansion (Slides 27-28)
- Regex-based Noise Cleaning (Slides 29-31)
- spaCy Linguistic Inspection (Tokens, POS, Lemmatization) (Slides 14, 19-24)
- Safe Preprocessing for Machine Translation vs. Lab Demonstration
"""

import re
from typing import Dict, List, Any

# Common English Contractions & Slang Mappings (Lecture Slides 27-28)
CONTRACTIONS_DICT = {
    r"\bi'm\b": "I am",
    r"\bi've\b": "I have",
    r"\bi'll\b": "I will",
    r"\bi'd\b": "I would",
    r"\byou're\b": "you are",
    r"\byou've\b": "you have",
    r"\byou'll\b": "you will",
    r"\byou'd\b": "you would",
    r"\bhe's\b": "he is",
    r"\bshe's\b": "she is",
    r"\bit's\b": "it is",
    r"\bwe're\b": "we are",
    r"\bthey're\b": "they are",
    r"\bdon't\b": "do not",
    r"\bdoesn't\b": "does not",
    r"\bdidn't\b": "did not",
    r"\bcan't\b": "cannot",
    r"\bcouldn't\b": "could not",
    r"\bwon't\b": "will not",
    r"\bwouldn't\b": "would not",
    r"\bshouldn't\b": "should not",
    r"\bhasn't\b": "has not",
    r"\bhaven't\b": "have not",
    r"\bhadn't\b": "had not",
    r"\bisn't\b": "is not",
    r"\baren't\b": "are not",
    r"\bwasn't\b": "was not",
    r"\bweren't\b": "were not",
    # Informal Slang (Slide 27-28)
    r"\bgonna\b": "going to",
    r"\bwanna\b": "want to",
    r"\bgotta\b": "got to",
    r"\bkinda\b": "kind of",
    r"\blol\b": "laughing out loud",
    r"\bpls\b": "please",
    r"\bplz\b": "please",
    r"\bu\b": "you",
    r"\br\b": "are",
    r"\bur\b": "your"
}

def expand_contractions(text: str) -> str:
    """
    Expands conversational contractions and common slang words.
    Lecture 8 Slides 27-28.
    """
    cleaned = text
    for pattern, replacement in CONTRACTIONS_DICT.items():
        cleaned = re.sub(pattern, replacement, cleaned, flags=re.IGNORECASE)
    return cleaned

def clean_noise_regex(text: str) -> str:
    """
    Removes URLs, HTML tags, excess whitespace, and irrelevant symbols using Regex.
    Lecture 8 Slides 29-31.
    """
    # Remove HTML tags if any
    text = re.sub(r"<[^>]+>", " ", text)
    # Remove URLs
    text = re.sub(r"http\S+|www\.\S+", " ", text)
    # Normalize multiple spaces, tabs, and newlines
    text = re.sub(r"\s+", " ", text)
    return text.strip()

def preprocess_for_translation(text: str) -> str:
    """
    Preprocesses text specifically for Seq2Seq Transformer translation.
    IMPORTANT (Lecture Slide 18 & 26):
    We do NOT remove stop words (e.g., 'not') or apply aggressive stemming,
    as machine translation requires full grammatical context and tense.
    """
    if not text:
        return ""
    # 1. Expand contractions & slang
    text = expand_contractions(text)
    # 2. Clean regex noise
    text = clean_noise_regex(text)
    return text

def analyze_linguistics_spacy(text: str, nlp_model=None) -> List[Dict[str, Any]]:
    """
    Analyzes text with spaCy for tokenization, POS tagging, and lemmatization.
    Lecture 8 Slides 14, 19-24.
    """
    if nlp_model is None:
        try:
            import spacy
            nlp_model = spacy.load("en_core_web_sm")
        except Exception:
            return []

    doc = nlp_model(text)
    tokens_data = []
    for token in doc:
        tokens_data.append({
            "Token": token.text,
            "Lemma": token.lemma_,
            "POS": token.pos_,
            "Tag": token.tag_,
            "Is_Stopword": token.is_stop
        })
    return tokens_data
