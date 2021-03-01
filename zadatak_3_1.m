clc; clear, close all;

T = 0.001;
A = 0.1;
N = 10000;
fg = 1000;
fs = 10000;
pn = 10e-5;
q = 100;
df = 10;

%% Generating input signal

s = A*idinput([T*fs,1,N/(T*fs)]).';

%% Generating noise

t = linspace(0, 10, N);
noise = 0;
A_noise = sqrt(2*10e-04);
for k = 1:101
   phi = 2*pi*rand; 
   noise = noise + A_noise*cos((2*pi*(k-1-round(N/2))*df)*t + phi);
end

%% Adding signal and noise & calculating SNR before filtration

SNR_pre = snr(s, noise);
x = s + noise;

figure
plot(x)
set(gca, 'FontName', 'Times New Roman', 'FontSize', 14)
ylabel('x(n)')
xlabel('n')
title('Signal sa dodatim sumom')

%% Filtering

F = 1/N .* fft(noise(1:N)); 
F = F(:);
S = 1/N .* fft(x(1:N)); 
S = S(:);
Rff = N .* real(ifft(F .* conj(F)));
Rfv = N .* real(ifft(F .* conj(S)));
RRff = toeplitz(Rff);
Rfv = Rfv';
b = Rfv / RRff; 
b = b(1:100);
vest = fftfilt(b, x);
MSE = mean(s - vest).^2;

figure
stem(b)
set(gca, 'FontName', 'Times New Roman', 'FontSize', 14)
ylabel('Vrednost koeficijenta')
title('Koeficijenti filtra')

figure
plot(vest)
set(gca, 'FontName', 'Times New Roman', 'FontSize', 14)
ylabel('vest(n)')
xlabel('n')
title('Filtrirani signal')

%% Calculating SNR after filtering

SNR_post = snr(vest, noise);
gain = SNR_post - SNR_pre;
