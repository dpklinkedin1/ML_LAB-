import statistics

data = list(map(float, input("Enter numbers: ").split()))

mean = statistics.mean(data)


median = statistics.median(data)

modes = statistics.multimode(data)
if len(modes) == len(data):
    mode = "No mode"
else:
    mode = modes

variance = statistics.variance(data)


stdev = statistics.stdev(data)

print("Mean =", mean)
print("Median =", median)
print("Mode =", mode)
print("Variance =", variance)
print("Standard Deviation =", stdev)
