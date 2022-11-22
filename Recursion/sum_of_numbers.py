def sumof(n):  # Our function will take a number n as input
    assert type(n) == int and n > 0 , "n should be a positive integer only"  # n should be a positive integer only
    if n in [1, 0]:  # If n is 0 or 1, we return the same value to the user
        return n
    else:
        # The sum of the first n numbers can be written as
        # n + (n-1) + (n-1) .... 0
        # This can be further written as :
        # n + sum of first (n-1) numbers
        # Here's where the recursion happens
        # We have simply coded this logic out in our program
        return n + sumof(n - 1)


print(sumof(4))  # We finally, test our function by giving it sample value of 4
