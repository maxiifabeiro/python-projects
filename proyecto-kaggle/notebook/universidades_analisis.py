import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("proyecto-kaggle/data/top_100_universities_dataset.csv")
df.head()
df.info()
df.describe()
df.isnull().sum()
df["Location"].value_counts().head(10)
df["Established_Year"].value_counts().sort_index()
df["Established_Year"].value_counts().sort_index().plot()
plt.title("Número de universidades por año de fundación")
plt.xlabel("Año de fundación")
plt.ylabel("Número de universidades")
plt.show()
