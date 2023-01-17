#Capitalizing every first letter of each word.
def solve(s):
    count = 0
    string = ''
    for i in s:
        if ord(i) >= ord('0') and ord(i) <= ord('9'):
            string = string + i
            count = 0
        elif i >= 'A' and i <= 'Z':
            string = string + i
            count = 0
        else:
            if i == s[0]:
                string = chr(ord(i) - 32)
            elif i == ' ':
                string = string + i
                count = count + 1
            elif count >= 1:
                string = string + chr(ord(i) - 32)
                count = 0
            else:
                string = string + i
    print(string)

if __name__ == '__main__':
    n = input()
    solve(n)

