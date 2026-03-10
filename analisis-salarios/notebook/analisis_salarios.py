import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("analisis-salarios/data/Data Science Jobs Salaries.csv")
df.head()
df.info()
df.describe()
df.isnull().sum()
df.groupby("job_title")["salary_in_usd"].mean().sort_values(ascending=False).head(10)
df.groupby("experience_level")["salary_in_usd"].mean()
df.groupby("employment_type")["salary_in_usd"].mean().sort_values(ascending=False).head(10)
df.groupby("remote_ratio")["salary_in_usd"].mean()
df.groupby("experience_level")["salary_in_usd"].mean().plot(kind="bar")
plt.title("Número de salarios por rango de salario en USD")
plt.xlabel("Rango de salario en USD")
plt.ylabel("Número de salarios")
plt.show()
