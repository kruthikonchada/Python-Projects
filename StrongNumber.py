#145 = 5! + 4! + 1! = 120 + 24 + 1 = 145
num = int(input())
s = 0
bkp = num
while num > 0:
    t = num % 10
    fact = 1
    while t >= 1:
        fact *= t
        t -= 1
    s += fact
    num //= 10
if s == bkp:
    print('Strong Number')
else:
    print('Not a Strong Number')