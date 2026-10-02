# 🤖 Huawei Certified Developer Associate - AI (HCCDA - AI) | NAVTTC

<div align="center">

[![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Anaconda](https://img.shields.io/badge/Conda-Environment-44A833?style=for-the-badge&logo=anaconda&logoColor=white)](https://www.anaconda.com/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?style=for-the-badge&logo=jupyter&logoColor=white)](https://jupyter.org/)
[![Scikit-Learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Data_Analysis-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![NumPy](https://img.shields.io/badge/NumPy-Scientific_Computing-013243?style=for-the-badge&logo=numpy&logoColor=white)](https://numpy.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-11557c?style=for-the-badge&logo=plotly&logoColor=white)](https://matplotlib.org/)
[![Seaborn](https://img.shields.io/badge/Seaborn-Statistical_Plots-388E3C?style=for-the-badge&logo=scipy&logoColor=white)](https://seaborn.pydata.org/)

<br/>

**Hands-on Labs, Exploratory Data Analysis, Machine Learning Algorithms & Applied AI Projects**  
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

This repository contains all practical labs, machine learning algorithms, exploratory data analysis (EDA), data engineering pipelines, and Huawei Cloud AI preparation exercises developed during the **HCCDA - AI (Huawei Certified Developer Associate - Artificial Intelligence)** program facilitated by **NAVTTC**.

The curriculum is designed to build strong expertise in:
- **Core Python Programming for Scientific Computing**
- **Multidimensional Array Operations & Vectorization with NumPy**
- **Data Wrangling & Statistical Analysis with Pandas**
- **Exploratory Data Analysis (EDA) & Data Visualization (Matplotlib / Seaborn)**
- **Supervised Machine Learning (Linear Regression, Classification Models with Scikit-Learn)**
- **Demand Forecasting & Data Preprocessing Pipelines**
- **Huawei Cloud AI Services & ModelArts Integration**

---

## 🎯 Learning Objectives

- [x] Master Python data structures, algorithms, and numerical computing workflows.
- [x] Implement mathematical operations, matrix broadcasting, 2D/3D tensor manipulation, and persistence with NumPy.
- [x] Perform end-to-end Exploratory Data Analysis on real-world datasets (Titanic, Iris, IMDB, Greenleaf Retail).
- [x] Build and evaluate **Supervised Machine Learning Models** (Linear Regression from scratch & Scikit-Learn, Iris Classification).
- [x] Develop modular data preprocessing and splitting pipelines (`train.csv`, `val.csv`, `test.csv`) with automated tests.
- [x] Gain hands-on practice with Huawei Cloud AI tools and lab environments.

---

## 📂 Repository Structure

```text
HCCDA_AI_NAVTTC/
├── 1.Linear Regression Model.ipynb                     # Supervised ML: Linear Regression (scratch & scikit-learn)
├── Copy_of_PythonforDS.ipynb                           # Comprehensive Python for Data Science guide
├── HCCDA-AI-Day-2-Lab-1.ipynb                          # HCCDA-AI Day 2 Practical Lab on AI workflows
├── Iris Dataset/                                       # Iris Flower Classification & EDA
│   ├── iris_EDA_with_Training.ipynb                    # End-to-end EDA and model training pipeline
│   └── iris_model.ipynb                                # Classification model development
├── Titanic Dataset/                                    # Titanic Survival Analysis Collection
│   ├── data/
│   │   ├── train.csv                                   # Titanic training dataset
│   │   └── test.csv                                    # Titanic test dataset
│   ├── EDA_Titanic_dataset.ipynb                       # Comprehensive Titanic EDA notebook
│   ├── Titanic_EDA.ipynb                               # Demographic survival rate breakdown
│   ├── data_visualisation.ipynb                        # Statistical visualization masterclass
│   ├── sir_lec_titanic.ipynb                           # Instructor lecture notes & lab walkthrough
│   └── titanic eda.ipynb                               # Alternative exploratory patterns & insights
├── greenleaf-perishable-demand-forecast/               # Retail Demand Forecasting Project
│   ├── ipynb_folder/
│   │   ├── preprocessing.ipynb                         # Data preprocessing notebook
│   │   ├── test_preprocessing.py                       # Unit testing script for preprocessing logic
│   │   ├── raw_data/sales_data.csv                     # Raw retail sales dataset
│   │   └── split_data/                                 # Stratified split partitions (train, val, test)
│   └── py_folder/
│       ├── preprocessing.py                            # Production-ready data cleaning script
│       └── test_preprocessing.py                       # Test runner
├── datasets/
│   ├── IMDB-Movie-Data.csv                             # 1,000 top movies dataset (rating & revenue)
│   └── titanic_dataset.xlsx                            # Classic Titanic Excel dataset
├── complete_numpy_course_for_beginners_complete.ipynb  # Complete beginner-to-advanced NumPy course
├── numpy_2d_array.ipynb                                # 2D Array operations, slicing & masking
├── numpy_3d_array.ipynb                                # 3D Array / Tensor structures and operations
├── list_concat.ipynb                                   # Python sequence manipulation techniques
├── one_to_hundred.csv                                  # Sample generated numerical dataset (CSV)
├── one_to_hundred.npy                                  # NumPy binary array file (.npy format)
├── week_2.py                                           # Week 2 introductory Python script
├── requirements.txt                                    # Project dependencies
├── .gitignore                                          # Standard Git ignore rules
└── README.md                                           # Documentation & project guide
```

---

## 🔬 Modules & Project Highlights

### 1. 🤖 Supervised Machine Learning (`1.Linear Regression Model.ipynb`)
- **Linear Regression from Scratch**: Cost function ($J(\theta)$), gradient descent intuition, and manual optimization.
- **Scikit-Learn Implementation**: Training `LinearRegression` on continuous features (House Price Prediction).
- **Model Evaluation**: Mean Squared Error (MSE), Root Mean Squared Error (RMSE), and $R^2$ Score.

### 2. 🌸 Iris Flower Classification (`Iris Dataset/`)
- Multiclass classification on the classic Fisher's Iris dataset (`Sepal/Petal Length & Width`).
- Feature distributions, pair plots, model training, accuracy evaluation, and decision boundaries.

### 3. 🚢 Comprehensive Titanic Survival Analysis (`Titanic Dataset/`)
- Data cleaning & imputation: handling missing values (`Age`, `Cabin`, `Embarked`).
- Deep-dive demographics: survival trends across `Pclass`, `Sex`, `Fare`, `SibSp`, and `Parch`.
- Visualizations: Correlation heatmaps, survival histograms, violin and box plots.

### 4. 🛒 Demand Forecasting Pipeline (`greenleaf-perishable-demand-forecast/`)
- Modular data pipeline: parsing raw time-series/retail transaction data (`sales_data.csv`).
- Data partitioning: automated generation of `train.csv`, `val.csv`, and `test.csv`.
- Test-driven validation: automated unit tests via `test_preprocessing.py`.

### 5. 🔢 NumPy & Python Foundations (`complete_numpy_course_for_beginners_complete.ipynb`, etc.)
- In-depth coverage from basic syntax to 2D/3D tensor reshaping, masking, broadcasting, and binary file I/O (`.npy`, `.csv`).

---

## 📊 Datasets

| Dataset | Location | Format | Description |
|---|---|---|---|
| **Titanic Dataset** | `Titanic Dataset/data/` | `.csv`, `.xlsx` | Passenger demographics, ticket class, and survival outcome. |
| **Iris Dataset** | `Iris Dataset/` | In-memory / `.csv` | 150 iris flower instances with 4 morphological features across 3 species. |
| **Sales Demand Data** | `greenleaf-perishable-demand-forecast/` | `.csv` | Retail sales transactions for demand forecasting and inventory modeling. |
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

Launch Jupyter Notebook inside your activated Conda environment:

```bash
jupyter notebook
```
Or open the project folder in **Visual Studio Code**, select the `hccda_ai (Python 3.12)` kernel in the top-right corner, and run any `.ipynb` notebook interactively.

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
