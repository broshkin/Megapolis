# Python
import csv  # Импортируем необходимую библиотеку


with open('products.csv', encoding='utf-8') as file:  # Открываем файл products.csv
    reader = list(csv.DictReader(file, delimiter=';'))  # Создаём объект считывания файла

    for row in reader:
        # Создаём промокоды
        row['promocode'] = f'{row["product"][:2].upper()}{row["Date"][:2]}{row["product"][-2:][::-1].upper()}{row["Date"].split(".")[1][::-1]}'

with open('product_promo.csv', 'w', newline='', encoding='utf-8') as file:  # Открываем запись файла product_promo.csv
    writer = csv.DictWriter(file, delimiter=';', fieldnames=['Category', 'product', 'Date', 'Price per unit', 'Count', 'promocode'])
    writer.writeheader()  # Записываем заголовки
    writer.writerows(reader)  # Записываем все строки с промокодами
