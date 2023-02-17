if __name__ == '__main__':
    s = input()
    count = 0
    for i in s:
        if i.isalnum() == False:
            count += 1
        else:
            count = 0
            print(True)
            break
    if count == len(s):
        print(False)
        count = 0
    for i in s:
        if i.isalpha() == False:
            count += 1
        else:
            count = 0
            print(True)
            break
    if count == len(s):
        print(False)
        count = 0
    for i in s:
        if i.isdigit() == False:
            count += 1
        else:
            count = 0
            print(True)
            break
    if count == len(s):
        print(False)
        count = 0
    for i in s:
        if i.islower() == False:
            count += 1
        else:
            count = 0
            print(True)
            break
    if count == len(s):
        print(False)
        count = 0
    for i in s:
        if i.isupper() == False:
            count += 1
        else:
            count = 0
            print(True)
            break
    if count == len(s):
        print(False)
        count = 0
