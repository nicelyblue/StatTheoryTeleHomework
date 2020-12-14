import numpy, random
from matplotlib import pyplot
from scipy.stats import binom
numpy.seterr(divide='ignore')

def square(a_list):

    return [ x**2 for x in a_list ]

def generate_N(N, p):
    
    y = []

    for _ in range(0, N):

        if random.uniform(0, 1)<=p:
            y.append(1)
        else:
            y.append(0)

    return y

def sample_mean(y, L):

    x = []

    for i in range(0, round(len(y)/L), L):
        x.append((numpy.count_nonzero(y[i:i+L]))/L)
    
    mean = numpy.float64(sum(x)/(len(x)))
    return mean

def sample_variance(y, L):

    mean = sample_mean(y, L)
    mean_square = sample_mean(square(y), L)

    variance = mean_square - mean**2
    return numpy.float64(variance)

def absolute_error(x, y):
    x = numpy.float64(x)
    y = numpy.float64(y)
    return abs(x-y) * 100

def relative_error(x, y):
    x = numpy.float64(x)
    y = numpy.float64(y)
    return abs(1 - (y/x)) * 100

N = 10000
p_1 = 0.01
p_2 = numpy.float64(0.0001)
p_3 = 0.7
p_4 = 0.05

y_1 = generate_N(N, p_1)
probability_1 = numpy.float64(numpy.count_nonzero(y_1))/len(y_1)
mean_1 = sample_mean(y_1, 10)
variance_1 = sample_variance(y_1, 10)
print("Array one")
print("Probability of 1:"+str(probability_1))
print("Mean:"+str(mean_1))
print("Variance:"+str(variance_1))
print("Absolute error of probability of 1:"+str(absolute_error(probability_1, p_1)))
print("Absolute error of mean:"+str(absolute_error(mean_1, p_1)))
print("Absolute error of variance:"+str(absolute_error(variance_1, p_1 - p_1**2)))
print("Relative error of probability of 1:"+str(relative_error(probability_1, p_1)))
print("Relative error of mean:"+str(relative_error(mean_1, p_1)))
print("Relative error of variance:"+str(relative_error(variance_1, p_1 - p_1**2)))

y_2 = generate_N(N, p_2)
probability_2 = numpy.float64(numpy.count_nonzero(y_2))/len(y_2)
mean_2 = numpy.float64(sample_mean(y_2, 10))
variance_2 = numpy.float64(sample_variance(y_2, 10))
print("\n\n")
print("Array two")
print("Probability of 1:"+str(probability_2))
print("Mean:"+str(mean_2))
print("Variance:"+str(variance_2))
print("Absolute error of probability of 1:"+str(absolute_error(probability_2, p_1)))
print("Absolute error of mean:"+str(absolute_error(mean_2, p_2)))
print("Absolute error of variance:"+str(absolute_error(variance_2, p_2 - p_2**2)))
print("Relative error of probability of 1:"+str(relative_error(probability_2, p_2)))
print("Relative error of mean:"+str(relative_error(mean_2, p_2)))
print("Relative error of variance:"+str(relative_error(variance_2, p_2 - p_2**2)))

y_3 = generate_N(N, p_3)
y_4 = generate_N(N, p_4)

probability_3 = [numpy.float64(numpy.count_nonzero(y_3))/len(y_3), 1-numpy.float64(numpy.count_nonzero(y_3))/len(y_3)]
probability_4 = [numpy.float64(numpy.count_nonzero(y_4))/len(y_4), 1-numpy.float64(numpy.count_nonzero(y_4))/len(y_4)]

pyplot.title("Distibution")
pyplot.xlabel("Values")
pyplot.stem(probability_3)
pyplot.grid(True)
pyplot.show()

pyplot.title("Distribution")
pyplot.xlabel("Values")
pyplot.stem(probability_4)
pyplot.grid(True)
pyplot.show()

pyplot.title("Probability mass function")
x = numpy.arange(binom.ppf(0.01, N, p_3), binom.ppf(0.99, N, p_3))
pyplot.plot(x, binom.pmf(x, N, p_3), 'bo', ms=8, label='binom pmf')
pyplot.grid(True)
pyplot.show()

pyplot.title("Probability mass function")
x = numpy.arange(binom.ppf(0.01, N, p_4), binom.ppf(0.99, N, p_4))
pyplot.plot(x, binom.pmf(x, N, p_4), 'bo', ms=8, label='binom pmf')
pyplot.grid(True)
pyplot.show()

Nn = numpy.ndarray.tolist(numpy.linspace(1000, 1000000))
Nn = [int(x) for x in Nn]
relative_3 = []
relative_4 = []
tens = [10] * len(Nn)
ones = [1] * len(Nn)

for n in Nn:
    y_3 = generate_N(n, p_3)
    mean_3 = sample_mean(y_3, 10)
    y_4 = generate_N(n, p_4)
    mean_4 = sample_mean(y_4, 10)
    relative_3.append(relative_error(mean_3, p_3))
    relative_4.append(relative_error(mean_4, p_4))

pyplot.title("Relative error")
pyplot.xlabel("N")
pyplot.plot(Nn, relative_3)
pyplot.plot(Nn, tens)
pyplot.plot(Nn, ones)
pyplot.grid(True)
pyplot.show()

pyplot.title("Relative error")
pyplot.xlabel("N")
pyplot.plot(Nn, relative_4)
pyplot.plot(Nn, tens)
pyplot.plot(Nn, ones)
pyplot.grid(True)
pyplot.show()
