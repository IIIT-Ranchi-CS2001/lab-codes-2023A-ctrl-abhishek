import random
import math
import matplotlib.pyplot as plt

K = int(input("Enter the number of random numbers (minimum 10): "))
while K < 10:
    K = int(input("K should be at least 10. Enter again: "))
N = int(input("Enter the limit for random numbers: "))

random_numbers = [random.randint(1, N) for _ in range(K)]
print(f"Generated list of random numbers: {random_numbers}")

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def separate_prime_composite(numbers):
    primes = [num for num in numbers if is_prime(num)]
    composites = [num for num in numbers if num > 1 and not is_prime(num)]
    return primes, composites

primes, composites = separate_prime_composite(random_numbers)

prime_squares = [p ** 2 for p in primes]
composite_sqrts = [math.sqrt(c) for c in composites]

print(f"Prime numbers: {primes}")
print(f"Squares of prime numbers: {prime_squares}")
print(f"Composite numbers: {composites}")
print(f"Square roots of composite numbers: {composite_sqrts}")

fig, axs = plt.subplots(1, 2, figsize=(14, 6))

axs[0].scatter(primes, prime_squares, color='blue', label='Prime Squares')
axs[0].set_title("Prime Numbers vs Their Squares")
axs[0].set_xlabel("Prime Numbers")
axs[0].set_ylabel("Squares")
axs[0].legend()

axs[1].scatter(composites, composite_sqrts, color='green', label='Composite Square Roots')
axs[1].set_title("Composite Numbers vs Their Square Roots")
axs[1].set_xlabel("Composite Numbers")
axs[1].set_ylabel("Square Roots")
axs[1].legend()

plt.tight_layout()
plt.show()