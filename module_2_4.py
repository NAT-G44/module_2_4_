numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
print("numbers", numbers)
primes = []
not_primes = []
for number in numbers:
    if number == 1:
        continue
    if number <= 1:                        # число <= 1 - непростое
        not_primes.append(number)           # добавляем в список непростых
        continue                        # переходим на следующую цифру
    is_prime = True                     # флаг правда
    for i in range(2, int(number**0.5) + 1):   # перебор с числа 2,
        if number % i == 0:                  # если число делится на себя без остатка
            is_prime = False            # флаг ложь
            break                          # выходим из цикла
    if is_prime:
        primes.append(number)               # число добавляем в простые
    else:
        not_primes.append(number)           # число добавляем в непростые
print("primes", primes)
print("not_primes", not_primes)












