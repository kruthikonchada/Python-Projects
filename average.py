#Finding the avearge of 3 subjects
if __name__ == '__main__':
    n = int(input())
    avg = 0
    average = ''
    count = 0
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    for i in student_marks:
        if i == query_name:
            for j in student_marks[i]:
                avg += j
            avg /= 3
            avg = str(avg)
            for k in avg:
                count += 1
                if count > 5:
                    break
                else:
                    average += k
            if count < 5:
                average += '0'
    print(average)