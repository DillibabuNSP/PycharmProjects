n = int(input("Enter number of rows:"))
m = (2 * n)-6
for i in range(0, n):
    for j in range(0, m):
        print(end=' ')
    m = m - 1
    for j in range(0, i + 1):
        print("*", end=' ')
    print(" ")
