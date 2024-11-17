
import random

NumArray = [random.randint(1,100) for _ in range(5000)]

def selectionSort(data):
    for i in range(len(data)-1):
        lowest = i
        for j in range(lowest + 1, len(data)):
            if data[lowest] > data[j]:
                lowest = j
        data[lowest], data[i] = data[i], data[lowest] 
    return data

import time
start_time = time.time()
print(selectionSort(NumArray))
end_time = time.time()

execution_time = (end_time - start_time) * 1000

print("Select")
print(f"{execution_time:.3f} ms")