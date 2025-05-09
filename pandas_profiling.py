# -*- coding: utf-8 -*-
"""Pandas Profiling.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1VD1TiRYbaBFiVquBm6Fdldg7lWRx2YKy

# **Pandas Profiling to automate Exploratory Data Analysis **

**Pandas Profiling** enables fast and automated exploratory data analysis (EDA) with just a few lines of code. It's an excellent starting point for data exploration and the AutoML workflow. The tool generates a comprehensive, easy-to-read report directly from a pandas DataFrame, summarizing variable types, distributions, correlations, ranges, and missing values. While it's not a substitute for the depth of analysis a skilled data scientist can provide, it's a valuable resource for quickly understanding the structure and quality of a dataset.
https://www.youtube.com/@Bioinformatics_Made_Easy
"""

# eda_report.ipynb

# Step 1: Install required package if not already installed
!pip install ydata-profiling

# Step 2: Import libraries
import pandas as pd
import seaborn as sns
from pandas_profiling import ProfileReport

# Step 3: Load dataset (Titanic)
df = sns.load_dataset('titanic')

# Step 4: Generate and display profile report
profile = ProfileReport(df, title='Titanic Dataset EDA Report', explorative=True)
profile.to_file("titanic_eda_report.html")
profile.to_notebook_iframe()

profile = ProfileReport(df, title="Profiling Report")