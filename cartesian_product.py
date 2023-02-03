from itertools import product

a = [int(a) for a in input().split()]
b = [int(b) for b in input().split()]

#Using normal basic code
output = []
for i in a:
    output.append(i)
    for j in b:
        output.append(j)
        print(tuple(output), end=' ')
        output = []
        output.append(i)
    output = []

#Using Cartesian Product
desired_output = list(product(a,b))
for i in desired_output:
    print(i, end=' ')
