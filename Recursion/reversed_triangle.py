def reversed_triangle(n):  # Our function as a value n as input
    assert type(n) == int and n >= 0, "n must be a positive integer only"
    # n must be a positive integer only
    if n == 0:  # At one point, the value of n becomes 0. Then, we terminate the program
        exit()
    else:
        print(n * str(n))  # We are printing n, n number of times each time on a different line
        reversed_triangle(n - 1)  # To run this for its predecessor we use recursion by calling the function again
        # for (n-1)


reversed_triangle(9)    # Finally, we test our function by providing it with an input value of 9
