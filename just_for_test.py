# 1️⃣ Libraries import karna (Data handling, Visualization, Model training)
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.linear_model import LinearRegression          # Linear Regression model
from sklearn.model_selection import train_test_split       # Train-test split
from sklearn.metrics import mean_squared_error, r2_score   # Evaluation metrics

# 2️⃣ Dataset load karna
df = sns.load_dataset("iris")   # seaborn ke andar builtin iris dataset hota hai
print(df.head())                # pehle 5 rows dekhna

# 3️⃣ Exploratory Dataa Analysis (EDA)
print(df.info())                # dataset structure (rows, columns, datatypes)
print(df.describe())            # numerical columns ka summary (mean, std, min, max)

sns.scatterplot(data=df, x="sepal_length", y="sepal_width", hue="species")  
plt.title("Sepal Length vs Sepal Width (with Species)")
plt.show()

# 4️⃣ Feature Selection (X aur y choose karna)
# Ham sirf ek feature use karenge (sepal_length) aur ek target (sepal_width)
X = df[['sepal_length']]   # independent variable (input)
y = df['sepal_width']      # dependent variable (output)

# 5️⃣ Train-Test Split
# Dataset ko training aur testing me divide karna (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 6️⃣ Model Initialization
model = LinearRegression()   # Linear Regression ka object banaya

# 7️⃣ Model Training (Fit karna training data par)
model.fit(X_train, y_train)

# 8️⃣ Model Parameters nikalna
print("Intercept (b):", model.intercept_)      # b in y = mx + b
print("Coefficient (m):", model.coef_)         # slope m

# Equation of line
print(f"Equation of line: y = {model.coef_[0]:.4f} * x + {model.intercept_:.4f}")

# 9️⃣ Prediction karna (Testing data par)
y_pred = model.predict(X_test)   # X_test par prediction generate karna

# 1️⃣0️⃣ Evaluation (Model ki accuracy check karna)
mse = mean_squared_error(y_test, y_pred)   # Mean Squared Error
r2 = r2_score(y_test, y_pred)              # R² score
rmse = np.sqrt(mse)                        # Root Mean Squared Error

print("Mean Squared Error (MSE):", mse)
print("Root Mean Squared Error (RMSE):", rmse)
print("R² Score:", r2)

# 1️⃣1️⃣ Visualization (Actual vs Predicted)
plt.figure(figsize=(8,6))
plt.scatter(X_test, y_test, color='blue', label='Actual Data')      # original points
plt.scatter(X_test, y_pred, color='red', label='Predicted Points')  # predicted points
plt.plot(X_test, y_pred, color='green', linewidth=2, label='Regression Line')  
plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")
plt.title("Linear Regression: Sepal Length vs Sepal Width")
plt.legend()
plt.show()
