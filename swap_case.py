#Converting capital letters to small letters and vice versa.
def swap_case(s):
    string = ''
    if len(s) > 0 and len(s) < 1001:
        for i in s:
            if i >= 'a' and i <= 'z':
                i = chr(ord(i) - 32)
                string = string + i
            elif i >= 'A' and i <= 'Z':
                i = chr(ord(i) + 32)
                string = string + i
            else:
                string = string + i
    return string

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)