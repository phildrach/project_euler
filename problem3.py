def prime_factors(n):
	##Returns all the prime factors of a given positive integer
	factors = []
	d = 2
	while n > 1:
		while n % d == 0:
			factors.append(d)
			n /= d
		d += 1

	return factors

pfs = prime_factors(600851475143)
largest_prime_factor = max(pfs)
print(largest_prime_factor)
