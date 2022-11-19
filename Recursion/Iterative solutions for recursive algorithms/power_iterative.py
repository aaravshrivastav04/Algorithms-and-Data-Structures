def power(base, exp):
    n = 1
    for i in range(0, exp):
        n *= base

    return n


print(power(4, 0))
