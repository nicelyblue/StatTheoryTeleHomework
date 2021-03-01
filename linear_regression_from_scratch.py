import numpy
import pandas
from matplotlib import pyplot

df = pandas.read_excel("Telecom_data.xlsx")

X = numpy.array(df.iloc[:, 0].values, dtype=numpy.float)
X = (X - numpy.mean(X)) / numpy.std(X)
Y = numpy.array(df.iloc[:, 3].values, dtype=numpy.float)
Y = (Y - numpy.mean(Y)) / numpy.std(Y)

a = 0.1
epochs = 1000

w = numpy.float(0)

b = numpy.float(0)
gradient_w = numpy.float(0)
gradient_b = numpy.float(0)

n = numpy.float(len(X))
for _ in range(epochs):
    Y_pred = X * w + b
    gradient_w = numpy.float((-2/n) * numpy.sum(X * (Y - Y_pred)))
    gradient_b = numpy.float((-2/n) * numpy.sum((Y - Y_pred)))
    w = w - numpy.float(a) * numpy.float(gradient_w)
    b = b - numpy.float(a) * numpy.float(gradient_b)

Y_pred = X * w + b

mse = 1/n * sum(numpy.square(Y - Y_pred))

print("Srednja kvadratna greska je:", mse)

pyplot.scatter(X, Y) 
pyplot.plot([min(X), max(X)], [min(Y_pred), max(Y_pred)], color='red')
pyplot.xlabel('Uzrast')
pyplot.ylabel('Godine radnog staza')
pyplot.show()

