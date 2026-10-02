import logging
import os
import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline

# 1. Setup Logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


def load_data(file_path: str) -> pd.DataFrame:
  logging.info(f"Loading raw data from: {file_path}")
  df = pd.read_csv(file_path)
  # Date ke hisaab se sort karna time-series data ke liye
  df = df.sort_values("date").reset_index(drop=True)
  return df


def split_data(df: pd.DataFrame):
  logging.info("Splitting dataset chronologically (70% Train, 20% Val, 10% Test)")
  n = len(df)
  train_df = df.iloc[: int(0.7 * n)].copy()
  val_df = df.iloc[int(0.7 * n) : int(0.9 * n)].copy()
  test_df = df.iloc[int(0.9 * n) :].copy()
  return train_df, val_df, test_df


def build_imputation_pipeline():
  num_pipeline = Pipeline([("imputer", SimpleImputer(strategy="median"))])
  cat_pipeline = Pipeline([("imputer", SimpleImputer(strategy="most_frequent"))])
  return num_pipeline, cat_pipeline


def impute_data(train_df, val_df, test_df):
  logging.info("Fitting imputation pipeline on Training set only...")
  num_cols = ["unit_price", "inventory_level"]
  cat_cols = ["promotion"]

  num_pipeline, cat_pipeline = build_imputation_pipeline()

  # Fit statistics ONLY on training set
  num_pipeline.fit(train_df[num_cols])
  cat_pipeline.fit(train_df[cat_cols])

  # Transform all splits
  logging.info("Transforming Train, Validation, and Test sets...")
  for split in [train_df, val_df, test_df]:
    split[num_cols] = num_pipeline.transform(split[num_cols])
    split[cat_cols] = cat_pipeline.transform(split[cat_cols])

  return train_df, val_df, test_df


def save_processed_data(train_df, val_df, test_df, output_dir="split_data"):
  os.makedirs(output_dir, exist_ok=True)
  train_path = os.path.join(output_dir, "train.csv")
  val_path = os.path.join(output_dir, "val.csv")
  test_path = os.path.join(output_dir, "test.csv")

  train_df.to_csv(train_path, index=False)
  val_df.to_csv(val_path, index=False)
  test_df.to_csv(test_path, index=False)
  logging.info(f"Cleaned datasets successfully saved to '{output_dir}/'")


def run_pipeline():
  input_path = "raw_data/sales_data.csv"
  df = load_data(input_path)
  train_df, val_df, test_df = split_data(df)
  train_clean, val_clean, test_clean = impute_data(train_df, val_df, test_df)
  save_processed_data(train_clean, val_clean, test_clean)
  logging.info("Pipeline executed successfully without errors.")


if __name__ == "__main__":
  run_pipeline()