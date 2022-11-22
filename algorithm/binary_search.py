import math

squares = [i*i for i in range(100)]
print(squares)

number = int(input("Enter a number: "))
start = 0
end = len(squares) - 1
found = False

while found == False and start <= end:
    midpoint = math.floor((start + end) / 2)
    if number > squares[midpoint]:
        start = midpoint + 1
    elif number < squares[midpoint]:
        end = midpoint - 1
    else:
        found = True
        
if number == squares[midpoint]:
    print("The number was found")
else:
    print("The number was not found")