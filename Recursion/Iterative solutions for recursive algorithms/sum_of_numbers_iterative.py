def sumof(n):  # Our function will take an integer n as input
    sum = 0  # We take an initial variable sum whose intial value assigned is 0
    for i in range(0, n + 1):  # We run a for loop till our number and keep on adding each value of i to it
        sum += i
    return sum  # Then, we return the output


print(sumof(4))  # Finally, we test our function with a sample value of 4
