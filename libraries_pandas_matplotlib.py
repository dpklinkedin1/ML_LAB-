import pandas as pd

s = pd.Series([10,20,30])
print(s)
data = {
    "Name": ["A","B","C"],
    "Marks": [90,80,85]
}

df = pd.DataFrame(data)
print(df)

df["Marks"] = df["Marks"].fillna(df["Marks"].mean())   #Replace missing values (NaN) in Marks column with the average (mean) of that column
df.head()  #Shows first 5 rows of dataset
df.tail() #Shows last 5 rows
df.info()  #Gives complete summary of DataFrame
df.describe() #Gives statistical summary

df["Marks"] #Selects a column
df.iloc[0]  #Select row by index position
df.loc[0] #Select row by label/index name   in short loc is name based and iloc is position based 

df[df["Marks"] > 80]  #

df["Grade"] = ["A","B","A"] #Adds or modifies column
df.dropna()   #Removes rows with missing values
df.fillna(0)    #Replace missing values


#df.loc[row_label, column_label]
df.loc[0]
df.loc[0:2]
df.loc[0, "Marks"]
df.loc[df["Marks"] > 80]


#matplotlib-------------------------------------------
#Function	Purpose
#plt.plot()	line graph
#plt.scatter()	scatter
#plt.bar()	bar chart
#plt.hist()	histogram
#plt.pie()	pie chart
#plt.title()	title
#plt.xlabel()	x label
#plt.ylabel()	y label
#plt.show()	display



import matplotlib.pyplot as plt

x = [1,2,3,4]
y = [10,20,15,25]

plt.plot(x, y)
plt.title("Line Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

plt.show()

#this below line Shows relationship between variables
plt.scatter([1,2,3], [2,4,6])
plt.show()
#bar chart
plt.bar(["A","B","C"], [10,20,15])
plt.show()
#histogram -> hist 
plt.hist([1,2,2,3,3,3])
plt.show()

#pie graph -> pie
plt.pie([30,40,30], labels=["A","B","C"])
plt.show()

#grid explanation 

















📚 plt.grid() in Matplotlib
🧩 1️⃣ DEFINITION

👉 plt.grid() is used to display grid lines on a graph.

👉 Grid lines = horizontal + vertical reference lines
👉 Helps in reading values easily

🧠 2️⃣ WHY WE USE GRID

Without grid ❌
👉 Hard to estimate values

With grid ✅
✔ Easy to read
✔ Better visualization
✔ Professional graphs

🧩 3️⃣ BASIC SYNTAX
plt.grid()

👉 Turns ON grid

🧾 4️⃣ BASIC EXAMPLE
import matplotlib.pyplot as plt

x = [1,2,3,4]
y = [10,20,15,25]

plt.plot(x, y)

plt.title("Graph with Grid")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

plt.grid()   # Add grid

plt.show()
🔍 5️⃣ WHAT HAPPENS INTERNALLY

👉 When you call:

plt.grid()

Matplotlib:

Reads axis values
Draws horizontal lines (Y-axis values)
Draws vertical lines (X-axis values)
Places them behind graph
🧩 6️⃣ GRID TYPES
🔹 Default grid
plt.grid()

✔ Both X and Y lines

🔹 Only X-axis grid
plt.grid(axis='x')
🔹 Only Y-axis grid
plt.grid(axis='y')
🧩 7️⃣ CUSTOMIZATION (IMPORTANT)
🔹 Change line style
plt.grid(linestyle='--')
🔹 Change color
plt.grid(color='gray')
🔹 Change thickness
plt.grid(linewidth=1.5)
🔹 Combine all
plt.grid(color='gray', linestyle='--', linewidth=0.5)
🧩 8️⃣ FULL EXAMPLE (IMPORTANT)
import matplotlib.pyplot as plt

x = [1,2,3,4]
y = [10,20,15,25]

plt.plot(x, y)

plt.title("Styled Grid")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

plt.grid(color='blue', linestyle='--', linewidth=0.5)

plt.show()
🧠 9️⃣ REAL-LIFE UNDERSTANDING

👉 Like graph paper 📈
👉 Helps you:

Track values
Compare points
📌 🔟 ADVANTAGES

✔ Better readability
✔ Easy comparison
✔ Professional look

❌ 1️⃣1️⃣ DISADVANTAGES

❌ Too many grid lines → messy

🎯 FINAL EXAM SUMMARY

👉

plt.grid() → adds grid lines
Can customize axis, color, style
Helps interpret graph
🧠 MEMORY TRICK

👉
“Grid = Guide lines”
