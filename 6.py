def is_prime(n):
    i = 2
    while i < int(n ** 0.5) + 1:
        if n % i == 0:
            return False
        i += 1
    return True


if __name__ == '__main__':
    num = int(input("Введите число: "))
    if is_prime(num):
        print("Простое")
    else:
        print("Состовное")
