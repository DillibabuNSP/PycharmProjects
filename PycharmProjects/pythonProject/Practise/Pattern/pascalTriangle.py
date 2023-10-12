size = 5
alpha = 65

# Right Pascal triangle
for i in range(0, size):
    for j in range(0, i + 1):
        print(chr(alpha + j), end=' ')
    print()

for i in range(size - 1, -1, -1):
    for j in range(0, i):
        print(chr(alpha + j), end=' ')
    print()

# Left Pascal triangle
for i in range(1, size + 1):
    for j in range(i, size):
        print(end='  ')
    for k in range(1, i + 1):
        print(chr(alpha + k), end=' ')
    print()

for i in range(size, 0, -1):
    for j in range(i, size + 1):
        print(end='  ')
    for k in range(1, i):
        print(chr(alpha + k), end=' ')
    print()
