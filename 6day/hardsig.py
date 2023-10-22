import time 
import adi 
from scipy.fftpack import fft, ifft,  fftshift, ifftshift 
from scipy import signal 
from scipy.signal import kaiserord, lfilter, firwin, freqz 
import numpy as np 
import matplotlib.pyplot as plt 
 
sdr = adi.Pluto("ip:192.168.2.1") 
table = 1 
sdr.rx_lo = 2452000000 + 2000000 * table 
sdr.tx_lo = 2452000000 + 2000000 * table 
sdr.sample_rate = 1e6
sdr.rx_buffer_size = 1000

samples = np.zeros(1000, dtype=complex)

bits = [0,1,1,0]
for i in range(len(bits)):
   if bits[i]=0:
       samples.append()
    else
   
   
        
        
#2**14 * 1 + 1j * 2**13  
 
#destroy buffer 
#sdr.tx_destroy_buffer() 
 
# Start the transmitter 
sdr.tx_cyclic_buffer = True # Enable cyclic buffers 
sdr.tx(samples) 

# for i in range(1000):
#         if (i==200):
#             sdr.tx(samples)
#             newdata = sdr.rx()
#             rx.extend(abs(newdata))
#  ####
big_array = np.array([])
for r in range(1000): 
    rx = sdr.rx()
    big_array = np.concatenate ((big_array, abs(rx))) 

plt.plot(big_array) 
plt.ylim([-2000, 4000]) 
plt.draw() 
plt.show()
