from datetime import datetime

def get_days_from_today(date):
    """
    Розраховує кількість днів між заданою датою і поточною датою.

    :param date: str, дата у форматі 'РРРР-ММ-ДД'.
    :return: int, кількість днів від заданої дати до поточної.
    """
    try:
        # Перетворення рядка дати на об'єкт datetime
        given_date = datetime.strptime(date, '%Y-%m-%d').date()
        # Отримання поточної дати
        today = datetime.today().date()
        # Обчислення різниці в днях
        delta = today - given_date
        return delta.days
    except ValueError:
        raise ValueError("Дата повинна бути у форматі 'РРРР-ММ-ДД'")

# Приклад використання функції
if __name__ == "__main__":
    try:
        example_date = "2021-10-09"
        print(get_days_from_today(example_date))
    except ValueError as e:
        print(e)









