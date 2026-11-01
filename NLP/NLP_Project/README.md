# Multilingual Text Translator: English to Urdu and Roman Urdu Using Transformers

**Course**: Natural Language Processing (NLP)  
**Instructor**: Fawad Bahadur (Corvit)  
**Author**: Mushtaq Ahmad Madni  
**Repository Directory**: `c:\Users\Mushtaq Ahmad Madni\Desktop\HCCDA_AI\NLP\NLP_Project`

---

## 📖 Project Overview
This project delivers an end-to-end Neural Machine Translation (NMT) and Multilingual Text Processing solution that translates English input into both **Urdu Script (اردو رسم الخط)** and **Roman Urdu (English alphabets)** using state-of-the-art Transformers and linguistic preprocessing.

### Direct Mapping to Lecture 8 (`Lec 8 (NLP).pdf`)
- **Slide 4 & 6**: Language Translation via Transformer architectures (`Helsinki-NLP/opus-mt-en-ur` MarianMT Seq2Seq).
- **Slide 9**: Addressing multilinguality and code-switching via Roman Urdu generation (*"Main office jaa raha hoon"*).
- **Slide 10–12**: Implementing the full NLP pipeline from raw input to evaluation.
- **Slide 14 & 15**: Using `spaCy` for linguistic analysis and `Hugging Face Transformers` for sequence modeling.
- **Slide 17–31**: Text cleaning, contractions expansion, regex noise removal, tokenization, POS tagging, and lemmatization.

---

## 📁 Project Structure

```
NLP_Project/
│
├── NLP_Project_Pipeline.ipynb   # Main Jupyter Notebook containing the 5 discrete steps
├── preprocessing.py            # Normalization, Contractions, Regex, & spaCy helper functions
├── transliteration.py          # Urdu script to Roman Urdu transliteration engine
├── app.py                      # Interactive Streamlit Web Application (Nastaliq font + Live Inspector)
├── requirements.txt            # Required Python libraries
└── README.md                   # Project documentation & presentation guide
```

---

## 🔬 The 5 Distinct Notebook Steps

1. **Step 1: Raw Text Input & Informal English Normalization**
   - Expands conversational contractions (`don't` $\rightarrow$ `do not`, `I'm` $\rightarrow$ `I am`, `gonna` $\rightarrow$ `going to`).
   - Cleans unwanted noise, URLs, and extra spaces using regular expressions (`re`).
2. **Step 2: spaCy Linguistic Demonstration**
   - Extracts Word/Sentence Tokens, POS tags, and Lemmatization roots.
   - Highlights why stopwords (e.g. `not`, `are`) and grammatical inflections must be preserved for Machine Translation rather than blindly stripped.
3. **Step 3: Hugging Face Pretrained Transformer (English $\rightarrow$ Urdu)**
   - Loads the sequence-to-sequence MarianMT model (`Helsinki-NLP/opus-mt-en-ur`) using PyTorch and beam search decoding.
4. **Step 4: Urdu to Roman Urdu Transliteration**
   - Uses a curated high-frequency Urdu lexicon alongside phonetic fallback rules to render natural Roman Urdu.
5. **Step 5: Test Dataset Evaluation using SacreBLEU & chrF**
   - Compares predictions against gold-standard references and computes Corpus BLEU and character n-gram F-score (chrF).

---

## 🚀 How to Run

### 1. Install Dependencies
```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

### 2. Run the Jupyter Notebook
Open and execute [NLP_Project_Pipeline.ipynb](file:///c:/Users/Mushtaq%20Ahmad%20Madni/Desktop/HCCDA_AI/NLP/NLP_Project/NLP_Project_Pipeline.ipynb) step-by-step:
```bash
jupyter notebook NLP_Project_Pipeline.ipynb
```

### 3. Launch the Interactive Web Application
```bash
streamlit run app.py
```

---

## 💡 Key Viva & Presentation Talking Points for Sir
1. **Why not just remove stop words before translation?**
   - In text classification, stop words are removed to reduce dimensionality. However, in Machine Translation (MT), words like *"not"*, *"never"*, *"he"*, *"she"* define polarity, subject, and tense. Removing them would invert or corrupt the translation.
2. **Why Seq2Seq MarianMT instead of standard BERT?**
   - BERT is an Encoder-only model suited for understanding (classification/NER). Machine Translation requires an Encoder-Decoder (Seq2Seq) architecture where the encoder processes English and the autoregressive decoder generates Urdu tokens.
3. **Why Roman Urdu?**
   - Slide 9 mentions Multilinguality & Code-Switching. A huge proportion of mobile and social messaging in Pakistan is typed in Roman Urdu, making multi-script translation essential for real-world user accessibility.
