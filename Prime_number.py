#Identifying if a given number is a prime number or not.
num = int(input("Enter a natural number:"))
if num > 1:
    for i in range(2, num//2 + 1):
        if num % i == 0 and num != 2:
            print(f'{num} is a Composite number.')
            break
    else:
        print(f'{num} is a Prime number.')