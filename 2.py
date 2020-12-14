from matplotlib import pyplot
import numpy
import statistics

def split(word): 

    return [char for char in word]  

def autocorr(x):

    x = numpy.array(x)
    R = numpy.zeros(25)
    for i in range(0, 25):
        y = numpy.zeros(len(x))
        y[i:] = x[0:len(x)-i]
        R[i] = numpy.sum(x*y)
    return R/len(x)

def autocovariance(x):
    x = numpy.array(x)
    mean_x = statistics.mean(x)
    C = numpy.zeros(25)
    for k in range(0, 25):
        s = 0
        for n in range(0, len(x)-k):
            product = (x[n] - mean_x)*(x[n+k] - mean_x)
            s += product
        C[k] = s
    return C/(len(x)*C[0])

def square(a_list):

    return [ x**2 for x in a_list ]

def find_middle(input_list):
    input_list = sorted(input_list)
    middle = float(len(input_list))/2

    if middle % 2 != 0:
        return input_list[int(middle - .5)]
    else:
        return (input_list[int(middle)] + input_list[int(middle-1)])/2

def sample_mean(y, L):

    x = []

    for i in range(0, round(len(y)/L), L):
        x.append(sum(y[i:i+L]))
    
    mean = sum(x)/(L*len(x))
    return mean

def sample_variance(y, L):

    mean = sample_mean(y, L)
    mean_square = sample_mean(square(y), L)

    variance = mean_square - mean**2
    return variance

def sample_median(y, L):

    x = []

    for i in range(0, round(len(y)/L)):
        x.append(sum(y[i:i+L]))

    middle = find_middle(x)
    median = middle/L
    return median

def sample_mode(y, L):

    x = []

    for i in range(0, round(len(y)/L)):
        x.append(statistics.mode(y[i:i+L]))

    mode = round(sum(x)/len(x))
    return mode

def median(data, probabilities):

    sum_1 = 0
    sum_2 = 0
    median_1 = 0
    median_2 = 0

    for i in range(0, len(data)):
        sum_1 += probabilities[i]
        if sum_1 >= 0.5:
            median_1 = data[i]

    for i in range(len(data)-1, -1, -1):
        sum_2 += probabilities[i]
        if sum_2 >= 0.5:
            median_2 = data[i]

    if median_1 == median_2:
        median = median_1
    else:
        median = (median_1 + median_2)/2

    return median

def encode(message): 
    encoded_message = "" 
    i = 0
   
    while (i <= len(message)-1): 
        count = 1
        ch = message[i] 
        j = i 
        while (j < len(message)-1): 
            if (message[j] == message[j+1]): 
                count = count+1
                j = j+1
            else: 
                break
        encoded_message=encoded_message+str(count)+ch 
        i = j+1
    return encoded_message 

text = "In most cases, you will see a unimodal distribution, such as the familiar bell shape of the normal, the flat shape of the uniform, or the descending or ascending shape of an exponential or Pareto distribution. You might also see complex distributions, such as multiple peaks that don\'t disappear with different numbers of bins, referred to as a bimodal distribution, or multiple peaks, referred to as a multimodal distribution. You might also see a large spike in density for a given value or small range of values indicating outliers, often occurring on the tail of a distribution far away from the rest of the density."

binary_text = ''.join(format(ord(i), 'b') for i in text)
binary_text = split(binary_text)
binary_text = [int(i) for i in binary_text]
binary_text_length = len(binary_text)

compressed_text = encode(text)
binary_compressed_text = ''.join(format(ord(i), 'b') for i in compressed_text)
binary_compressed_text = split(binary_compressed_text)
binary_compressed_text = [int(i) for i in binary_compressed_text]
binary_compressed_text_length = len(binary_compressed_text)

ascii_text = [ord(i) for i in text]
ascii_text_length = len(ascii_text)

# ASCII
print("ASCII")

ascii_range = range(0, 128)
ascii_range_squares = [x**2 for x in ascii_range]

histogram, _, _ = pyplot.hist(ascii_text, bins=128, range = (0, 128))
pyplot.show()

probabilities = histogram / ascii_text_length

mean = sum(probabilities * ascii_range)
print('Srednja vrednost je: '+str(mean))

samp_mean = sample_mean(ascii_text, 10)
print('Srednja vrednost (usrednjavanje po vremenu) je: '+str(samp_mean))

mean_squares = sum(probabilities * ascii_range_squares)
print('Srednja kvadratna vrednost je: '+str(mean_squares))

samp_mean_squares = sample_mean(square(ascii_text), 10)
print('Srednja kvadratna vrednost (usrednjavanje po vremenu) je: '+str(samp_mean_squares))

variance = mean_squares - mean**2
print('Varijansa je: '+str(variance))

samp_variance = sample_variance(ascii_text, 10)
print('Varijansa (usrednjavanje po vremenu) je: '+str(samp_variance))

med = median(ascii_range, probabilities)
print('Medijana je: '+str(med))

samp_median = sample_median(ascii_text, 10)
print('Medijana (usrednjavanje po vremenu) je: '+str(samp_median))

max_index = numpy.argmax(probabilities)
modus = ascii_range[max_index]
print('Modus je: '+str(modus))

samp_mode = sample_mode(ascii_text, 10)
print('Modus (usrednjavanje po vremenu) je: '+str(samp_mode))

print("\n\n\n")

autocorrelation = autocorr(ascii_text)
axis = range(0, len(autocorrelation))
pyplot.title("Autokorelaciona funkcija")
pyplot.xlabel("Koraci")
pyplot.plot(axis, autocorrelation, 'bo')
pyplot.grid(True)
pyplot.show()

autocov = autocovariance(ascii_text)
axis = range(0, len(autocov))
pyplot.title("Autokovarijansa")
pyplot.xlabel("Koraci")
pyplot.plot(axis, autocorrelation, 'bo')
pyplot.grid(True)
pyplot.show()

# BINARY
print("BINARY")
binary_range = range(0, 2)
binary_range_squares = [x**2 for x in binary_range]

histogram, _, _ = pyplot.hist(binary_text, bins=2)
pyplot.show()

probabilities = histogram / binary_text_length

mean = sum(probabilities * binary_range)
print('Srednja vrednost je: '+ str(mean))

samp_mean = sample_mean(binary_text, 10)
print('Srednja vrednost (usrednjavanje po vremenu) je: '+str(samp_mean))

mean_squares = sum(probabilities * binary_range_squares)
print('Srednja kvadratna vrednost je: '+str(mean_squares))

samp_mean_squares = sample_mean(square(binary_text), 10)
print('Srednja kvadratna vrednost (usrednjavanje po vremenu) je: '+str(samp_mean_squares))

variance = mean_squares - mean**2
print('Varijansa je: '+str(variance))

samp_variance = sample_variance(binary_text, 10)
print('Varijansa (usrednjavanje po vremenu) je: '+str(samp_variance))

med = median(binary_range, probabilities)
print('Medijana je: '+str(med))

samp_median = sample_median(binary_text, 10)
print('Medijana (usrednjavanje po vremenu) je: '+str(samp_median))

max_index = numpy.argmax(probabilities)
modus = binary_range[max_index]
print('Modus je: '+str(modus))

samp_mode = sample_mode(binary_text, 10)
print('Modus (usrednjavanje po vremenu) je: '+str(samp_mode))

print("\n\n\n")

autocorrelation = autocorr(binary_text)
axis = range(0, len(autocorrelation))
pyplot.title("Autokorelaciona funkcija")
pyplot.xlabel("Koraci")
pyplot.plot(axis, autocorrelation, 'bo')
pyplot.grid(True)
pyplot.show()

autocov = autocovariance(binary_text)
axis = range(0, len(autocov))
pyplot.title("Autokovarijansa")
pyplot.xlabel("Koraci")
pyplot.plot(axis, autocorrelation, 'bo')
pyplot.grid(True)
pyplot.show()

# BINARY COMPRESSED
print("BINARY COMPRESSED")
binary_compressed_range = range(0, 2)
binary_compressed_range_squares = [x**2 for x in binary_compressed_range]

histogram, _, _ = pyplot.hist(binary_compressed_text, bins=2)
pyplot.show()

probabilities = histogram / binary_compressed_text_length

mean = sum(probabilities * binary_compressed_range)
print('Srednja vrednost je: '+str(mean))

samp_mean = sample_mean(binary_compressed_text, 10)
print('Srednja vrednost (usrednjavanje po vremenu) je: '+str(samp_mean))

mean_squares = sum(probabilities * binary_compressed_range_squares)
print('Srednja kvadratna vrednost je: '+str(mean_squares))

samp_mean_squares = sample_mean(square(binary_compressed_text), 10)
print('Srednja kvadratna vrednost (usrednjavanje po vremenu) je: '+str(samp_mean_squares))

variance = mean_squares - mean**2
print('Varijansa je: '+str(variance))

samp_variance = sample_variance(binary_compressed_text, 10)
print('Varijansa (usrednjavanje po vremenu) je: '+str(samp_variance))

med = median(binary_compressed_range, probabilities)
print('Medijana je: '+str(med))

samp_median = sample_median(binary_compressed_text, 10)
print('Medijana (usrednjavanje po vremenu) je: '+str(samp_median))

max_index = numpy.argmax(probabilities)
modus = binary_compressed_range[max_index]
print('Modus je: '+str(modus))

samp_mode = sample_mode(binary_compressed_text, 10)
print('Modus (usrednjavanje po vremenu) je: '+str(samp_mode))

autocorrelation = autocorr(binary_compressed_text)
axis = range(0, len(autocorrelation))
pyplot.title("Autokorelaciona funkcija")
pyplot.xlabel("Koraci")
pyplot.plot(axis, autocorrelation, 'bo')
pyplot.grid(True)
pyplot.show()

autocov = autocovariance(binary_compressed_text)
axis = range(0, len(autocov))
pyplot.title("Autokovarijansa")
pyplot.xlabel("Koraci")
pyplot.plot(axis, autocorrelation, 'bo')
pyplot.grid(True)
pyplot.show()
