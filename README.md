# 🤖 Huawei Certified Developer Associate - AI (HCCDA - AI) | NAVTTC

<div align="center">

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange.svg?logo=jupyter&logoColor=white)](https://jupyter.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458.svg?logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![NumPy](https://img.shields.io/badge/NumPy-Scientific%20Computing-013243.svg?logo=numpy&logoColor=white)](https://numpy.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-11557c.svg)](https://matplotlib.org/)
[![Seaborn](https://img.shields.io/badge/Seaborn-Statistical%20Plots-blueviolet.svg)](https://seaborn.pydata.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

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
- [⚙️ Setup & Installation](#️-setup--installation)
- [🚀 How to Run](#-how-to-run)
- [👤 Author](#-author)
- [📜 License](#-license)

---

## 📖 About the Program

This repository contains all the practical labs, coursework, exploratory data analysis (EDA), and machine learning preparation exercises developed during the **HCCDA - AI (Huawei Certified Developer Associate - Artificial Intelligence)** program facilitated by **NAVTTC**.

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
│   ├── IMDB-Movie-Data.csv          # 1,000 top movies dataset for rating & revenue analysis
│   └── titanic_dataset.xlsx         # Classic Titanic passenger survival dataset
├── Copy_of_PythonforDS.ipynb        # Comprehensive Python for Data Science guide & exercises
├── EDA_Titanic_dataset.ipynb        # Exploratory Data Analysis on Titanic survival demographics
├── HCCDA-AI-Day-2-Lab-1.ipynb       # HCCDA-AI Day 2 Practical Lab on AI workflows
├── data_visualisation.ipynb         # Data Visualization masterclass (Matplotlib & Seaborn)
├── list_concat.ipynb                # Python sequence & list manipulation techniques
├── numpy_2d_array.ipynb             # 2D Array operations, slicing, masking & broadcasting
├── numpy_3d_array.ipynb             # 3D Array / Tensor structures and operations
├── week_2.py                        # Week 2 introductory Python script
├── requirements.txt                 # Project dependencies
├── .gitignore                       # Standard Git ignore rules
└── README.md                        # Documentation & project guide
```

---

## 🔬 Modules & Lab Details

### 1. 🐍 Python for Data Science (`Copy_of_PythonforDS.ipynb`, `list_concat.ipynb`, `week_2.py`)
- Python data types, strings, lists, tuples, and dictionaries.
- Control flow, list comprehensions, concatenation, and functions.
- Transitioning from pure Python to data science libraries.

### 2. 🔢 Scientific Computing with NumPy (`numpy_2d_array.ipynb`, `numpy_3d_array.ipynb`)
- **2D Arrays**: Matrix representations, row/column slicing, axis-wise aggregations, boolean indexing.
- **3D Arrays**: High-dimensional array manipulation, reshaping, block operations, and tensor foundations.

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

## ⚙️ Setup & Installation

Follow these steps to run the notebooks locally:

### 1. Clone the repository
```bash
git clone https://github.com/Mushtaq0054/HCCDA_AI_NAVTTC.git
cd HCCDA_AI_NAVTTC
```

### 2. Create a virtual environment (Recommended)
```bash
# Windows (PowerShell / Command Prompt)
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install required packages
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

---

## 🚀 How to Run

Launch Jupyter Notebook or Jupyter Lab in your browser:

```bash
jupyter notebook
```
Or open the workspace in **Visual Studio Code** with the **Jupyter Extension** enabled to run the `.ipynb` files interactively.

---

## 👤 Author

- **Mushtaq Ahmad Madni**
- **GitHub**: [@Mushtaq0054](https://github.com/Mushtaq0054)
- **Program**: HCCDA - AI (Huawei Certified Developer Associate - AI) with NAVTTC

---

## 📜 License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT) - feel free to use and adapt the code for educational and learning purposes.
