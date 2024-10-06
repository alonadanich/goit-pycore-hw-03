import random


def get_numbers_tickets(min, max, quantity):
    if min < 1 or max > 1000 or quantity > (max - min + 1):
        return []
    random_numbers = random.sample(range(min, max + 1), quantity)
    return sorted(random_numbers)


print(get_numbers_tickets(1, 50, 8))
print(get_numbers_tickets(1, 36, 6))
print(get_numbers_tickets(0, 1001, 25))
