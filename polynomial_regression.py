import numpy
import pandas
from matplotlib import pyplot
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error

df = pandas.read_excel("Telecom_data.xlsx")

X = numpy.array(df.iloc[:, 0].values, dtype=numpy.float)
X = X.reshape(-1, 1)
Y = numpy.array(df.iloc[:, 3].values, dtype=numpy.float)

mse = []

for deg in range(1, 11):

    polynomial_features = PolynomialFeatures(degree = deg, include_bias = False)
    X_poly = polynomial_features.fit_transform(X)

    linear_regression = LinearRegression()
    linear_regression.fit(X_poly, Y)

    Y_pred = linear_regression.predict(X_poly)

    mse.append(mean_squared_error(Y, Y_pred))

pyplot.plot(range(1, 11), mse)
pyplot.xlabel('Stepen polinoma')
pyplot.ylabel('MSE')
pyplot.show()

polynomial_features = PolynomialFeatures(degree = 4, include_bias = False)
X_poly = polynomial_features.fit_transform(X)

linear_regression = LinearRegression()
linear_regression.fit(X_poly, Y)

Y_pred = linear_regression.predict(X_poly)

print("Srednja kvadratna greska je:", mean_squared_error(Y, Y_pred))

pyplot.scatter(X, Y) 
pyplot.plot(X, Y_pred, color='red')
pyplot.xlabel('Uzrast')
pyplot.ylabel('Godine radnog staza')
pyplot.show()