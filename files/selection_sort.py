list = [7, 4, 5, 9, 8, 2, 1]
n = 7

for i in range(len(list) - 1):
    latest_lowest = 99999
    lowest_index = -1
    
    for j in range(i, len(list)):
        if list[j] < latest_lowest:
            latest_lowest = list[j]
            lowest_index = j
            
    temp = list[i]
    list[i] = latest_lowest
    list[lowest_index] = temp
    
print(list)