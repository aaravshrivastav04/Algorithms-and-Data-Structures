def dtb(n):
    assert type(n) == int, "n should be an integer only"
    if n == 0:
        return 0
    else:
        return n % 2 + 10 * dtb(n // 2)


print(dtb(13))
