def get_factors(number):

    factors = []
    for n in range(1, number + 1):
        if number % n == 0:
            factors.append(n)
    return factors