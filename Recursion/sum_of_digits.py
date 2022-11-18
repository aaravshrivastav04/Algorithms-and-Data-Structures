def sum_of_digits(n):
    assert type(n) == int and n>0, "n should be a positive integer only"
    if n == 0:
        return n
    else:
        return (n % 10) + sum_of_digits(int(n // 10))


print(sum_of_digits(123))
