def prime_number(low_border: int, high_border: int):
    list_of_primes = []

    # нижний или верхний порог меньше 0
    if low_border * high_border < 0:
        return []

    # нижний порог больше верхнего
    elif low_border > high_border:
        return []

    # O(n^2)
    for number in range(low_border, high_border):
        if number > 1:
            for i in range(2, number):
                if (number % i) == 0:
                    break
            else:
                list_of_primes.append(number)

    return list_of_primes