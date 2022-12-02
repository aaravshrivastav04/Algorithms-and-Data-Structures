number = int(input())

def sum_of_digits(n): # Our function will take a number n as input
    sum = 0 # We define a variable sum which will take an initial value of 0
    while(n > 0):   # We run a while loop till the number n is greater than 0
        digit = n % 10  # The digits of any number can be obtained by getting the remainder when dividing by 10 
                        # iteratively by changing the value of the number each time to the new quotitent    
        sum+=digit  # We keep on adding each digit extracted to the sum variable defined above
        n//=10  # We also change the value of the number n to the new quotitent each time
       return sum   # Then, we return the variable sum

print(sum_of_digits(123)) # Finally, we test our function by providing it with  a sample value of 123 
