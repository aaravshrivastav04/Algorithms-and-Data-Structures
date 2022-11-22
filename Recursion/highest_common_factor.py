def hcf(n1, n2):    # Our function will take two numbers as input
    
    
    # NOTE : THE FOLLOWING LOGIC IMPLEMENTS THE EUCLID's ALGORITHM OF FINDING THE GREATEST COMMON DIVISOR
    
    assert type(n1) == type(n2) == int, "n1 and n2 should be integers only"
    # The two numbers must be integers only

    # Next, we use two if conditions which will convert negative values into their corresponding positive values
    # Because, the HCF of negative numbers is same as that of positive numbers
    if n1 < 0:
        n1 *= -1

    if n2 < 0:
        n2 *= -1

    # As we use the Euclid's algorithm, at one point we end up having the remainder as 0
    # So, as a result our code will throw an error of division by zero
    # To prevent, that  we will immediately return the last divisor as the HCF
    if n1 % n2 == 0:
        return n2
    else:
        # Here, we are coding out the recursive case
        # We can see that in the algorithm we keep on dividing by changing the values of the dividend and the
        # divisor which can be taken as our recursive case
        # So we just keep on replacing the divisor with the last remainder and the dividend with the last divisor
        return hcf(n2, n1 % n2)


print(hcf(25, 75))   # Finally, we are testing our function with sample values of 25 and 75
