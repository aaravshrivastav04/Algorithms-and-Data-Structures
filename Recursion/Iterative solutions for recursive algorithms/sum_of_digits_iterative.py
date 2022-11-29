number = int(input())

def sum_of_digits(n):
    sum = 0
    while(n > 0):
        digit = n % 10
        sum+=digit
        n//=10
       return sum

print(sum_of_digits(123))
