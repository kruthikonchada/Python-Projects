if __name__ == '__main__':
    N = int(input())
    l = []
    a = []
    for x in range(N):
        a = input().split(' ')
        if a[0] == "insert":
            l.insert(int(a[1]), int(a[2]))
        elif a[0] == "print":
            print(l)
        elif a[0] == "append":
            l.append(int(a[1]))
        elif a[0] == "remove":
            l.remove(int(a[1]))
        elif a[0] == "sort":
            l.sort()
        elif a[0] == "pop":
            s = l.pop()
        elif a[0] == "reverse":
            l.reverse()
