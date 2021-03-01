import numpy
import pandas
from matplotlib import pyplot
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

df = pandas.read_excel("Telecom_data.xlsx")

X = numpy.array(df.iloc[:, 0].values, dtype=numpy.float)
X = X.reshape(-1, 1)
Y = numpy.array(df.iloc[:, 3].values, dtype=numpy.float)

linear_regression = LinearRegression()
linear_regression.fit(X, Y)

Y_pred = linear_regression.predict(X)

print("Srednja kvadratna greska je:", mean_squared_error(Y, Y_pred))

pyplot.scatter(X, Y) 
pyplot.plot([min(X), max(X)], [min(Y_pred), max(Y_pred)], color='red')
pyplot.xlabel('Uzrast')
pyplot.ylabel('Godine radnog staza')
pyplot.show()