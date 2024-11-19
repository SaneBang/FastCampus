# 동적 계획법

# 피보나치
def fibo(num):
    fibolist = [0] * 10000
    fibolist[0:6] = [0, 1, 1, 2, 3, 5]
    if num < 6:
        return fibolist[num]
    
    for i in range(6, num+1):
        fibolist[i] = fibolist[i-1] + fibolist[i-2]
    return fibolist[num]
        

print(fibo(10))

     

