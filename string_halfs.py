def merge_the_tools(string, k):
    count = 0
    start = 0
    output_string = ''
    n = len(string)
    end = k
    if k >= 1 and k <= n and n >= 1 and n <= 10000:
        for i in string:
            if i >= 'A' and i <= 'Z':
                count += 1
    if count == n and n % k == 0:
        for j in range(n // k):
            for i in range(start, end):
                if string[i] not in output_string:
                    output_string += string[i]
            start += k
            end += k
            print(output_string)
            output_string = ''


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
