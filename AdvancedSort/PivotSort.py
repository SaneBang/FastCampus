# 퀵 정렬
# 오름차순이나 내림차순 정렬된 경우 피봇정렬하면 최악의 시간복잡도를 가진 O(n^2)

list1 = [49, 97, 53 , 5, 33, 65, 62 ,51]

def pivotSort(data):
    if len(data) <= 1:
        return data
    left, right = list(),list()
    
    pivot = data[0]
    for i in range(1, len(data)):
        if pivot > data[i]:
            left.append(data[i])
        else:
            right.append(data[i])
    return pivotSort(left) + [pivot] + pivotSort(right)

print(pivotSort(list1))

