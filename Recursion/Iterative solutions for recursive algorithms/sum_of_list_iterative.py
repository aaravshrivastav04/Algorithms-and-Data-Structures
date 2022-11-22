l1 = [1,2,3,4,5,6,7]


def sumof(l):   # Our function will take a list l as input
    sum = 0 # We define a variable sum with an initial value 0
    for e in l: # Now, we iterate through our list and keep on adding each number to our sum variable
        sum += e
    return sum  # Now, we return the output


print(sumof(l1)) # Finally, we test our function with a sample list l1
