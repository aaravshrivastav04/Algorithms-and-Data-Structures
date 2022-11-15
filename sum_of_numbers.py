l1 = [1, 2, 3, 4, 5, 6, 7]


def sumof(l):  # Our function will take a list as input
    # assert type(l) == int, "n must be an integer only"
    if not l:  # Our base condition is that if the list passed is empty the sum will be returned as 0
        return 0
    else:
        # Here's where the recursion happens
        # Taking a list [1,2,3,4,5] and a function f which returns the sum of all the digits
        # present in the list we observe the following
        # The sum of all digits is 1 + 2 + 3 + 4 + 5 = 15
        # This is also equal to the first element of the list added to the sum of the
        # digits present in the rest of the list
        # Thus, our function can be written as :
        # f(l) = l[0] + f(l[1:)
        assert type(l[0]) == int, "the list must contain integers only"
        return l[0] + sumof(l[1:])


print(sumof(l1))  # Finally, we use a list l1 to test our code
