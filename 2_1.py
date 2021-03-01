import numpy
import random
from matplotlib import pyplot
from scipy import stats, special

def QPSK_tx(x):
    r = NRZ(x)
    p, q = splitter(r)
    QPSK = (p + 1j*q) / numpy.sqrt(2)
    return QPSK

def add_noise(x, SNR):
    sigma = numpy.sqrt(1/4)*numpy.power(10, -SNR/20)
    noise = (numpy.random.normal(0, 1, len(x)) + 1j*numpy.random.normal(0, 1, len(x)))*sigma
    noisy_signal = x + noise
    return noisy_signal

def QPSK_rx(QPSK, offset = 0, region_shift = 0):
    offset = numpy.cos(offset) + 1j*numpy.sin(offset)
    p = numpy.zeros(len(QPSK))
    q = numpy.zeros(len(QPSK))
    QPSK = QPSK*offset
    angles = numpy.angle(QPSK, deg = True)
    col = []
    for i in range(0, len(angles)):
        if angles[i] >= 0.0 + region_shift and angles[i] <= 90.0 - region_shift:
            q[i] = 1
            p[i] = 1
            col.append('m')
        elif angles[i] >= 90.0 - region_shift and angles[i] <= 180.0 + region_shift:
            q[i] = 1
            p[i] = 0
            col.append('g')
        elif angles[i] >= 180.0 + region_shift and angles[i] <= 270.0 - region_shift:
            q[i] = 0
            p[i] = 0
            col.append('r')
        elif angles[i] >= 270 - region_shift and angles[i] <= 360 + region_shift:
            q[i] = 0
            p[i] = 1
            col.append('b')
        elif angles[i] <= 0.0 + region_shift and angles[i] >= -90.0 - region_shift:
            q[i] = 0
            p[i] = 1
            col.append('b')
        elif angles[i] <= -90.0 - region_shift and angles[i] >= -180.0 + region_shift:
            q[i] = 0
            p[i] = 0
            col.append('r')
        elif angles[i] <= -180.0 + region_shift and angles[i] >= -270.0 - region_shift:
            q[i] = 1
            p[i] = 0
            col.append('g')
        elif angles[i] <= -270.0 - region_shift and angles[i] >= -360.0 + region_shift:
            q[i] = 1
            p[i] = 1
            col.append('m')
    sequence = assemble(p, q)
    return sequence, col

def assemble(p, q):
    sequence = []
    j = 0
    k = 0
    for i in range(0, 2*len(p)):
        if (i%2 == 0):
            sequence.append(p[j])
            j += 1
        else:
            sequence.append(q[k])
            k += 1
    sequence = numpy.array(sequence)
    return sequence

def splitter(x):
    p = []
    q = []
    for i in range(0, len(x)):
        if (i%2 == 0):
            p.append(x[i])
        else:
            q.append(x[i])
    p = numpy.array(p)
    q = numpy.array(q)
    return p, q

def NRZ(x):
    r = numpy.array(x)
    for i in range(0, len(x)):
        if (x[i] == 0):
            r[i] = -1
        else:
            r[i] = x[i]
    return r

def bit_error_rate(x, y):
    error = 0
    for i in range(0, len(x)):
        if not int(x[i]) == int(y[i]):
            error+=1
    error_rate = numpy.float64(error/len(x))
    return error_rate

def constellation_diagram(QPSK_tx_, QPSK_rx_):
    real_tx = numpy.real(QPSK_tx_)
    im_tx = numpy.imag(QPSK_tx_)
    real = numpy.real(QPSK_rx_)
    im = numpy.imag(QPSK_rx_)
    pyplot.title("Konstelacioni dijagram")
    pyplot.scatter(real, im, c = col)
    pyplot.scatter(real_tx, im_tx, marker='x', color = 'black', s = 100)
    pyplot.show()

def plot_error_rates(estimated, theoretical):
    axis = range(0, 11)
    pyplot.title("BER")
    pyplot.plot(axis, estimated, label = 'Procenjena')
    pyplot.plot(axis, theoretical, label = 'Teorijska')
    pyplot.yscale('log')
    pyplot.legend()
    pyplot.show()

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

N = 5000

offset_1 = numpy.pi/12
offset_2 = numpy.random.uniform(0.0, numpy.pi/6, round(N/2))

generator_1 = Binary_Generator(0.5, 0.5)
generator_2 = Binary_Generator(0.1, 0.1)

sequence_1 = generator_1.generate(N)
sequence_1 = numpy.array(sequence_1)
tx_sequence_1 = numpy.copy(sequence_1)

sequence_2 = generator_2.generate(N)
sequence_2 = numpy.array(sequence_2)
tx_sequence_2 = numpy.copy(sequence_2)


estimated_bit_error_1 = []
theoretical_bit_error_1 = []
for i in range(0, 11):
    QPSK_1 = QPSK_tx(tx_sequence_1)
    QPSK_rx_1 = add_noise(QPSK_1, i)
    rx_sequence, col = QPSK_rx(QPSK_rx_1)
    if i == 2 or i == 8:
        constellation_diagram(QPSK_1, QPSK_rx_1)
    estimated_bit_error_1.append(bit_error_rate(tx_sequence_1, rx_sequence))
    theoretical_bit_error_1.append(0.5*special.erfc(numpy.sqrt(numpy.power(10, i/10))))

plot_error_rates(estimated_bit_error_1, theoretical_bit_error_1)

estimated_bit_error_2 = []
theoretical_bit_error_2 = []
for i in range(0, 11):
    QPSK_2 = QPSK_tx(tx_sequence_2)
    QPSK_rx_2 = add_noise(QPSK_2, i)
    rx_sequence, col = QPSK_rx(QPSK_rx_2)
    if i == 2 or i == 8:
        constellation_diagram(QPSK_2, QPSK_rx_2)
    estimated_bit_error_2.append(bit_error_rate(tx_sequence_2, rx_sequence))
    theoretical_bit_error_2.append(0.5*special.erfc(numpy.sqrt(numpy.power(10, i/10))))

plot_error_rates(estimated_bit_error_2, theoretical_bit_error_2)

estimated_bit_error_2 = []
theoretical_bit_error_2 = []
for i in range(0, 11):
    QPSK_2 = QPSK_tx(tx_sequence_2)
    QPSK_rx_2 = add_noise(QPSK_2, i)
    rx_sequence, col = QPSK_rx(QPSK_rx_2, region_shift=15)
    if i == 2 or i == 8:
        constellation_diagram(QPSK_2, QPSK_rx_2)
    estimated_bit_error_2.append(bit_error_rate(tx_sequence_2, rx_sequence))
    theoretical_bit_error_2.append(0.5*special.erfc(numpy.sqrt(numpy.power(10, i/10))))

plot_error_rates(estimated_bit_error_2, theoretical_bit_error_2)

estimated_bit_error_2 = []
theoretical_bit_error_2 = []
for i in range(0, 11):
    QPSK_2 = QPSK_tx(tx_sequence_2)
    QPSK_rx_2 = add_noise(QPSK_2, i)
    rx_sequence, col = QPSK_rx(QPSK_rx_2, offset_1)
    if i == 2 or i == 8:
        constellation_diagram(QPSK_2, QPSK_rx_2)
    estimated_bit_error_2.append(bit_error_rate(tx_sequence_2, rx_sequence))
    theoretical_bit_error_2.append(0.5*special.erfc(numpy.sqrt(numpy.power(10, i/10))))

plot_error_rates(estimated_bit_error_2, theoretical_bit_error_2)

estimated_bit_error_2 = []
theoretical_bit_error_2 = []
for i in range(0, 11):
    QPSK_2 = QPSK_tx(tx_sequence_2)
    QPSK_rx_2 = add_noise(QPSK_2, i)
    rx_sequence, col = QPSK_rx(QPSK_rx_2, offset_2)
    if i == 2 or i == 8:
        constellation_diagram(QPSK_2, QPSK_rx_2)
    estimated_bit_error_2.append(bit_error_rate(tx_sequence_2, rx_sequence))
    theoretical_bit_error_2.append(0.5*special.erfc(numpy.sqrt(numpy.power(10, i/10))))

plot_error_rates(estimated_bit_error_2, theoretical_bit_error_2)