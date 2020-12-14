import numpy
import random
from matplotlib import pyplot

def probabilities(seq):

    n_11 = 0
    n_00 = 0
    n_10 = 0
    n_01 = 0
    for i in range(0, len(seq)-1):
        if seq[i] == 1:
            if seq[i+1] == 1:
                n_11 += 1
            else:
                n_10 += 1
        elif seq[i] == 0:
            if seq[i+1] == 1:
                n_01 += 1
            else:
                n_00 += 1
    return n_11/len(seq), n_00/len(seq), n_10/len(seq), n_01/len(seq)

def autocorr(x):

    x = numpy.array(x)
    R = numpy.zeros(25)
    for i in range(0, 25):
        y = numpy.zeros(len(x))
        y[i:] = x[0:len(x)-i]
        R[i] = numpy.sum(x*y)
    return R/len(x)

class Binary_Generator:

    def __init__(self, P_11, P_00):

        self.P_11 = P_11
        self.P_00 = P_00
        self.P_10 = 1 - P_11
        self.P_01 = 1 - P_00

    def generate(self, length, first_bit = numpy.random.randint(0, 2)):

        sequence = []
        for _ in range(0, length):
            current_val = random.uniform(0, 1)
            if first_bit == 0:
                if current_val <= self.P_01:
                    new_bit = 1
                else:
                    new_bit = 0
            elif first_bit == 1:
                if current_val <= self.P_11:
                    new_bit = 1
                else:
                    new_bit = 0
            first_bit = new_bit
            sequence.append(new_bit)
        return sequence

generator = Binary_Generator(0.1, 0.7)

sequence_1 = generator.generate(1000)
sequence_2 = generator.generate(100000)

P_11, P_00, P_10, P_01 = probabilities(sequence_1)
print("Verovatnoce parova za N=1000: ", P_11, P_00, P_10, P_01)

P_11, P_00, P_10, P_01 = probabilities(sequence_2)
print("Verovatnoce parova za N=100000: ", P_11, P_00, P_10, P_01)

P1_1 = numpy.count_nonzero(sequence_1)/len(sequence_1)
P1_2 = numpy.count_nonzero(sequence_2)/len(sequence_2)

P0_1 = 1 - P1_1
P0_2 = 1 - P1_2

print("Verovatnoce jedinice i nule za N=1000: ", P1_1, P0_1)
print("Verovatnoce jedinice i nule za N=100000: ", P1_2, P0_2)

generator_3 = Binary_Generator(0.9, 0.9)
sequence_3 = generator.generate(100000)
R = autocorr(sequence_3)
x = range(0, len(R))
pyplot.title("Autokorelaciona funkcija")
pyplot.xlabel("Koraci")
pyplot.plot(x, R, 'bo')
pyplot.grid(True)
pyplot.show()

generator_4 = Binary_Generator(0.3, 0.3)
sequence_4 = generator.generate(100000)
R = autocorr(sequence_4)
pyplot.title("Autokorelaciona funkcija")
pyplot.xlabel("Koraci")
pyplot.plot(x, R, 'bo')
pyplot.grid(True)
pyplot.show()

generator_5 = Binary_Generator(0.3, 0.3)
sequence_5 = generator.generate(100000)
R = autocorr(sequence_5)
pyplot.title("Autokorelaciona funkcija")
pyplot.xlabel("Koraci")
pyplot.plot(x, R, 'bo')
pyplot.grid(True)
pyplot.show()
