def superset(l, n_set):
    count = 0
    if l <= n_set:
        yield False
    else:
        for i in n_set:
            if i in l:
                count += 1
            else:
                yield False
        if count == len(n_set):
            yield True

l1 = set(map(int, input().split()))
n = int(input())
for i in range(n):
    n_set = set(map(int, input().split()))
    res = superset(l1, n_set)
print(all(res))