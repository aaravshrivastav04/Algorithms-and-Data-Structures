def dtb(n):
    l = []
    while n // 2 != 0:
        l.append(n % 2)
        n //= 2

    l.append(n % 2)

    final = ""
    for e in reversed(l):
        final += str(e)

    return int(final)


print(dtb(13))
