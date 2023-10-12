def gen_fibon(n):
    a = 1
    b = 1
    output = []
    for i in range(n):
        output.append(a)
        # yield a
        a, b = b, a + b
    return output


for num in gen_fibon(10):
    print(num)
