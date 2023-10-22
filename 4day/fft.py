import time
import adi
import matplotlib.pyplot as plt
import numpy as np
from scipy.fftpack import fft, ifft,  fftshift, ifftshift

# Create radio
sdr = adi.Pluto("ip:192.168.2.1")

# Configure properties
sdr.rx_lo = 2462000000

plt.figure("11 channel 2.462 GHz")
#plt.figure("2 GHz")
# Collect data
for r in range(30):
    rx = sdr.rx()
    plt.clf()
    plt.plot(rx.real)
    plt.plot(rx.imag)
    plt.draw()
    plt.pause(0.05)
    time.sleep(0.1)
    if(rx > 1000).any(): break

N=1024 # количество точек ДПФ
X = fft(rx,N)/N
plt.figure("FFT")
plt.stem(abs(X))

plt.show()
