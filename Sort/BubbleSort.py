import random


NumArray = [random.randint(1, 100) for _ in range(5000)]

def bubbleSort(data):
    N = len(data)
    for i in range(N-1):
        isSwap = False
        for j in range(N-i-1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j+1], data[j]
                isSwap = True
        if isSwap == False:
            break
    return data

import time
start_time = time.time()
bubbleSort(NumArray)
end_time = time.time()

execution_time = (end_time - start_time) * 1000

print("Bubble")
print(f"{execution_time:.3f} ms")
