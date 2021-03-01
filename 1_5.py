import numpy
import random
from matplotlib import pyplot
from scipy import stats
import math

N = 100000
binwidth = 0.01
n = 5

x = numpy.random.normal(0.0, 1.0, N)
y = numpy.random.normal(0.0, 1.0, N)
z = numpy.random.normal(0.0, 1.0, N)
p = numpy.random.normal(0.0, 1.0, N)
q = numpy.random.normal(0.0, 1.0, N)

r = numpy.sqrt(numpy.square(x) + numpy.square(y) + numpy.square(z) + numpy.square(p) + numpy.square(q))

f = numpy.power(r, n/2-1)*numpy.exp(-r/2)/(numpy.power(2, n/2) * math.gamma(n/2))

axis = numpy.linspace(0.0, 25.0, N)

pdf = stats.chi2.pdf(axis, 5)

mean_squared_error = 0
for i in range(0, len(f)):
    mean_squared_error += f[i]**2 - pdf[i]**2
mean_squared_error = mean_squared_error/len(f)
print("Srednja kvadratna greska je: "+str(mean_squared_error))

pyplot.figure(1)
pyplot.title("Procena funkcije gustine verovatnoce")
pyplot.stem(r, f)
pyplot.plot(axis, pdf, color = 'red')
pyplot.show()