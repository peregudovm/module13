ticket = int(input("Введите количество билетов:"))
print(ticket)
price = []
for i in range(1, ticket+1):
    age = int(input(f"Введите возраст {i} посетителя: "))
    if 0 < age < 18:
        price.append(0)
    elif 17 < age < 25:
        price.append(990)
    elif 24 < age < 100:
        price.append(1390)
    else:
        print("Введен некорректный возраст")



    # Если купили более 3х билетов, то выводится сумма к оплате с учетом скидки 10%,
    if ticket > 3:
        print("Сумма к оплате с учетом скидки: ", sum(price) - ((sum(price) / 100) * 10), "рублей")
    else:
        print("Сумма к оплате: ", sum(price), "рублей")