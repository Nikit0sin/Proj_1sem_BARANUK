# Дано целое число A. Проверить истинности высказывания:"Число A является положительным"
A = input("Введите число (A): ")
while type(A) != int:
    try:
        A = int(A)
    except ValueError:
        print('Число введено неправильно')
        A = input("Введите число (A): ")
print("Число положительно: ", A > 0)
