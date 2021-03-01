import numpy
import random
from matplotlib import pyplot
from scipy import stats

N = 1000000
random_process = numpy.random.uniform(3.0, 5.0, N)
binwidth = 0.01

axis = numpy.linspace(3.0, 5.0, round(2.0/binwidth))
expected_pdf = stats.uniform.pdf(axis, 3, 2)

pyplot.figure(1)
pyplot.title("Procena funkcije gustine verovatnoce")
counts, _, _ = pyplot.hist(random_process, bins=numpy.arange(min(random_process), max(random_process) + binwidth, binwidth), density=True)
pyplot.plot(axis, expected_pdf)
pyplot.show()

mean_squared_error = 0
for i in range(0, len(counts)):
    mean_squared_error += counts[i]**2 - expected_pdf[i]**2
mean_squared_error = mean_squared_error/len(counts)
print("Srednja kvadratna greska je: "+str(mean_squared_error))

pyplot.figure(2)
pyplot.title("Procena funkcije raspodele")
pyplot.hist(random_process, bins=numpy.arange(min(random_process), max(random_process) + binwidth, binwidth))
pyplot.show()