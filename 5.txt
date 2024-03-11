# Python
import csv  # Импортируем необходимую библиотеку


with open('products.csv', encoding='utf-8') as file:  # Открываем файл products.csv
    reader = list(csv.DictReader(file, delimiter=';'))  # Создаём объект считывания файла
    hash_table = []
    for row in reader:
        hash_table.append({row['Category']: float(row['Count'])})
    hash_table = sorted(hash_table, key=lambda x: list(x.values())[0])
    for i in range(10):
        print(f'{list(hash_table[i].keys())[0]}, {list(hash_table[i].values())[0]}.')


