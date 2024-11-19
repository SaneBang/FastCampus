

list1 = [i for i in range(1,100)]


def binarySearch(data, num):
    
    if len(data) == 1 and num == data[0]:
        return True
    
    if len(data) == 1 and num != data[0]:
        return False
    
    if len(data) == 0:
        return False
    
    middle = len(data) // 2
    if num == data[middle]:
        return True
    else:
        if num > data[middle]:
            return binarySearch(data[middle:],num)
        else:
            return binarySearch(data[:middle],num)
        

print(binarySearch(list1, 90))