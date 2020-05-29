import math

number = int(input())
num = number / 2
rows = math.ceil(num / 2)
lines = rows * 2
var = rows
star = 2
start1 = 1
start2 = number - rows
temp = start2
end = number
for i in range(rows):
    temp = start2
    lines = var * 2
    var -= 1
    if i != 0:
        for k in range(star):
            print('*', end='')
            star += 2
    for j in range(lines):
        if j < lines / 2:
            print(start1, end='0')
            start1 += 1
        else:
            if start2 < end - 1:
                start2 += 1
                print(start2, end='0')
            else:
                print(start2 + 1, end='')
    end = temp
    start2 = temp - var

    print('')
