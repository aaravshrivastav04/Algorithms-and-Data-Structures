def factorial(n):
    # Our contraint is that n should be a positive integer only
    assert 0 <= n == int(n), 'The number must be a positive integer only'
    # The factorial of both 0 and 1 is 1. Thus, to prevent an infinite loop it's essential 
    # to define our base condition
    if n in [0, 1]:
        return 1
    else:
        # Our function can we written as f(n) = n * f(n-1) 
        # This where we use recursion 
        return n * factorial(n - 1)

# Finally we test our function by giving it an input value of 10
print(factorial(10))

