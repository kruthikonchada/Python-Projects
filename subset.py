t = int(input())
for i in range(t):
    count = 0
    a = int(input())
    set_a = set(map(int, input().split()))
    b = int(input())
    set_b = set(map(int, input().split()))
    for i in set_a:
        if i in set_b:
            count += 1
        else:
            print(False)
            break
    if count == a:
        print(True)
