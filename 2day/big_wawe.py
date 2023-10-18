import numpy as np
import matplotlib.pyplot as plt
import time 
import random

big_np_array_1 = np.random.sample(3000000)
start = time.time() 
np.sort(big_np_array_1)

end = time.time() - start 
print(end) 

big_lists_array_1 = []
for i in range(3000000):
    big_lists_array_1.append(random.random())

start = time.time() 
big_lists_array_1.sort()

end = time.time() - start 
print(end) 

n = 40
# time vector
t = np.linspace(0, 1, n, endpoint=True)
# sine wave
x = np.sin(np.pi*t) + np.sin(2*np.pi*t) + np.sin(3*np.pi*t) + np.sin(5*np.pi*t)

fig = plt.figure(figsize=(16, 5), dpi=100)
plt.plot(t, x)
