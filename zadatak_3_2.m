clc; clear, close all;

fm = 1000;
fs = 10000;
N = 1000000;
q = 20;
gaussian_variance = 0.2e-3;

%% Signal generation

A = 0.003;
t = (0:N-1)/fs;
s = zeros(1, N);

for k = 1:3
   phi = 2*pi*rand;
   f = fm*rand;
   s = s + A*cos(2*pi*f*t + phi);
end

figure
plot(t, s)
set(gca, 'FontName', 'Times New Roman', 'FontSize', 14)
ylabel('s(t)')
xlabel('t(s)')
title('Zbir sinusoida')

%% Correlated noise generation

R = zeros(q+1, 1);
line = (-1/10)*(0:10) + 1;
R(1:11)=line;

k = 0:q;
figure
stem(k, R)
set(gca, 'FontName', 'Times New Roman', 'FontSize', 14)
xlabel('Pomeraj')
title('Zeljeni oblik autokorelacione funkcije')

noise = randn(1,N).*sqrt(gaussian_variance);
R_mat = toeplitz(R(1:20));
a = -inv(R_mat)*R(2:end);

j = filter(1, [1 a'], noise);

figure
plot(noise)
hold on
plot(j, '--')
hold off
legend('Nekorelisani sum','Korelisani sum')
set(gca, 'FontName', 'Times New Roman', 'FontSize', 14)
xlabel('n')
title('Nekorelisani i korelisani sum')

acf = autocorr(j);
figure
stem(k, acf)
set(gca, 'FontName', 'Times New Roman', 'FontSize', 14)
xlabel('Pomeraj')
title('Autokorelacija suma nakon AR postupka')

%% Adding up noise and signal

f = s + j;

%% Autocorrelation

acf = autocorr(f, N-1);

figure
plot(t, acf)
set(gca, 'FontName', 'Times New Roman', 'FontSize', 14)
xlabel('Pomeraj (s)')
title('Autokorelacija signala')

