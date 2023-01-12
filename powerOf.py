#Finding out if the given 'number' is obtained or not when 'a' is multiplied several times.
number = int(input())
a = int(input())
if number > 0:
    i = 1
    while number > i:
        i = i * a
    if number == i:
        print(True)
    else:
        print(False)
else:
    print("Invalid number")
