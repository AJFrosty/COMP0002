def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

primes = []
count = 0

for i in range(2, 1001):
    if is_prime(i):
        primes.append(i)
        count += 1

for i, prime in enumerate(primes):
    print(prime, end=" ")
    if (i + 1) % 8 == 0:
        print()
