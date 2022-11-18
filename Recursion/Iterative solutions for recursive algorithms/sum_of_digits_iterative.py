n = int(input())  # n will be our input number


def sum_of_digits(input_num):  # Our function takes a parameter n
    k = list(str(input_num))  # The variable k will help us split our number into it's digits and store
    # those in a list

    list_of_digits = []  # l is an empty list

    sum_of_digits = 0  # We define a variable sum whose initial value is 0

    for i in range(1, len(k)):  # if the number of digits is x then the number of times we
        # loop is n-1, so we start with 1
        # We append the quotient and remainder upon dividing by 10
        # in the list l
        list_of_digits.append(input_num // 10)
        list_of_digits.append(input_num % 10)
        input_num //= 10  # Finally, we change the value of n to the new quotient

    for e in list_of_digits:  # The final list also has some numbers which are of more than 1 digit
        # Thus, we remove them here
        if len(list(str(e))) > 1:
            list_of_digits.remove(e)

    for f in list_of_digits:  # Finally, we add all the numbers by storing the result in the sum variable
        # we declared above
        sum_of_digits += f

    return sum_of_digits    # Returning the sum


print(sum_of_digits(n))  # Now, we test this function with our input variable n
