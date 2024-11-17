# »ğÀÔ Á¤·Ä


import random

NumArray = [random.randint(1,100) for _ in range(5000)]

def insertSort(data):
    N = len(data)
    for i in range(N-1):
        for j in range(i+1, 0, -1):
            if data[j] < data[j-1]:
                data[j], data[j-1] = data[j-1], data[j]
            else:
                break;
                
                
    return data

import time
start_time = time.time()
insertSort(NumArray)
end_time = time.time()
execution_time = (end_time - start_time) * 1000


print("Insert")
print(f"{execution_time:.3f} ms")