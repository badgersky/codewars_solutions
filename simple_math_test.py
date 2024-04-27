def number_property(n):
    return [is_prime(n), n % 2 == 0, n % 10 == 0]


def is_prime(num):
    if num <= 1:
        return False
    
    for n in range(2, int(num**0.5) + 1):
        if num % n == 0:
            return False
        
    return True


if __name__ == '__main__':
    print(number_property(3))
    print(number_property(13))
    print(number_property(4))
    print(number_property(20))
