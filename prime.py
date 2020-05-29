lower = int(input("enter lower bound"))
upper = int(input("enter upper bound"))

for n in range(lower, upper):

    if n == 1: continue

    flag = 1
    for val in range(2, n // 2 + 1):
        if n % val == 0:
            flag = 0
            break

    if flag == 1:
        print("Prime number: ", n)
