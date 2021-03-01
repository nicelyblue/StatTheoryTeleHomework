import numpy
import pandas
import sklearn.preprocessing
from matplotlib import pyplot

df = pandas.read_excel("Telecom_data.xlsx")

X = numpy.array(df.iloc[:, 0].values, dtype=numpy.float)
X = X.reshape(-1, 1)
Y = numpy.array(df.iloc[:, 3].values, dtype=numpy.float)
Y = (Y - numpy.mean(Y)) / numpy.std(Y)

poly_features = sklearn.preprocessing.PolynomialFeatures(degree=4, include_bias=False)
X_poly = poly_features.fit_transform(X)
X_poly = (X_poly - numpy.mean(X_poly, axis = 0)) / numpy.std(X_poly, axis = 0)
X = (X - numpy.mean(X)) / numpy.std(X)

a = 0.1
epochs = 1000

w = numpy.zeros((X_poly.shape[1]))
b = numpy.float(0)
gradient_w = numpy.float(0)
gradient_b = numpy.float(0)

n = numpy.float(len(X))
for _ in range(epochs):
    Y_pred = X_poly.dot(w) + b
    gradient_w = numpy.float((-2/n) * numpy.sum(X_poly.T.dot((Y - Y_pred))))
    gradient_b = numpy.float((-2/n) * numpy.sum((Y - Y_pred)))
    w = w - numpy.float(a) * numpy.float(gradient_w)
    b = b - numpy.float(a) * numpy.float(gradient_b)

Y_pred = X_poly.dot(w) + b

mse = 1/n * sum(numpy.square(Y - Y_pred))
print("Srednja kvadratna greska je:", mse)

pyplot.scatter(X, Y)
axis = numpy.linspace(min(X), max(X), X.shape[0])
pyplot.plot(axis, Y_pred, color='red')
pyplot.xlabel('Uzrast')
pyplot.ylabel('Godine radnog staza')
pyplot.show()


