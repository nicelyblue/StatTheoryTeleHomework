import numpy
import random
from matplotlib import pyplot
from scipy import stats

N = 10000
binwidth = 0.2

X_1 = numpy.random.uniform(-1.0, 1.0, N)
X_2 = numpy.random.uniform(-1.0, 1.0, N)
Y = X_1 + X_2

if numpy.mean(X_1*X_2) == numpy.mean(X_1) * numpy.mean(X_2):
    print("Promenljive nisu korelisane")
else:
    print("Promenljive su korelisane")

print("Srednja vrednost proizvoda:", numpy.mean(X_1*X_2))
print("Proizvod srednje vrednosti:", numpy.mean(X_1) * numpy.mean(X_2))

X = numpy.ndarray((10, N))
for i in range(0, 10):
    X[i, :] = numpy.random.uniform(-1.0, 1.0, N)
Z = numpy.sum(X, axis = 0)

mean_y = numpy.mean(Y)
var_y = numpy.var(Y)
std_y = numpy.std(Y)

mean_z = numpy.mean(Z)
var_z = numpy.var(Z)
std_z = numpy.std(Z)

axis = numpy.linspace(-10, 10, N)
expected_pdf_y = stats.norm.pdf(axis, mean_y, std_y)
expected_pdf_z = stats.norm.pdf(axis, mean_z, std_z)

pyplot.figure(1)
pyplot.title("Procena funkcije gustine verovatnoce")
counts, _, _ = pyplot.hist(Y, bins=numpy.arange(-2, 2 + binwidth, binwidth), density = True)
pyplot.plot(axis, expected_pdf_y)
pyplot.show()

mean_squared_error = 0
for i in range(0, len(counts)):
    mean_squared_error += counts[i]**2 - expected_pdf_y[i]**2
mean_squared_error = mean_squared_error/len(counts)
print("Srednja kvadratna greska je: "+str(mean_squared_error))

binwidth = 0.3

pyplot.figure(2)
pyplot.title("Procena funkcije gustine verovatnoce")
count, _, _ = pyplot.hist(Z, bins=numpy.arange(-10, 10 + binwidth, binwidth), density = True)
pyplot.plot(axis, expected_pdf_z)
pyplot.show()

mean_squared_error = 0
for i in range(0, len(count)):
    mean_squared_error += count[i]**2 - expected_pdf_z[i]**2
mean_squared_error = mean_squared_error/len(count)
print("Srednja kvadratna greska je: "+str(mean_squared_error))
