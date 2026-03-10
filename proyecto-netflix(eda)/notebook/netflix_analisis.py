import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("proyecto-netflix(eda)/data/netflix_titles.csv")

df.head()

df.info()

df.describe()

df.isnull().sum()

df["type"].value_counts()

df["country"].value_counts().head(10)

df["release_year"].value_counts().sort_index()

df["release_year"].value_counts().sort_index().plot()

plt.title("Número de títulos por año de lanzamiento")
plt.xlabel("Año de lanzamiento")
plt.ylabel("Número de títulos")
plt.show()
