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
    # Fermat test incorrectly declares composite numbers prime roughly 1/2 of the time, so anything found prime
    # by the test is (1/2)^k% likely to be correct, where k is the number of repeated tests
    return 1.0 - (1.0 / pow(2, k))


def mprobability(k):
    # Miller-Rabin test incorrectly declares composite numbers prime roughly 1/4 of the time, so anything found prime
    # by the test is (3/4)^k% likely to be correct, where k is the number of repeated tests
    return 1.0 - (1.0 / pow(4, k))


def fermat(N, k):
    # You will need to implement this function and change the return value, which should be
    # either 'prime' or 'composite'.
    #
    # To generate random values for a, you will most likley want to use
    # random.randint(low,hi) which gives a random integer between low and
    #  hi, inclusive.


    for i in range(k): # conduct k tests
        a = random.randint(2, N - 1) # choose a random number between 2 and N - 1 to test
        if mod_exp(a, N - 1, N) != 1: # if a^(N - 1) =/= 1 mod(N), then the number must be composite
            return 'composite'
    # if no tests are failed, the number is probably prime (but may not be)
    return 'prime'


def miller_rabin(N, k):
    # You will need to implement this function and change the return value, which should be
    # either 'prime' or 'composite'.
    #
    # To generate random values for a, you will most likley want to use
    # random.randint(low,hi) which gives a random integer between low and
    #  hi, inclusive.

    for i in range(k): # conduct k tests
        a = random.randint(2, N - 1) # choose a random number between 2 and N - 1 to test
        if mod_exp(a, N - 1, N) != 1: # if a^(N - 1) =/= 1 mod(N), then the number must be composite
            return 'composite'

        # if the number is not yet found to be composite, repeatedly square root the number and see if the number
        # continues to be in the equivalence class of 1
        n = N - 1
        while n % 2 == 0: # continue while the exponent is divisible by 2
            x = mod_exp(a, n, N) # get the modular exponentiation of a
            if x != 1:
                if x == N - 1: # If it is in the equivalence class of -1, the number could be prime.
                    break
                else:
                    return 'composite' # If it is neither 1 nor -1, the number is composite
            n /= 2
    # if no tests are failed, the number is probably prime (but may not be)
    return 'prime'
