def print_rangoli(size):
    string = ''
    alphas = size + size - 1
    dashes = alphas - 1
    width = alphas + dashes
    output_string = ''
    a = size
    b = a
    char = a
    bottom_half = size
    if size == 1:
        print('a')
    else:
        for i in range(size):
            string = string + chr(97+size-1) + '-'
            output_string = string + output_string + string[-4::-1]
            output_string = output_string.center(width, '-')
            print(output_string)
            output_string = ''
            size = size - 1
        string = ''
        for i in range(bottom_half-1):
            for j in range(a-1):
                string = string + chr(97 + char - 1) + '-'
                char = char - 1
            output_string = string + output_string + string[-4::-1]
            output_string = output_string.center(width, '-')
            print(output_string)
            output_string = ''
            string = ''
            char = b
            a = a - 1

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)