#aaabbbbbbddffefd
#output will be: bad

string = input()
already_counted = {}
for i in string:
    if i not in already_counted.keys():
        if string.count(i) > 1:
            already_counted[i] = string.count(i)
print(already_counted)

def MaxValues(already_counted):
    maximum = max(already_counted.values())
    for j in already_counted.keys():
        if already_counted[j] == maximum:
            already_counted[j] = 0
            return j


i = len(already_counted.values()) - 1
res = ''
while i > 0:
    res = res + MaxValues(already_counted)
    i -= 1
print(res)

