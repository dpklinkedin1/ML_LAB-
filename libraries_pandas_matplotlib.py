import pandas as pd

s = pd.Series([10,20,30])
print(s)
data = {
    "Name": ["A","B","C"],
    "Marks": [90,80,85]
}

df = pd.DataFrame(data)
print(df)

df["Marks"] = df["Marks"].fillna(df["Marks"].mean())
df.head()
df.tail()
df.info()
df.describe()

df["Marks"]
df.iloc[0]
df.loc[0]

df[df["Marks"] > 80]

df["Grade"] = ["A","B","A"]
df.dropna()
df.fillna(0)
