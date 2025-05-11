import random

def get_numbers_ticket(min, max, quantity):
    if min < 1 or max > 1000:
        print("Помилка: межі діапазону повинні бути від 1 до 1000.")
        return []
    if min > max:
        print("Помилка: мінімальне значення не може бути більшим за максимальне.")
        return []
    if quantity < 1:
        print("Помилка: кількість чисел має бути не менше 1.")
        return []
    if quantity > (max - min + 1):
        print("Помилка: кількість чисел перевищує кількість доступних унікальних значень у діапазоні.")
        return []
    numbers = random.sample(range(min, max + 1), quantity)
    return sorted(numbers)












