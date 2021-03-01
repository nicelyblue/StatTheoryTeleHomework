import numpy
import random
from matplotlib import pyplot
from scipy import stats

N = 100000
binwidth = 0.01
lam = 1

exponential = (-1 / lam) * numpy.log(numpy.random.uniform(0.0, 1.0, N))
axis = numpy.linspace(0, 10, N)
expected_pdf = stats.expon.pdf(axis)
pyplot.figure(1)
pyplot.title("Procena funkcije gustine verovatnoce")
counts, _, _ = pyplot.hist(exponential, bins=numpy.arange(0, max(exponential) + binwidth, binwidth), density = True)
pyplot.plot(axis, expected_pdf)
pyplot.show()

mean_squared_error = 0
for i in range(0, len(counts)):
    mean_squared_error += counts[i]**2 - expected_pdf[i]**2
mean_squared_error = mean_squared_error/len(counts)
print("Srednja kvadratna greska je: "+str(mean_squared_error))

exponential = numpy.ndarray((20, N))
for i in range(0, 20):
    exponential[i, :] = (-1 / lam) * numpy.log(numpy.random.uniform(0.0, 1.0, N))
exponential = numpy.sum(exponential, axis = 0)

pyplot.figure(2)
pyplot.title("Procena funkcije raspodele")
pyplot.hist(exponential, bins=numpy.arange(0, max(exponential) + binwidth, binwidth), density = True)
pyplot.show()