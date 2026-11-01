# 🤖 Huawei Certified Developer Associate - AI (HCCDA - AI) | NAVTTC

<div align="center">

[![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Anaconda](https://img.shields.io/badge/Conda-Environment-44A833?style=for-the-badge&logo=anaconda&logoColor=white)](https://www.anaconda.com/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?style=for-the-badge&logo=jupyter&logoColor=white)](https://jupyter.org/)
[![OpenCV](https://img.shields.io/badge/OpenCV-Computer_Vision-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)](https://opencv.org/)
[![Deep Learning](https://img.shields.io/badge/Deep_Learning-Neural_Networks-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)](https://www.tensorflow.org/)
[![NLP](https://img.shields.io/badge/NLP-Natural_Language-25D366?style=for-the-badge&logo=huggingface&logoColor=white)](https://huggingface.co/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Scikit-Learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Data_Analysis-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![NumPy](https://img.shields.io/badge/NumPy-Scientific_Computing-013243?style=for-the-badge&logo=numpy&logoColor=white)](https://numpy.org/)

<br/>

**Comprehensive Hands-on Labs, Deep Learning, Natural Language Processing (NLP), Computer Vision, Machine Learning & Certification Preparation**  
*Conducted under the NAVTTC (National Vocational and Technical Training Commission) AI Training Initiative & Huawei Certification Program.*

</div>

---

## 📌 Table of Contents
- [📖 About the Program](#-about-the-program)
- [🎯 Learning Objectives](#-learning-objectives)
- [📂 Repository Structure](#-repository-structure)
- [🔬 Modules & Project Highlights](#-modules--project-highlights)
- [📊 Datasets](#-datasets)
- [⚙️ Setup & Installation (Anaconda / Conda)](#️-setup--installation-anaconda--conda)
- [🚀 How to Run](#-how-to-run)
- [👤 Connect With Me](#-connect-with-me)
- [📜 License](#-license)

---

## 📖 About the Program

This repository houses all the coursework, practical labs, neural network implementations, Computer Vision apps, Natural Language Processing pipelines, Exploratory Data Analysis (EDA), and Huawei Cloud AI preparation materials developed during the **HCCDA - AI (Huawei Certified Developer Associate - Artificial Intelligence)** program facilitated by **NAVTTC**.

The curriculum spans from fundamentals to advanced AI tracks:
- **Python Foundations & Scientific Computing** (NumPy, Pandas, Matplotlib, Seaborn)
- **Supervised Machine Learning** (Linear & Logistic Regression with Scikit-Learn and Scratch)
- **Deep Learning Foundations** (Binary Classification, Forward/Backward Propagation, Neural Network Mindset)
- **Computer Vision & GUI Applications** (OpenCV, Haar Cascades Face & Eye Detection, Real-time Webcam Processing)
- **Natural Language Processing (NLP)** (Text Preprocessing, Tokenization, Transliteration, Interactive Streamlit Web Apps)
- **Huawei Cloud AI & Certification Prep** (HCIA/HCCDA AI Study Guides, Lecture Notes, 5-Phase MCQ Exam Question Banks)

---

## 🎯 Learning Objectives

- [x] Master Python numerical workflows, multidimensional arrays, tensor reshaping, and vectorization with NumPy.
- [x] Conduct end-to-end Exploratory Data Analysis (EDA) and visualizations on real-world datasets (Titanic, Iris, IMDB).
- [x] Build and optimize **Supervised Machine Learning Models** (Linear Regression, Logistic Regression, Decision Boundaries).
- [x] Develop a **Deep Learning Neural Network** classifier from scratch using vectorization and gradient descent.
- [x] Create real-time **Computer Vision applications** with OpenCV, Haar Cascades, and desktop GUI interfaces.
- [x] Design **NLP pipelines** for text normalization, cleaning, transliteration, and build a full-stack **Streamlit** app.
- [x] Master Huawei AI architecture, Ascend AI Chips, MindSpore framework, and ModelArts workflows.

---

## 📂 Repository Structure

```text
HCCDA_AI_NAVTTC/
├── Computer Vision/                                    # Computer Vision & Real-time Processing
│   ├── GUI_cv2.py                                      # Desktop GUI application for CV filters & detection
│   ├── run_GUI.bat                                     # Windows one-click batch launcher for CV GUI
│   ├── live_face_detection.ipynb                       # Real-time face detection using webcam stream
│   ├── face_detetcion_task.ipynb                       # Haar Cascade face and eye detection exercises
│   ├── OpenCV_Lab.ipynb                                # Core OpenCV transformations, filters & color spaces
│   ├── Task.ipynb                                      # Practical image processing & detection challenges
│   ├── fruit.ipynb                                     # Fruit ripeness detection & color segmentation
│   ├── haarcascade_frontalface_default.xml             # Pre-trained frontal face cascade classifier
│   ├── haarcascade_eye.xml                             # Pre-trained eye cascade classifier
│   ├── detected_faces.jpg                              # Output visual of face detection results
│   ├── Lec 7 (Computer Vision).pdf                     # Lecture slide notes on Computer Vision
│   ├── images/                                         # Test images for computer vision experiments
│   └── resources/                                      # Cascade models and sample video assets (cctv.mp4)
├── Deep learning/                                      # Deep Learning Foundations & Neural Networks
│   └── fisrt day of DL/
│       ├── Logistic_Regression_with_a_Neural_Network_mindset.ipynb  # Neural network binary classifier from scratch
│       ├── lr_utils.py                                 # Data loading utilities for H5 datasets
│       ├── datasets/                                   # Cat vs Non-Cat classification datasets (train/test .h5)
│       └── images/                                     # Sample test images for model evaluation
├── NLP/                                                # Natural Language Processing & Text Analytics
│   ├── NLP_Lab.ipynb                                   # Hands-on NLP exercises (tokenization, stopwords, regex)
│   ├── NLP_Cheat_Sheet.ipynb                           # Comprehensive NLP quick-reference guide
│   ├── Updated_NLP_Cheat_Sheet.ipynb                   # Expanded NLP reference with advanced pipelines
│   ├── Lec 8 (NLP).pdf                                 # NLP lecture slides & theoretical foundations
│   └── NLP_Project/                                    # Full-stack Streamlit NLP Web Application
│       ├── app.py                                      # Streamlit interactive UI application
│       ├── preprocessing.py                            # Text cleaning, normalization & preprocessing logic
│       ├── transliteration.py                          # Roman-to-Urdu / text transliteration utilities
│       ├── NLP_Project_Pipeline.ipynb                  # Development and validation pipeline
│       └── requirements.txt                            # App-specific dependencies
├── Initial Documents and MCQS/                         # Huawei Certification Exam Prep & Question Banks
│   ├── TLM-HCCDA AI V 2.0 (1).pdf                      # Official HCCDA AI v2.0 Training Learning Material
│   ├── HCIA-AI-Course-main/                            # HCIA AI complete reference slides (MindSpore, Chips, Cloud)
│   └── Quiz/                                           # 100 MCQ Practice Sets & Exam Preparation Guides
│       ├── ML_AI_100_MCQ_Complete_Guide_ENGLISH.pdf
│       ├── Computer_Vision_100_MCQ_Complete_Guide_ENGLISH.pdf
│       └── HCCDA_AI_5_Phase_100_MCQ_Exam_Preparation_*.pdf
├── 1.Linear Regression Model.ipynb                     # Supervised ML: Linear Regression (scratch & scikit-learn)
├── Copy_of_PythonforDS.ipynb                           # Comprehensive Python for Data Science guide
├── HCCDA-AI-Day-2-Lab-1.ipynb                          # HCCDA-AI Day 2 Practical Lab on AI workflows
├── Iris Dataset/                                       # Iris Flower Classification & Regression
│   ├── iris_EDA_with_Training.ipynb                    # End-to-end EDA and model training pipeline
│   ├── iris_linear_regression_model.ipynb              # Linear regression applied to continuous features
│   └── Iris Logistic Regression.ipynb                  # Logistic regression multiclass classifier
├── Titanic Dataset/                                    # Titanic Survival Analysis Collection
│   ├── data/                                           # Training and test CSV datasets
│   ├── EDA_Titanic_dataset.ipynb                       # Comprehensive Titanic EDA notebook
│   ├── Titanic_EDA.ipynb                               # Demographic survival rate breakdown
│   ├── data_visualisation.ipynb                        # Statistical visualization masterclass
│   ├── sir_lec_titanic.ipynb                           # Instructor lecture notes & lab walkthrough
│   └── titanic eda.ipynb                               # Alternative exploratory patterns & insights
├── datasets/
│   ├── IMDB-Movie-Data.csv                             # 1,000 top movies dataset (rating & revenue)
│   └── titanic_dataset.xlsx                            # Classic Titanic Excel dataset
├── complete_numpy_course_for_beginners_complete.ipynb  # Complete beginner-to-advanced NumPy course
├── numpy_2d_array.ipynb                                # 2D Array operations, slicing & masking
├── numpy_3d_array.ipynb                                # 3D Array / Tensor structures and operations
├── list_concat.ipynb                                   # Python sequence manipulation techniques
├── one_to_hundred.csv                                  # Sample generated numerical dataset (CSV)
├── one_to_hundred.py                                   # Python script for array generation & testing
├── week_2.py                                           # Week 2 introductory Python script
├── requirements.txt                                    # Project dependencies
├── .gitignore                                          # Standard Git ignore rules
└── README.md                                           # Documentation & project guide
```

---

## 🔬 Modules & Project Highlights

### 1. 🧠 Deep Learning with Neural Network Mindset (`Deep learning/`)
- **Forward & Backward Propagation**: Implemented vectorized computation from mathematical first principles.
- **Sigmoid Activation & Loss**: Computed cross-entropy cost function and analytical gradients ($dw, db$).
- **Cat vs. Non-Cat Classifier**: Evaluated on preprocessed H5 image datasets (`train_catvnoncat.h5`).

### 2. 💬 Natural Language Processing & Streamlit App (`NLP/`)
- **Text Preprocessing**: Tokenization, lemmatization, stopword removal, regular expression filtering, and vocabulary indexing.
- **Roman Urdu / English Transliteration**: Rule-based and mapped string conversion algorithms.
- **Interactive Web App**: Standalone Streamlit dashboard (`app.py`) allowing interactive real-time text analysis.

### 3. 👁️ Computer Vision & Real-Time GUI (`Computer Vision/`)
- **Face & Eye Detection**: Haar Feature-based Cascade Classifiers applied to static images and live video streams.
- **Interactive CV GUI (`GUI_cv2.py`)**: Tkinter/OpenCV desktop tool to dynamically apply filters, edge detection, and thresholding.
- **Fruit Ripeness & Segmentation**: Hue channel extraction and Otsu's thresholding for agricultural sorting.

### 4. 🤖 Supervised Machine Learning & Regression (`1.Linear Regression Model.ipynb`, `Iris Dataset/`)
- **Linear & Logistic Regression**: Mathematical cost functions, gradient descent optimization, and Scikit-Learn APIs.
- **Model Evaluation**: Precision, Recall, F1-Score, Confusion Matrices, and $R^2$ scores.

### 5. 🚢 Exploratory Data Analysis & Visualization (`Titanic Dataset/`)
- Comprehensive demographic analysis, missing value imputations, correlation matrices, and distribution styling with Seaborn.

### 6. 📚 Certification Preparation & Practice Exams (`Initial Documents and MCQS/`)
- Official Huawei AI syllabus materials, MindSpore frameworks, Ascend AI Chips overview, and hundreds of verified practice MCQs across 5 study phases.

---

## 📊 Datasets

| Dataset | Location | Format | Description |
|---|---|---|---|
| **Cat vs Non-Cat** | `Deep learning/fisrt day of DL/datasets/` | `.h5` | 209 train & 50 test labeled images ($64 \times 64 \times 3$) for binary image classification. |
| **Computer Vision Assets** | `Computer Vision/resources/`, `images/` | `.jpg`, `.mp4` | Face detection test samples and CCTV surveillance footage. |
| **Titanic Dataset** | `Titanic Dataset/data/` | `.csv`, `.xlsx` | Passenger demographics, ticket class, and survival outcome. |
| **Iris Dataset** | `Iris Dataset/` | In-memory / `.csv` | 150 iris flower instances with 4 morphological features across 3 species. |
| **IMDB Movie Data** | `datasets/IMDB-Movie-Data.csv` | `.csv` | 1,000 top movies (2006–2016) with revenue, ratings, genre, and director. |

---

## ⚙️ Setup & Installation (Anaconda / Conda)

Follow these steps to set up the environment and run the notebooks:

### 1. Clone the repository
```bash
git clone https://github.com/Mushtaq0054/HCCDA_AI_NAVTTC.git
cd HCCDA_AI_NAVTTC
```

### 2. Create & Activate Conda Environment
Open **Anaconda Prompt** or terminal and run:

```bash
# Create a new conda environment with Python 3.12
conda create -n hccda_ai python=3.12 -y

# Activate the conda environment
conda activate hccda_ai
```

### 3. Install Dependencies
```bash
# Upgrade pip and install required packages
pip install --upgrade pip
pip install -r requirements.txt
```

---

## 🚀 How to Run

### 📓 Jupyter Notebooks
Launch Jupyter Notebook inside your activated Conda environment:
```bash
jupyter notebook
```

### 🖥️ Computer Vision GUI Application
Run the desktop computer vision application:
```bash
python "Computer Vision/GUI_cv2.py"
# or double-click "Computer Vision/run_GUI.bat"
```

### 🌐 Streamlit NLP Web Application
Run the interactive NLP dashboard:
```bash
cd NLP/NLP_Project
streamlit run app.py
```

---

## 👤 Connect With Me

<div align="center">

### **Mushtaq Ahmad Madni**
*AI & Data Science Enthusiast | HCCDA - AI Trainee (NAVTTC)*

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Mushtaq_Madni-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/mushtaq-madni)
[![Portfolio](https://img.shields.io/badge/Portfolio-Live_Website-000000?style=for-the-badge&logo=vercel&logoColor=white)](https://mushtaq-portfolio-pi.vercel.app)
[![GitHub](https://img.shields.io/badge/GitHub-Mushtaq0054-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Mushtaq0054)

</div>

---

## 📜 License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT) - feel free to use and adapt the code for educational and learning purposes.
