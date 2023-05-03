sum_tickets = 0
qnt_tickets = int(input("Введите количестов билетов: "))
age = int(input("Введите возраст посетителя: "))
for age in range (qnt_tickets):
    if age < 18:
        sum_tickets += 0
    elif 18 <= age <= 25:
        sum_tickets += 990
    elif age > 25:
        sum_tickets += 1390
print("Стоимость Ваших билетов: ", sum_tickets)


