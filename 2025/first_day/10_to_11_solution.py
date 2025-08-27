# Задача:
# Ввести с клавиатуры три числа,
# вычислить от каждого из них двойной факториал 
# (произведение всех натуральных чисел, меньших n,
# с такой же, как у n 
# чётностью), а результаты -- сложить. 
# Вывести сумму на экран.

# (Для проверки можно использовать https://en.wikipedia.org/wiki/Double_factorial)

a1 = int(input())
a2 = int(input())
a3 = int(input())

def double_factorial(n):
    remainder = n % 2
    res = 1
    for i in range(1, n + 1):
        if i % 2 == remainder:
            res *= i
    return res

print(double_factorial(a1) + double_factorial(a2) + double_factorial(a3))