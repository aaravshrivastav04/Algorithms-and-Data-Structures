def factorial(n):
    f = 1 # Initialising a variable f whose initial value will be 1
    for i in range(n, 1, -1): # We loop backwards from n till we reach 1
        f *= i  # While looping we multiply f with each value of i each time
    return f # Finally, we return the factorial of the input number


  # We also test our factorial function by providing an input value of 5
print(factorial(5))
