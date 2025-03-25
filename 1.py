import numpy
from scipy import stats
speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
x = numpy.mean(speed)
print("mean value is:",x)
y = numpy.median(speed)
print("the median value is:",y)
z = stats.mode(speed)
print("the mode value is:",z)
v=numpy.var(speed)
print("the variance of given data set is :",v)
s=numpy.std(speed)
print("standard deviation is :",s)
