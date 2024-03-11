# Python

import csv  # Импортируем необходимую библиотеку


def insertion_sort(array):  # Функция сортировки вставками
    n = len(array)
    for i in range(1, n):
        j = i
        x = array[j]
        while j > 0 and array[j - 1]['Category'] > x['Category']:
            array[j] = array[j - 1]
            j -= 1
        array[j] = x
    return array


with open('products.csv', encoding='utf-8') as file:  # Открываем файл products.csv
    reader = list(csv.DictReader(file, delimiter=';'))  # Создаём объект считывания файла
    reader = insertion_sort(reader)
    bakery = [row for row in reader if row['Category'] == reader[0]['Category']]  # Отбираем только товары первой категории
    most_expansive = max(bakery, key=lambda x: x['Price per unit'])
    print(f'В категории: {most_expansive["Category"]} самый дорогой товар: {most_expansive["product"]}'
          f' его цена за единицу товара составляет {most_expansive["Price per unit"]}')
