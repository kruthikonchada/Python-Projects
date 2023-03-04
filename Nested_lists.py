lowest_score = 100.00
needed_score = 0.00
result = []
scores = {}
for i in range(int(input())):
    name = input()
    score = float(input())
    if score <= lowest_score:
        lowest_score = score
    if score > needed_score:
        needed_score = score
    scores[name] = score
for i in scores:
    if scores[i] != lowest_score:
        if scores[i] <= needed_score:
            needed_score = scores[i]
for i in scores:
    if scores[i] == needed_score:
        result.append(str(i))
result.sort()
for i in result:
    print(i)

