from datetime import datetime

def get_days_from_today(date):
    try:
        given_date = datetime.strptime(date, '%Y-%m-%d').date()
        today = datetime.today().date()
        delta = today - given_date
        return delta.days
    except ValueError:
        print("Помилка: Дата повинна бути у форматі 'РРРР-ММ-ДД'")
        return None

if __name__ == "__main__":
    example_date = "13.14.2000"
    result = get_days_from_today(example_date)
    if result is not None:
        print(result)











