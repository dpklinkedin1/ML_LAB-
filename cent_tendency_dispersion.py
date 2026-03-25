import math
from collections import Counter

# Step 1: Input
data = list(map(float, input("Enter numbers: ").split()))

n = len(data)

# Mean
mean = sum(data) / n

# Median
sorted_data = sorted(data)
if n % 2 == 0:
    median = (sorted_data[n//2 - 1] + sorted_data[n//2]) / 2
else:
    median = sorted_data[n//2]

# Mode
count = Counter(data)
max_freq = max(count.values())
mode = [k for k, v in count.items() if v == max_freq]

# Variance
variance = sum((x - mean) ** 2 for x in data) / n

# Standard Deviation
std_dev = math.sqrt(variance)

# Output
print("Mean =", mean)
print("Median =", median)
print("Mode =", mode)
print("Variance =", variance)
print("Standard Deviation =", std_dev)
