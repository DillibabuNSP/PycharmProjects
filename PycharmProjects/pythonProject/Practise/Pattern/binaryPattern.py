size = int(input("Enter the Length: "))
for i in range(1, size):
    if i % 2 == 0:
        num = 0
        for j in range(1, size):
            print(num, end='')
            num = 1 if num == 0 else 0
        print()

    else:
        num = 1
        for j in range(1, size):
            print(num, end='')
            num = 1 if num == 0 else 0
        print()
