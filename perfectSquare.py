def perfect_square(number):
    i = 1
    while (number/2) >= i:
        if number == (i * i):
            print(f"Perfect square of {i}")
            break
        else:
            i += 1
    else:
        print("Not a perfect square")


number = int(input('Enter a number:'))
perfect_square(number)