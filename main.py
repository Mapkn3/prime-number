from math import gcd
from random import getrandbits, randint


def is_prime(a):
    return all(a % i for i in range(2, a))


def factorize(n):
    factors = []

    p = 2
    while True:
        while n % p == 0 and n > 0:
            factors.append(int(p))
            n = n / p
        p += 1
        if p > n / p:
            break
    if n > 1:
        factors.append(int(n))
    return factors


def calculate_legendre(a, p):
    if a >= p or a < 0:
        return calculate_legendre(a % p, p)
    elif a == 0 or a == 1:
        return a
    elif a == 2:
        if p % 8 == 1 or p % 8 == 7:
            return 1
        else:
            return -1
    elif a == p - 1:
        if p % 4 == 1:
            return 1
        else:
            return -1
    elif not is_prime(a):
        factors = factorize(a)
        product = 1
        for pi in factors:
            product *= calculate_legendre(pi, p)
        return product
    else:
        if ((p - 1) / 2) % 2 == 0 or ((a - 1) / 2) % 2 == 0:
            return calculate_legendre(p, a)
        else:
            return (-1) * calculate_legendre(p, a)


def solovay_strassen_primality_test(n, a):
    if gcd(a, n) != 1:
        return 'Incorrect a'
    an = pow(a, (n - 1) // 2, n)
    if an == (n - 1):
        an = -1
    if not (is_prime(n) and an == calculate_legendre(a, n)):
        return 'Not prime'
    return 'Prime'


def generate_n(count_bit):
    return getrandbits(count_bit) | int('1' + '0' * (count_bit - 2) + '1', 2)


def check_prime(n):
    first_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101,
                    103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199,
                    211, 223, 227, 229, 233, 239, 241, 251]
    return all(n % prime for prime in first_primes)


if __name__ == '__main__':
    p_bits = 24
    x = generate_n(p_bits)
    while not check_prime(x):
        x = generate_n(p_bits)
    print(f'x = {x}')
    for _ in range(5):
        test_a = randint(1, x - 1)
        print(f'a = {test_a}')
        print(solovay_strassen_primality_test(x, test_a))
