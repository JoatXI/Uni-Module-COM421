num = [20, 13, 17, 6, 1]
n = 5

for i in range(len(num) - 1):
    for j in range(len(num) - i - 1):
        if num[j] > num[j + 1]:
            temp = num[j]
            num[j] = num[j + 1]
            num[j + 1] = temp
            print(num)