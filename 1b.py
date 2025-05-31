import statistics 
data = [1, 2, 3, 4, 5, 5, 6, 7, 8, 9] 
# Mean 
mean = statistics.mean(data) 
print("Mean value is:", mean) 
# Median 
median = statistics.median(data) 
print("Median value is :", median) 
# Mode 
mode = statistics.mode(data) 
print("Mode value is:", mode) 
# Variance 
variance = statistics.variance(data) 
print("Variance value is:", variance) 
# Standard Deviation 
std_deviation = statistics.stdev(data) 
print("Standard Deviation of given data set is:", std_deviation)
