#ABC is a right angled triangle, angle B is 90 degress and M is the median.
#Finding the angle of MBC.
import math
ab = int(input())
bc = int(input())
degree = chr(176)
ac = math.sqrt(ab**2 + bc**2)
mc = ac/2.0
bm = mc
if ab == bc:
    print('45', end='')
    print(degree)
else:
    angle_b_radian = math.acos(bc/ac)
    angle_b_degree = (180 * angle_b_radian) / math.pi
    degree_count = int(angle_b_degree + 1) - angle_b_degree
    if degree_count <= 0.5:
        print(int(angle_b_degree+1), end='')
    else:
        print(int(angle_b_degree), end='')
    print(degree)
