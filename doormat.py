n, m = input().split()
n = int(n)
m = int(m)
output_string = ''
mat = ''

if n % 2 != 0 and m == n * 3:
    for i in range(n):
        if i <= n//2 - 1:
            if i == 0:
                mat = mat + '.|.'
                output_string = output_string + mat.center(m, '-')
            else:
                for j in range(2):
                    mat = mat + '.|.'
                output_string = output_string + mat.center(m, '-')
            print(output_string)
            output_string = ''
        elif i == n//2:
            mat = 'WELCOME'
            output_string = output_string + mat.center(m, '-')
            print(output_string)
            output_string = ''
            mat = ''
        else:
            for k in range(n-2):
                mat = mat + '.|.'
            n = n - 2
            output_string = output_string + mat.center(m, '-')
            print(output_string)
            output_string = ''
            mat = ''
            