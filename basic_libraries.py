
import math
import numpy as np 
from scipy import stats
import statistics
data = list(map(float, input("Enter number:").split()))
#---------------statistics-------------------------#
mean = statistics.mean(data)
m = statistics.multimode(data)
if len(m)>len(data):
    mode = "no mode"
else:
    mode = m
median = statistics.median(data)
stdev = statistics.stdev(data)
variance = statistics.variance(data)


print("mean = ",mean)
print("mode= ",mode)
print("median = ",median)
print("variance",variance)
print("standard_dev =",stdev)
#--------------------math-----------------
print("Square root of mean:",math.sqrt(mean))
print("Pow of mean(mean^2)",math.pow(mean,2))
if mean>0:
    print("Log value of mean:",math.log(mean))
else:
    print("Log is not defined")
    

#-----------numpy-------------------

arr = np.array(data)
print("mean = ",np.mean(arr))
print("sum =",np.sum(arr))
print("max = ",np.max(arr))
print("min = ",np.min(arr))
print("25th percentile = ",np.percentile(data,25))
print("75Th percentile = ",np.percentile(data,75))


#------------------scipy-----------

#basic description
result = stats.describe(data)
print("Count = ",result.nobs)
print("Mean = ",result.mean)
print("min,max = ",result.minmax)
print("variance = ",result.variance)

print("kurtosis=",result.kurtosis) #peak 
print("symmetry=",stats.skew(data)) #symmetry

print("Normalizartion: Z-score :",stats.zscore(data))










#-------------------------------------------------------------------
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




#---------------------------------------------------
      
