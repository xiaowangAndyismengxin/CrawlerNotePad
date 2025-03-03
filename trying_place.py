# Try something at here.
def generator_of_prime():
    num = 2
    while True:
        if is_prime(num):
            yield num
        num += 1
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def main():
    prime_generator = generator_of_prime()
    for primary in prime_generator:
        print(primary)
if __name__ == '__main__':
    main()
