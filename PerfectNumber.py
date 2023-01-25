#6 = 1, 2, 3 = 1 + 2 + 3 = 6
num = int(input())
sum = 0
i = 1
while i <= (num//2):
    if num % i == 0:
        sum = sum + i
    i = i + 1
if sum == num:
    print('Perfect square')
else:
    print('Not a Perfect square')