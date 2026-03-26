import math

x = 16

print("Square root:", math.sqrt(x))
print("Power:", math.pow(2,3))
print("Log:", math.log(10))
print("Sin:", math.sin(0))
print("Ceil:", math.ceil(4.2))
print("Floor:", math.floor(4.8))




import statistics

data = [1,2,2,3,4]

print("Mean:", statistics.mean(data))
print("Median:", statistics.median(data))
print("Mode:", statistics.mode(data))
print("Variance:", statistics.variance(data))
print("Standard Deviation:", statistics.stdev(data))


from scipy import stats

data = [1,2,2,3,4]

print("Mean:", stats.tmean(data))
print("Variance:", stats.tvar(data))
print("Mode:", stats.mode(data))
print("normalization:", stats.norm(data))



from scipy import linalg
import numpy as np

A = np.array([[1,2],[3,4]])

print("Inverse:", linalg.inv(A))
print("Determinant:", linalg.det(A))



import numpy as np

data = np.array([10,20,20,30])

print("Mean:", np.mean(data))
print("Median:", np.median(data))
print("Std Dev:", np.std(data))

data = data * 2
print("After multiplication:", data
a = np.array([1,2,3])
b = 2

print(a + b) #[3 4 5]
arr = np.array([[1,2],[3,4]])

print(arr.shape) #(2,2)
      
