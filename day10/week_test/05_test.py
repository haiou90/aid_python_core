def calculate_prime(start,end):
    prime = []
    for numerator in range(start,end+1):
        count = 0
        # sum = 0
        for denominator in range(2,numerator):
            if numerator % denominator == 0:
                count += 1
                # sum += count
        if count == 0:
            prime.append(numerator)

    return prime
result = calculate_prime(2,20)
print(result)


def calculate_prime(start,end):
    prime = []
    for numerator in range(start,end+1):
        count = 0
        for denominator in range(2,numerator):
            if numerator % denominator == 0:
                  count += 1
        if count == 0:
            prime.append(numerator)

    return prime
result = calculate_prime(2,20)
print(result)
