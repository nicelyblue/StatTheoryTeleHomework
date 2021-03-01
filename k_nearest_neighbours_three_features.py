import numpy
import pandas
from matplotlib import pyplot
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.model_selection import validation_curve

df = pandas.read_excel("Telecom_data.xlsx")

X = numpy.array(df.iloc[:, [0, 2, 3]].values, dtype=numpy.float)
Y = numpy.array(df.iloc[:, 4].values, dtype=numpy.float)

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, train_size = 0.66)

accuracy = []
k_range = range(1, 100, 2)

model = KNeighborsClassifier()
model.fit(X_train, Y_train)

train_scores, test_scores = validation_curve(
                model, X_train, Y_train,
                param_name='n_neighbors',
                param_range=k_range,
                cv=5,
                scoring='accuracy')


train_scores_mean = numpy.mean(train_scores, axis=1)
train_scores_std = numpy.std(train_scores, axis=1)
test_scores_mean = numpy.mean(test_scores, axis=1)
test_scores_std = numpy.std(test_scores, axis=1)

pyplot.title("Validaciona kriva")
pyplot.xlabel("Broj suseda")
pyplot.ylabel("Skor")
lw = 2
pyplot.plot(k_range, train_scores_mean, label="Trening",
            color="darkorange")
pyplot.fill_between(k_range, train_scores_mean - train_scores_std,
                 train_scores_mean + train_scores_std, alpha=0.2,
                 color="darkorange")
pyplot.plot(k_range, test_scores_mean, label="Validacija",
             color="navy")
pyplot.fill_between(k_range, test_scores_mean - test_scores_std,
                 test_scores_mean + test_scores_std, alpha=0.2,
                 color="navy")
pyplot.legend(loc="best")
pyplot.show()

k_nearest_neighbors = KNeighborsClassifier(n_neighbors = 20)
k_nearest_neighbors.fit(X_train, Y_train)
print(k_nearest_neighbors.score(X_test, Y_test))

k_nearest_neighbors = KNeighborsClassifier(n_neighbors = round(numpy.sqrt(X.shape[0])))
k_nearest_neighbors.fit(X_train, Y_train)
print(k_nearest_neighbors.score(X_test, Y_test))