from datetime import datetime, timedelta


def get_uncomming_birthdays(users):
    today = datetime.today().date()
    upcomming_birthdays = []
    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = birthday.replace(year=today.year)
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)
        if 0 <= (birthday_this_year - today).days <= 7:
            congratulation_date = birthday_this_year
            if congratulation_date.weekday() == 5:
                congratulation_date += timedelta(days=2)
            elif congratulation_date.weekday() == 6:
                congratulation_date += timedelta(days=1)
            upcomming_birthdays.append(
                {
                    "name": user["name"],
                    "congratulation_date": congratulation_date.strftime("%Y.%m.%d"),
                }
            )
    return upcomming_birthdays


users = [
    {"name": "Max", "birthday": "1986.05.23"},
    {"name": "Olena", "birthday": "1988.03.24"},
    {"name": "Sergii", "birthday": "2000.05.26"},
    {"name": "Olha", "birthday": "1977.08.31"},
    {"name": "Mykhaylo", "birthday": "1996.02.14"},
    {"name": "Vasyl", "birthday": "1997.10.5"},
    {"name": "Oleksii", "birthday": "1999.10.8"},
    {"name": "Mykola", "birthday": "1989.10.12"},
]

print(get_uncomming_birthdays(users))
