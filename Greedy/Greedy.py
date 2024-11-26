# Greedy

# ���� ����
# �����ؾ� �ϴ� ���� 4720�� �϶� 1, 50, 100, 500 �������� ������ ���� ���� ���� �����Ͻÿ�.

coin_list = [500, 100, 50, 1]

def min_coin_count(value, coin_list):
    total_count = 0
    details = list()
    coin_list.sort(reverse=True)
    for coin in coin_list:
        coin_num = value // coin
        total_count += coin_num
        value -= coin_num * coin
        details.append([coin, coin_num])
    return total_count

print(min_coin_count(4720,coin_list))

data_list = [(10,10), (15,12), (20,10), (25,8), (30,5)]
# ���� �� ��ġ�� ���

data_list = sorted(data_list, key=lambda x:x[1]/x[0], reverse=True)
print(data_list)

def get_max_value(data_list, capacity):
    data_list = sorted(data_list, key = lambda x:x[1]/x[0], reverse=True)
    total_value = 0
    details = list()
    
    for data in data_list:
        if capacity - data[0] >= 0:
            capacity -= data[0]
            total_value += data[1]
            details.append([data[0],data[1],1])
        else:
            fraction = capacity / data[0]
            total_value += data[1] * fraction
            details.append([data[0],data[1],1])
            
            break
    return total_value


print(get_max_value(data_list, 30))
            
