# Из заданного числа вычли сумму его его цифр.
# Из результата вновь вычли сумму его цифр и т.д.
# Сколько таких действий надо произвести, чтобы получился нуль python
def f(n):
    s = 0
    while n > 0:
        s += n % 10
        n = n // 10
    return s


c = input("Введите число: ")
while type(c) != int:
    try:
        c = int(c)
    except ValueError:
        print('Неправильно')
        c = input("Введите число: ")
k = 0
while c > 0:
    c -= f(c)
    k += 1

print("Через " + str(k) + " действий")
