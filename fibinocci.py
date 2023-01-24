#Fibinocci Series
num = int(input())
x = 0
y = 1
j = 1
while j <= num:
    z = x + y
    print(x, end = ' ')
    x = y
    y = z
    j = j + 1

