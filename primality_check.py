from math import sqrt

def is_prime(given_n):
    if given_n == 2 or given_n == 3 or given_n == 5:
        return True
    elif given_n%2 == 0 or given_n == 1:
        return False
    else:
        n = int(sqrt(given_n))
        for i in range(3, n+1, 2):
            if given_n%i == 0:
                return False
    return True

given_n = int(input("Give me a number to check for primality: "))

if is_prime(given_n) == True:
    print("Prime")
else:
    print("Not prime")
