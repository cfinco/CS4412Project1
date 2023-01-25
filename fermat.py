import random
import math


def prime_test(N, k):
    # This is main function, that is connected to the Test button. You don't need to touch it.
    return fermat(N, k), miller_rabin(N, k)


def mod_exp(x, y, N):
    # You will need to implement this function and change the return value.
    if y == 0:
        return 1
    else:
        z = mod_exp(x, math.floor(y / 2), N)
        if y % 2 == 0:
            return (pow(z, 2)) % N
        else:
            return (x * pow(z, 2)) % N


def fprobability(k):
    # You will need to implement this function and change the return value.   
    return 1.0 - (1.0 / pow(2, k))


def mprobability(k):
    # You will need to implement this function and change the return value.
    return 1.0 - (1.0 / pow(4, k))


def fermat(N, k):
    # You will need to implement this function and change the return value, which should be
    # either 'prime' or 'composite'.
    #
    # To generate random values for a, you will most likley want to use
    # random.randint(low,hi) which gives a random integer between low and
    #  hi, inclusive.
    for i in range(k):
        a = random.randint(2, N - 1)
        if mod_exp(a, N - 1, N) != 1:
            return 'composite'
    return 'prime'


def miller_rabin(N, k):
    # You will need to implement this function and change the return value, which should be
    # either 'prime' or 'composite'.
    #
    # To generate random values for a, you will most likley want to use
    # random.randint(low,hi) which gives a random integer between low and
    #  hi, inclusive.

    for i in range(k):
        a = random.randint(2, N - 1)
        if mod_exp(a, N - 1, N) != 1:
            return 'composite'

        n = N - 1
        while n % 2 == 0:
            x = mod_exp(a, N - 1, N)
            if x != 1:
                if x == -1:
                    break
                else:
                    return 'composite'
            n /= 2
    return 'prime'
