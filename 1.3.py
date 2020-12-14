import numpy as np
import matplotlib.pyplot as plt

def xor(a, b):
    if a == b:
        result = 0
    else:
        result = 1
    return result

def autocorr(x):
    x = np.array(x)
    R = np.zeros(25)
    for i in range(0, 25):
        y = np.zeros(len(x))
        y[i:] = x[0:len(x)-i]
        R[i] = np.sum(x*y)
    return R/len(x)


class LSFR5():

    def __init__(self, seed):
        self.seed = seed

    def generate(self):
        last_bit = self.seed[-1]
        new_val = xor(self.seed[2], self.seed[-1])
        for i in range(len(self.seed)-1, 0, -1):
            self.seed[i] = self.seed[i - 1]
        self.seed[0] = new_val

        return last_bit

class LSFR15():

    def __init__(self, seed):
        self.seed = seed

    def generate(self):
        last_bit = self.seed[-1]
        new_val = xor(self.seed[-1], self.seed[-2])
        for i in range(len(self.seed)-1, 0, -1):
            self.seed[i] = self.seed[i - 1]
        self.seed[0] = new_val

        return last_bit


lsfr5 = LSFR5([0, 1, 0, 0, 1])
lsfr15 = LSFR15([0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0])
binary_output_lsfr5 = []
binary_output_lsfr15 = []

for j in range(0, 9999):
    binary_output_lsfr5.append(lsfr5.generate())

R = autocorr(binary_output_lsfr5)
x = range(0, len(R))

plt.title("Autokorelaciona funkcija")
plt.xlabel("Koraci")
plt.plot(x, R, 'bo')
plt.grid(True)
plt.show()

print("p = " +str(np.count_nonzero(binary_output_lsfr5)/len(binary_output_lsfr5)))
