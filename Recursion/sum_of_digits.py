def sum_of_digits(n):   # Our function will take an integer n as input
    assert type(n) == int and n > 0, "n should be a positive integer only" # n should always be a positive integer only
    if n == 0:  # It's essential to define our base condition as otheriwise our code will run into an infinite loop
        return n # If the integer given is 0 then our code will return 0
    else:
        return (n % 10) + sum_of_digits(int(n // 10)) # Here's where the actual recursion happens. Let's say that there is a four digit number, then to get all it's 
                                                      # digits we will have to keep on dividing by 10 three times


print(sum_of_digits(123))   # Finally we test our function by a sample number 123
