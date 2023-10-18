import numpy as np
arr = np.random.randint(-1000,1000,1024)
arr.sort()
positive_numbers = []

for num in arr:
    if num >= 0:
        positive_numbers.append(num)

print(positive_numbers)
