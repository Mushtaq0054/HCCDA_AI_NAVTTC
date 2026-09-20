# 🤖 Huawei Certified Developer Associate - AI (HCCDA - AI) | NAVTTC

<div align="center">

[![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Anaconda](https://img.shields.io/badge/Conda-Environment-44A833?style=for-the-badge&logo=anaconda&logoColor=white)](https://www.anaconda.com/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?style=for-the-badge&logo=jupyter&logoColor=white)](https://jupyter.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Data_Analysis-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![NumPy](https://img.shields.io/badge/NumPy-Scientific_Computing-013243?style=for-the-badge&logo=numpy&logoColor=white)](https://numpy.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-11557c?style=for-the-badge&logo=plotly&logoColor=white)](https://matplotlib.org/)
[![Seaborn](https://img.shields.io/badge/Seaborn-Statistical_Plots-388E3C?style=for-the-badge&logo=scipy&logoColor=white)](https://seaborn.pydata.org/)

<br/>

**Hands-on Labs, Exploratory Data Analysis, Machine Learning Foundations & Notebooks**  
*Conducted under the NAVTTC (National Vocational and Technical Training Commission) AI Training Initiative & Huawei Certification Program.*

</div>

---

## 📌 Table of Contents
- [📖 About the Program](#-about-the-program)
- [🎯 Learning Objectives](#-learning-objectives)
- [📂 Repository Structure](#-repository-structure)
- [🔬 Modules & Lab Details](#-modules--lab-details)
- [📊 Datasets](#-datasets)
- [⚙️ Setup & Installation (Anaconda / Conda)](#️-setup--installation-anaconda--conda)
- [🚀 How to Run](#-how-to-run)
- [👤 Connect With Me](#-connect-with-me)
- [📜 License](#-license)

---

## 📖 About the Program

This repository contains all practical labs, coursework, exploratory data analysis (EDA), and machine learning preparation exercises developed during the **HCCDA - AI (Huawei Certified Developer Associate - Artificial Intelligence)** program facilitated by **NAVTTC**.

The curriculum is designed to build strong foundations in:
- **Core Python Programming for Data Science**
- **Multidimensional Array Operations with NumPy**
- **Data Wrangling & Analysis with Pandas**
- **Statistical Data Visualization with Matplotlib & Seaborn**
- **Exploratory Data Analysis (EDA) on Real-World Datasets**
- **Huawei Cloud AI Services & Lab Practicals**

---

## 🎯 Learning Objectives

- [x] Master Python fundamentals and data structures for scientific workflows.
- [x] Perform multidimensional array manipulations, slicing, vectorization, and tensor operations in NumPy (2D & 3D arrays).
- [x] Conduct end-to-end Exploratory Data Analysis (EDA) on structured datasets (e.g., Titanic, IMDB Movie Data).
- [x] Design insightful statistical graphs, correlation heatmaps, distribution plots, and relational visualizations using Seaborn and Matplotlib.
- [x] Understand ModelArts and Huawei Cloud AI development paradigms through guided lab exercises.

---

## 📂 Repository Structure

```text
HCCDA_AI_NAVTTC/
├── datasets/
│   ├── IMDB-Movie-Data.csv                             # 1,000 top movies dataset for rating & revenue analysis
│   └── titanic_dataset.xlsx                            # Classic Titanic passenger survival dataset
├── Copy_of_PythonforDS.ipynb                           # Comprehensive Python for Data Science guide & exercises
├── EDA_Titanic_dataset.ipynb                           # Exploratory Data Analysis on Titanic survival demographics
├── HCCDA-AI-Day-2-Lab-1.ipynb                          # HCCDA-AI Day 2 Practical Lab on AI workflows
├── complete_numpy_course_for_beginners_complete.ipynb  # Complete beginner-to-advanced NumPy course
├── data_visualisation.ipynb                            # Data Visualization masterclass (Matplotlib & Seaborn)
├── list_concat.ipynb                                   # Python sequence & list manipulation techniques
├── numpy_2d_array.ipynb                                # 2D Array operations, slicing, masking & broadcasting
├── numpy_3d_array.ipynb                                # 3D Array / Tensor structures and operations
├── one_to_hundred.csv                                  # Sample generated numerical dataset (CSV)
├── one_to_hundred.npy                                  # NumPy binary array file (.npy format)
├── week_2.py                                           # Week 2 introductory Python script
├── requirements.txt                                    # Project dependencies
├── .gitignore                                          # Standard Git ignore rules
└── README.md                                           # Documentation & project guide
```

---

## 🔬 Modules & Lab Details

### 1. 🐍 Python for Data Science (`Copy_of_PythonforDS.ipynb`, `list_concat.ipynb`, `week_2.py`)
- Python data types, strings, lists, tuples, and dictionaries.
- Control flow, list comprehensions, concatenation, and functions.
- Transitioning from pure Python to data science libraries.

### 2. 🔢 Scientific Computing with NumPy (`complete_numpy_course_for_beginners_complete.ipynb`, `numpy_2d_array.ipynb`, `numpy_3d_array.ipynb`)
- **NumPy Fundamentals**: Comprehensive beginner to advanced masterclass covering array creation, math operations, and vectorized computation.
- **2D Arrays**: Matrix representations, row/column slicing, axis-wise aggregations, boolean indexing.
- **3D Arrays**: High-dimensional array manipulation, reshaping, block operations, and tensor foundations.
- **Array Persistence**: Saving and loading binary (`.npy`) and tabular (`.csv`) data (`one_to_hundred.csv`, `one_to_hundred.npy`).

### 3. 🚢 Exploratory Data Analysis (EDA) (`EDA_Titanic_dataset.ipynb`)
- Data cleaning: handling missing values (`Age`, `Cabin`, `Embarked`).
- Demographic analysis: survival rates grouped by `Pclass`, `Sex`, `Age`, and `Fare`.
- Statistical insights into feature correlations.

### 4. 📈 Data Visualization (`data_visualisation.ipynb`)
- **Matplotlib**: Line charts, bar plots, histograms, and scatter plots.
- **Seaborn**: Heatmaps, pair plots, box plots, violin plots, and categorical plots.
- Customizing aesthetics, color palettes, and plot layouts for presentations.

### 5. ☁️ HCCDA - AI Practicals (`HCCDA-AI-Day-2-Lab-1.ipynb`)
- Practical exercises aligned with Huawei Cloud AI Associate certification.
- Hands-on implementation of AI fundamentals and pipeline preparation.

---

## 📊 Datasets

| Dataset | Format | Description |
|---|---|---|
| **Titanic Dataset** | `.xlsx` | Contains passenger demographic info (age, gender, ticket class, fare) and survival outcomes from the Titanic disaster. |
| **IMDB Movie Data** | `.csv` | 1,000 popular movies from 2006 to 2016 detailing title, genre, director, actors, year, runtime, rating, votes, revenue, and Metascore. |

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

Launch Jupyter Notebook inside your activated Conda environment:

```bash
jupyter notebook
```
Or open the project folder in **Visual Studio Code**, select the `hccda_ai (Python 3.12)` kernel in the top-right corner, and run the `.ipynb` notebooks interactively.

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
