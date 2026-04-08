

import pandas as pd
import matplotlib.pyplot as plt

data = {
    "name": ['A','B','C','D','E'],
    "marks":[80,90,78,90,76] 
}

print("==========Pandas section=========")

df = pd.DataFrame(data)
print("DataFrame:",df)

avg = df["marks"].mean()
print("Av
erage marks = ",avg)

max = df["marks"].max()
print("Maximum marks = ",max)

min = df["marks"].min()
print("Minimum marks =",min)

#add new column
df["result"] = ['pass' if m>=75 else "fali" for m in df["marks"]]
print("\nUpdated data:\n",df)


print("=======matplotlib========")

plt.bar(df["name"],df["marks"])
plt.title("student marks{bar graph}")
plt.xlabel("student")
plt.ylabel("marks")
plt.show()


plt.plot(df["name"],df["marks"])
plt.title("marks trend{line graph}")
plt.xlabel("student")
plt.ylabel("marks")
plt.show()




#----------------------------------------------------------------------------------------------------------------------------


mathplotlib_pandas.py
Displaying sci_np_stat_math.py.
