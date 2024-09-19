numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

primes = []
not_primes = []

for j in numbers:
    is_prime = True

    if j < 2:
        is_prime = False

    for i in range(2, int(j**0.5) + 1):
        if j % i == 0:
            is_prime = False
            break


    if j > 1:
        primes += [j] if is_prime else []
        not_primes += [j] if not is_prime else []

print('Primes: ', primes)
print('Not Primes: ', not_primes)