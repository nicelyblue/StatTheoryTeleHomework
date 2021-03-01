import numpy
import random
from matplotlib import pyplot
from scipy import stats

N = 100000
binwidth = 0.01

x = numpy.random.normal(0.0, 1.0, N)
y = numpy.random.normal(0.0, 1.0, N)

sigma_squared = numpy.var(x)

mean = numpy.sqrt(numpy.pi * sigma_squared /  2)
variance = ((4 - numpy.pi)/2) * sigma_squared

r = numpy.sqrt(numpy.square(x) + numpy.square(y))

f = r/variance * numpy.exp(-numpy.square(r)/(2 * variance))

axis = numpy.linspace(0.0, 5.0, N)

pdf = stats.rayleigh.pdf(axis, 0, numpy.sqrt(variance))

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