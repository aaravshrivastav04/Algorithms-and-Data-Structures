# 0, 1, 1, 2, 3, 5, 8, 13, 21

def fibonacci(n):
    # Our constraint is that n should be a positive integer only
    assert 0 <= n == int(n), "n should be a positive integer only"
    # The fibonacci of 0 is 0 and that of 1 is 1.
    # Thus, it's essential to define our base condition such that our code does not end up in an infinite loop
    if n in [0, 1]:
        return n
    else:
        # Our function can be written as f(n-1) + f(n-2)
        # Here's where the recursion takes place
        # Note : here n is the index in the fibonacci series and not the value
        # The indexes start from 0
        return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(7))  # Finally, we test our function by giving it an input index of 7
# We get an output 13 as it is the 7th number in the fibonacci series
