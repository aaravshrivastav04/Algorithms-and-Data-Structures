def power(base, exp):
    assert type(exp) == int, "the exponent must be an integer only"
    assert type(base) in [int, float], "the base should be a number only"
    
    if exp == 0:
        return 1
    elif exp < 0:
        return 1/base * power(base, exp+1)
    else:
        return base * power(base, exp - 1)


print(power(2, -2))

