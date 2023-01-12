def missing_number(original_list):
    missing_list = []
    count = original_list[0]
    for i in original_list:
        if i != count:
            for j in range(count,i):
                missing_list.append(count)
                count += 1
        count += 1
    print(missing_list)

number = int(input('Enetr how many values you want to insert:'))
list = []
for i in range(number):
    value = int(input('Enter the value:'))
    list.append(value)
missing_number(list)