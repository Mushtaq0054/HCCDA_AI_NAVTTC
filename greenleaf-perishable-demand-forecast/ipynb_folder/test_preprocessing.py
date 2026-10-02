import os
import pandas as pd
import pytest


def test_imputation_no_missing_values():
  # Teeno files load karein
  train_path = os.path.join("split_data", "train.csv")
  val_path = os.path.join("split_data", "val.csv")
  test_path = os.path.join("split_data", "test.csv")

  # Check karein ke teeno files exist karti hain
  assert os.path.exists(train_path), "train.csv file mojood nahi hai"
  assert os.path.exists(val_path), "val.csv file mojood nahi hai"
  assert os.path.exists(test_path), "test.csv file mojood nahi hai"

  train_df = pd.read_csv(train_path)
  val_df = pd.read_csv(val_path)
  test_df = pd.read_csv(test_path)

  # Check columns jisme missing values the
  cols_to_check = ["unit_price", "inventory_level", "promotion"]

  # Assert karein ke kisi mein koi null value na bachi ho
  assert (
      train_df[cols_to_check].isnull().sum().sum() == 0
  ), "Train data mein abhi bhi missing values hain!"
  assert (
      val_df[cols_to_check].isnull().sum().sum() == 0
  ), "Validation data mein abhi bhi missing values hain!"
  assert (
      test_df[cols_to_check].isnull().sum().sum() == 0
  ), "Test data mein abhi bhi missing values hain!"