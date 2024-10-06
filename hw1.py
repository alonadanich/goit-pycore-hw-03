from datetime import datetime


def get_days_from_today(date):
    try:
        given_date = datetime.strptime(date, "%Y-%m-%d").date()
        today = datetime.today().date()
        delta = today - given_date
        return delta.days
    except ValueError:
        return "Неправильний формат дати. Використовуйте формат 'PPPP-MM-DD'."


print(get_days_from_today("2024-11-01"))
print(get_days_from_today("2024-10-01"))
print(get_days_from_today("28-07-2024"))
