# Python

import csv  # Импортируем необходимую библиотеку

with open('products.csv', encoding='utf-8') as file:  # Открываем файл products.csv
    reader = list(csv.DictReader(file, delimiter=';'))  # Создаём объект считывания файла
    total_of_snacks = 0  # Создаём переменную для записывания итоговой суммы закусок
    for row in reader:
        row['total'] = float(row['Price per unit']) * float(row['Count'])  # Присваиваем числовое значение стоблца total

        if row['Category'] == 'Закуски':
            total_of_snacks += row['total']   # Считаем количество итоговых сумм всех закусок

with open('products_new.csv', 'w', newline='', encoding='utf-8') as file:  # Открываем файл products_new.csv
    writer = csv.DictWriter(file, fieldnames=['Category', 'product', 'Date', 'Price per unit', 'Count', 'total'],
                            delimiter=';')  # Создаём объект записывания в файл
    writer.writeheader()  # Записываем заголовки
    writer.writerows(reader)  # Записываем все строки

print(total_of_snacks)  # Выводим итоговую сумму закусок