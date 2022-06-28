import pandas as pd
col_names = ['pregnant', 'glucose', 'bp', 'skin', 'insulin', 'bmi', 'pedigree', 'age', 'label']
pima = pd.read_csv("./data/pima_indians_diabetes.csv", header = None, names = col_names)

print(pima.head())