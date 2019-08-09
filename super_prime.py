import math


def prime(number):
    if number ==1:
        return False
    for i in range (2, int(math.sqrt(number))+1):
        if number % i == 0:
            return False
    return True


res = prime(24)


def is_super_prime():

    i = 2
    is_superprime = True


    return