def reversed_triangle(n):   # Our function will take a number n as input
    for i in range(n, 0, -1):   # We run a for loop backwards from n to 1
        print(i * str(i))   # We are printing i, i number of times each time on a different line


reversed_triangle(9) # Finally, we test our function by providing it with a sample value of 9
