def hcf(n1, n2):  # Our function will take two numbers as input

    # NOTE : THE FOLLOWING LOGIC IMPLEMENTS THE EUCLID's ALGORITHM OF FINDING THE GREATEST COMMON DIVISOR

    if n1 % n2 == 0:
        return n2
    else:
        while n1 % n2 != 0:  # We move into a while loop which ends when the remainder becomes 0

            # The following piece of code helps us change the values of the last divisor to that of the remainder
            # and the last dividend to that of the last divisor

            k = n1  # We store the value of the last dividend in a variable k such that it's value
            # does not get lost when we assign it the value of the last divisor
            n1 = n2  # Then we change the value of the last dividend to that of the last divisor
            n2 = k % n2  # We also change the value of the last divisor to that of the last remainder

        return n2  # Then, we return the value of the final divisor which is the HCF


print(hcf(25, 75))  # Finally, we test our function with two sample values of 25 and 75
