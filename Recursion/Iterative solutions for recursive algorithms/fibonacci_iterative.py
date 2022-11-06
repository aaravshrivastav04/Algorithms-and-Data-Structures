def gen_fib(a, b, r):  # Defining our function

    # Printing our initial values

    print(a)
    print(b)

    # Going into a for loop to keep on changing the values of a and b
    # which in turn changes their sum

    for i in range(0, r + 1):
        c = (a + b)  # Printing the sum
        print(c)

        # These will be the new values of a and b

        a = b
        b = c


gen_fib(1, 2, 10)  # Finally we call our function to test it's output
