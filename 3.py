# Python
import csv  # Импортируем необходимую библиотеку


with open('products.csv', encoding='utf-8') as file:  # Открываем файл products.csv
    reader = list(csv.DictReader(file, delimiter=';'))  # Создаём объект считывания файла

    request = input()  # Создаём переменную запроса

    all_categories = []  # Создаём переменную с названиями всех категорий

    reader = sorted(reader, key=lambda x: float(x['Count']))  # Сортируем список по количеству продаж

    for row in reader:  # Заполняем список с названиями всех категорий
        if row['Category'] not in all_categories:
            all_categories.append(row['Category'])

    while request != 'молоко':  # Создаём цикл пока не будет ввод "молоко"
        if request in all_categories:
            for row in reader:
                if request == row['Category']:  # В случае совпадения с названием категории выводим нужный товар
                    print(f'В категории: {row["Category"]} товар {row["product"]} был куплен {row["Count"]} раз')
                    break
        else:
            print('Такой категории не существует в нашей БД')
        request = input()
