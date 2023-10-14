import datetime


def is_int(s):
    try:
        return int(s)
    except ValueError:
        return False
def is_float(s):
    try:
        return float(s)
    except ValueError:
        return False

def is_date(d, m, y):
    try:
        return datetime.date(y, m, d)
    except ValueError:
        return False
print('Программа для контроля собственных денежных средств')
favorites = dict()
shopping_list = {'Одежда':{}, 'Еда':{}, 'Техника':{}}
while True:
    print('Доступны команды:\n'
                   '1. Зафиксировать новую покупку\n'
                   '2. Добавить продукт в коллекцию "избранное"\n'
                   '3. Посмотреть или редактировать список покупок\n'
                   '4. Поиск товара по дате покупки\n'
                   '5. Посмотреть или редактировать коллекцию "избранное"\n'
                   '6. Выйти из программы')
    all_products = {}
    for category in shopping_list:
        for product in shopping_list[category]:
            all_products[product] = shopping_list[category][product]
    choise = input('Введите номер команды, которую хотите совершить: ')
    while not is_int(choise):
        choise = input('Номер команды был введен с ошибкой, повторите попытку. Введите номер команды, которую хотите совершить: ')
    choise=int(choise)

    match choise:
        case 1:
            name_product = input('Введите название приобретенного товара: ')
            day = input('Введите число, когда был приобретен товар: ')
            month = input('Введите номер месяца, когда был приобретен товар: ')
            year = input('Введите номер года, когда был приобретен товар: ')


            while not is_int(day):
                day = input('Число было введено с ошибкой, повторите попытку.Введите число, когда был приобретен товар: ' )
            while not is_int(month):
                month = input('Номер месяца был введен с ошибкой, повторите попытку.Введите номер месяца, когда был приобретен товар: ' )
            while not is_int(year):
                year = input('Год был введен с ошибкой, повторите попытку.Введите номер года, когда был приобретен товар: ' )

            day, month, year = map(int, [day, month, year])
            while not is_date(day, month, year):
                day, month, year = map(int, input('Введенной даты не существует. Повторите попытку. '
                                                  'Введите дату, когда был приобретен товар в формате '
                                                  'Число. номер месяца. номер года: ').split('.'))
            date = datetime.date(year, month, day)
            price = input("Введите цену товара в рублях, если в цене есть копейки, "
                          "поставьте после целочисленной части рубля точку и введите копейки без"
                          " лишних знаков: ")
            while not is_float(price):
                price = input("Повторите попытку. Введите цену товара в рублях, если в цене есть копейки, "
                              "поставьте после целочисленной части рубля точку и введите копейки без"
                              " лишних знаков: ")
            price = float(price)
            print(*shopping_list.keys())
            category = input('Выберите категорию, в которую хотите добавить товар '
                             '(напишите ее) или создайте новую категорию, '
                             'в которую хотите добавить товар (напишите ее название): ')
            if category in shopping_list: shopping_list[category][name_product]=[price, date]
            else:
                shopping_list[category]={name_product: [price, date]}

            print(f'Товар {name_product} добавлен в список покупок')

        case 2:
            answer = input("Вы уже зафиксировали даннный товар в списке покупок? Ответьте да или нет: ")
            while answer not in ['да', 'нет', 'Да', 'Нет']:
                answer = input("Ответьте на предыдущий вопрос да или нет ")
            if answer in ['да', 'Да']:
                print(*shopping_list.keys())
                category = input('Введите категорию товара, который хотите добавить в коллекцию "избранное":')
                while category not in shopping_list:
                    category = input('Данной категории нет в списке покупок. '
                                         'Введите название категории товара, который хотите добавить в коллекцию "избранное": ')
                print(*shopping_list[category].keys())
                name_product = input('Введите название товара, который хотите добавить в коллекцию "избранное":')
                while name_product not in shopping_list[category]:
                    name_product = input('Данного товара нет в списке покупок. '
                                     'Введите название товара, который хотите добавить в коллекцию "избранное": ')
                favorites[name_product] = shopping_list[category][name_product][0]
            else:
                name_product = input('Введите название товара, которое хотите добавить в коллекцию "избранное": ')
                price = input("Введите цену товара в рублях, если в цене есть копейки, "
                              "поставьте после целочисленной части рубля точку и введите копейки без"
                              " лишних знаков ")
                while not is_float(price):
                    price = input("Повторите попытку. Введите цену товара в рублях, если в цене есть копейки, "
                                  "поставьте после целочисленной части рубля точку и введите копейки без"
                                  " лишних знаков ")
                price = float(price)
                favorites[name_product] = [price]
            print(f'Товар {name_product} добавлен в коллекцию "избранное": ')
        case 3:
            print('1. Посмотреть категории товаров\n'
                  '2. Посмотреть товары конкретной категории\n'
                  '3. Посмотреть товары из всех категорий\n'
                  '4. Редактировать список товаров')

            choise2 = input('Введите номер команды, которую необходимо выполнить: ')
            while not is_int(choise2):
                choise2 = input(
                    'Номер команды был введен с ошибкой, повторите попытку. Введите номер команды, необходимо выполнить: ')
            choise2 = int(choise2)
            match choise2:
                case 1:
                    print(*shopping_list.keys())
                case 2:
                    print(*shopping_list.keys())
                    category = input('Введите категорию, товары  которой хотите посмотреть:')
                    while category not in shopping_list:
                        category = input('Данной категории нет в списке покупок. '
                                         'Введите название категории, товары которой хотите посмотреть: ')
                    answer1 = input('Выводить товары вместе с ценой?Ответьте да или нет: ')
                    while answer1 not in ['да', 'нет', 'Да', 'Нет']:
                        answer1 = input("Ответьте на предыдущий вопрос да или нет: ")
                    answer2 = input('Выводить товары вместе с датой приобретения? Ответьте да или нет: ')
                    while answer2 not in ['да', 'нет', 'Да', 'Нет']:
                        answer2 = input("Ответьте на предыдущий вопрос да или нет: ")
                    answer3 = input('Хотите ли вы, чтобы товары были отсортированы по стоимости? (Ответьте да или нет): ')
                    while answer3 not in ['да', 'нет', 'Да', 'Нет']:
                        answer3 = input("Ответьте на предыдущий вопрос да или нет: ")

                    if answer3 in ['да','Да']:
                        print('1. Отсортировать по возрастанию\n'
                              '2. Отсортировать по убыванию')
                        choise3 = input('Введите номер команды, которую необходимо выполнить: ')
                        while not is_int(choise3):
                            choise3 = input(
                                'Номер команды был введен с ошибкой, повторите попытку. Введите номер команды, которую хотите совершить: ')
                        choise3 = int(choise3)
                        match choise3:
                            case 1:
                                if answer1 in ['да', 'Да'] and answer2 in ['да','Да']:
                                    for key, value in sorted(shopping_list[category].items(),
                                                             key=lambda item: item[1][0] ):
                                        print("{0}:{1}, {2}".format(key, *value))
                                if answer1 in ['да', 'Да'] and answer2 not in ['да','Да']:
                                    for key, value in sorted(shopping_list[category].items(),
                                                             key=lambda item: item[1][0] ):
                                        print("{0}:{1}".format(key, *value))
                                if answer1 not in ['да', 'Да'] and answer2 in ['да','Да']:
                                    for key, value in sorted(shopping_list[category].items(),
                                                             key=lambda item: item[1][0] ):
                                        print("{0}:{2}".format(key, *value))
                                if answer1 not in ['да', 'Да'] and answer2 not in ['да','Да']:
                                    for key, value in sorted(shopping_list[category].items(),
                                                             key=lambda item: item[1][0] ):
                                        print(key)
                            case 2:
                                if answer1 in ['да', 'Да'] and answer2 in ['да', 'Да']:
                                    for key, value in sorted(shopping_list[category].items(),
                                                             key=lambda item: -item[1][0]):
                                        print("{0}:{1}, {2}".format(key, *value))
                                if answer1 in ['да', 'Да'] and answer2 not in ['да', 'Да']:
                                    for key, value in sorted(shopping_list[category].items(),
                                                             key=lambda item: -item[1][0]):
                                        print("{0}:{1}".format(key, *value))
                                if answer1 not in ['да', 'Да'] and answer2 in ['да', 'Да']:
                                    for key, value in sorted(shopping_list[category].items(),
                                                             key=lambda item: -item[1][0]):
                                        print("{0}:{2}".format(key, *value))
                                if answer1 not in ['да', 'Да'] and answer2 not in ['да', 'Да']:
                                    for key, value in sorted(shopping_list[category].items(),
                                                             key=lambda item: -item[1][0]):
                                        print(key)
                            case _:
                                print('Неверный выбор')
                    else:
                        if answer1 in ['да', 'Да'] and answer2 in ['да', 'Да']:
                            for key, value in shopping_list[category].items():
                                print("{0}:{1}, {2}".format(key, *value))
                        if answer1 in ['да', 'Да'] and answer2 not in ['да', 'Да']:
                            for key, value in shopping_list[category].items():
                                print("{0}:{1}".format(key, *value))
                        if answer1 not in ['да', 'Да'] and answer2 in ['да', 'Да']:
                            for key, value in shopping_list[category].items():
                                print("{0}:{2}".format(key, *value))
                        if answer1 not in ['да', 'Да'] and answer2 not in ['да', 'Да']:
                            for key, value in shopping_list[category].items():
                                print(key)
                case 3:
                    answer1 = input('Выводить товары вместе с ценой?(Ответьте да или нет: ')
                    while answer1 not in ['да', 'нет', 'Да', 'Нет']:
                        answer1 = input("Ответьте на предыдущий вопрос да или нет: ")
                    answer2 = input('Выводить товары вместе с датой приобретения?(Ответьте да или нет: ')
                    while answer2 not in ['да', 'нет', 'Да', 'Нет']:
                        answer2 = input("Ответьте на предыдущий вопрос да или нет: ")
                    answer3 = input(
                        'Хотите ли вы, чтобы товары были отсортированы по стоимости? (Ответьте да или нет): ')
                    while answer3 not in ['да', 'нет', 'Да', 'Нет']:
                        answer3 = input("Ответьте на предыдущий вопрос да или нет: ")
                    if answer3 in ['да','Да']:
                        print('1. Отсортировать по возрастанию\n'
                              '2. Отсортировать по убыванию')
                        choise4 = input('Введите номер команды, которую необходимо выполнить: ')
                        while not is_int(choise4):
                            choise4 = input(
                                'Номер команды был введен с ошибкой, повторите попытку. Введите номер команды, которую хотите совершить: ')
                        choise4 = int(choise4)
                        match choise4:
                            case 1:
                                if answer1 in ['да', 'Да'] and answer2 in ['да', 'Да']:
                                    for key, value in sorted(all_products.items(),
                                                             key=lambda item: item[1][0]):
                                        print("{0}:{1}, {2}".format(key, *value))
                                if answer1 in ['да', 'Да'] and answer2 not in ['да', 'Да']:
                                    for key, value in sorted(all_products.items(),
                                                             key=lambda item: item[1][0]):
                                        print("{0}:{1}".format(key, *value))
                                if answer1 not in ['да', 'Да'] and answer2 in ['да', 'Да']:
                                    for key, value in sorted(all_products.items(),
                                                             key=lambda item: item[1][0]):
                                        print("{0}:{2}".format(key, *value))
                                if answer1 not in ['да', 'Да'] and answer2 not in ['да', 'Да']:
                                    for key, value in sorted(all_products.items(),
                                                             key=lambda item: item[1][0]):
                                        print(key)
                            case 2:
                                if answer1 in ['да', 'Да'] and answer2 in ['да', 'Да']:
                                    for key, value in sorted(all_products.items(),
                                                             key=lambda item: -item[1][0]):
                                        print("{0}:{1}, {2}".format(key, *value))
                                if answer1 in ['да', 'Да'] and answer2 not in ['да', 'Да']:
                                    for key, value in sorted(all_products.items(),
                                                             key=lambda item: -item[1][0]):
                                        print("{0}:{1}".format(key, *value))
                                if answer1 not in ['да', 'Да'] and answer2 in ['да', 'Да']:
                                    for key, value in sorted(all_products.items(),
                                                             key=lambda item: -item[1][0]):
                                        print("{0}:{2}".format(key, *value))
                                if answer1 not in ['да', 'Да'] and answer2 not in ['да', 'Да']:
                                    for key, value in sorted(all_products.items(),
                                                             key=lambda item: -item[1][0]):
                                        print(key)
                            case _:
                                print('Неверный выбор')
                    else:
                        if answer1 in ['да', 'Да'] and answer2 in ['да', 'Да']:
                            for key, value in all_products.items():
                                print("{0}:{1}, {2}".format(key, *value))
                            if answer1 in ['да', 'Да'] and answer2 not in ['да', 'Да']:
                                for key, value in all_products.items():
                                    print("{0}:{1}".format(key, *value))
                            if answer1 not in ['да', 'Да'] and answer2 in ['да', 'Да']:
                                for key, value in all_products.items():
                                    print("{0}:{2}".format(key, *value))
                            if answer1 not in ['да', 'Да'] and answer2 not in ['да', 'Да']:
                                for key, value in all_products.items():
                                    print(key)
                case 4:
                    print('Доступные команды:\n'
                          '1. Редактировать категории товаров\n'
                          '2. Редактировать товары конкретной категории')
                    choise5 = input('Введите номер команды, которую необходимо выполнить: ')
                    while not is_int(choise5):
                        choise5 = input(
                            'Номер команды был введен с ошибкой, повторите попытку. Введите номер команды, которую хотите совершить: ')
                    choise5 = int(choise5)
                    match choise5:
                        case 1:
                            print("Категории товаров:")
                            print(shopping_list.keys())
                            print('Доступные команды:\n'
                                  '1. Добавить новую категорию товаров\n'
                                  '2. Удалить одну из категорий товаров')
                            choise6 = input('Введите номер команды, которую необходимо выполнить: ')
                            while not is_int(choise6):
                                choise6 = input(
                                    'Номер команды был введен с ошибкой, повторите попытку. Введите номер команды, которую хотите совершить: ')
                            choise6 = int(choise6)
                            match choise6:
                                case 1:
                                    name_category = input('Введите название категории которую хотите добавить: ')
                                    shopping_list[name_category]={}
                                    print(f'Категория товаров {name_category} создана')
                                case 2:
                                    print("Категории товаров:")
                                    print(*shopping_list.keys())
                                    category_remove = input('Введите название категории, которую хотите удалить: ')
                                    while category_remove not in shopping_list:
                                        category_remove = input('Данной категории товаров нет. Повторите попытку. '
                                                                'Введите название категории, которую хотите удалить: ')
                                    answer1 = input('Вы хотите перенести товары из данной категории в другую перед удалением?'
                                                    'Ответьте да или нет: ')
                                    while answer1 not in ['да', 'нет', 'Да', 'Нет']:
                                        answer1 = input("Ответьте на предыдущий вопрос да или нет: ")
                                    if answer1 in ['да','Да']:
                                        print("Категории товаров:")
                                        print(*shopping_list.keys())
                                        category_save = input(f'Введите название категории, в которую хотите сохранить товары '
                                                                f'перед удалением {category_remove}. \n'
                                                              f'Если хотите сохранить покупки в новую категорию, просто напишите ее название,'
                                                              f' она будет создана автоматически: ')
                                        while category_save==category_remove:
                                            if category_remove==category_save:
                                                category_save = input('Эта категория товаров будет удалена. Повторите попытку. '
                                                                      'Введите название категории отличной от той, которую хотите удалить, '
                                                                      'чтобы сохранить в нее товары :')

                                        shopping_list[category_save]=shopping_list[category_remove]
                                        shopping_list.pop(category_remove)
                                        print(f'Категория товаров {category_remove} удалена, товары из нее перенесены в категорию товаров {category_save}')
                                    else:
                                        shopping_list.pop(category_remove)
                                        print(f'Категория товаров {category_remove} удалена')
                        case 2:
                            print("Категории товаров:")
                            print(*shopping_list.keys())
                            name_category = input('Выберите категорию, товары которой вы хотите отредактировать: ')
                            while name_category not in shopping_list:
                                name_category = input('Введенная вами категория товаров отсутствует. '
                                                      'Выберите категорию, товары которой вы хотите отредактировать: ')
                            print(f'Товары категории {name_category}: ')
                            for key, value in shopping_list[name_category].items():
                                print("{0} :{1}, {2}".format(key, *value))
                            name_product = input('Выберите товар, информацию о котором вы хотите изменить: ')
                            while name_product not in shopping_list[name_category]:
                                name_product = input(f'Введенная вами товар отсутствует в категории {name_category}. '
                                                      'Выберите товар, который вы хотите отредактировать: ')
                            print('Доступные команды: \n'
                                  '1. Изменить название товара \n'
                                  '2. Изменить цену товара\n'
                                  '3. Изменить дату покупки товара\n'
                                  '4. Изменить категорию товара\n'
                                  '5. Удалить товар')
                            choise7 = input('Введите номер команды, которую необходимо выполнить: ')
                            while not is_int(choise7):
                                choise7 = input(
                                    'Номер команды был введен с ошибкой, повторите попытку. Введите номер команды, которую хотите совершить: ')
                            choise7 = int(choise7)
                            match choise7:
                                case 1:
                                    new_name = input('Введите измененное название товара: ')
                                    shopping_list[name_category][new_name] = shopping_list[name_category][name_product]
                                    shopping_list[name_category].pop(name_product)
                                case 2:
                                    new_price = input('Введите измененную цену товара: ')
                                    while not is_float(new_price):
                                        new_price = input(
                                            "Повторите попытку. Введите цену товара в рублях, если в цене есть копейки, "
                                            "поставьте после целочисленной части рубля точку и введите копейки без"
                                            " лишних знаков: ")
                                    new_price = float(new_price)
                                    shopping_list[name_category][name_product][0] = new_price
                                case 3:
                                    day = input('Введите измененное число, когда был приобретен товар: ')
                                    month = input('Введите измененный номер месяца, когда был приобретен товар: ')
                                    year = input('Введите измененный номер года, когда был приобретен товар: ')

                                    while not is_int(day):
                                        day = input(
                                            'Число было введено с ошибкой, повторите попытку.Введите измененное число, когда был приобретен товар: ')
                                    while not is_int(month):
                                        month = input(
                                            'Номер месяца был введен с ошибкой, повторите попытку.Введите измененный номер месяца, когда был приобретен товар: ')
                                    while not is_int(year):
                                        year = input(
                                            'Год был введен с ошибкой, повторите попытку.Введите измененный номер года, когда был приобретен товар: ')

                                    day, month, year = map(int, [day, month, year])
                                    while not is_date(day, month, year):
                                        day, month, year = map(int, input('Введенной даты не существует. Повторите попытку. '
                                                                          'Введите дату, когда был приобретен товар в формате '
                                                                          'Число. номер месяца. номер года: ').split('.'))
                                    date = datetime.date(year, month, day)
                                    shopping_list[name_category][name_product][1] = date
                                case 4:
                                    print("Категории товаров:")
                                    print(*shopping_list.keys())
                                    new_category = input('Введите название категории, в которую хотели бы сохранить товар.\n'
                                                         'Если вы хотите создать новую категорию и сохранить товар туда, так же'
                                                         ' напишите ее название: ')
                                    while new_category==name_category:
                                        new_category = input(
                                            'Название измененной категории совпадает с предыдущим.\n'
                                            'Повторите попытку. Введите название категории, в которую хотели бы сохранить товар.\n'
                                            'Если вы хотите создать новую категорию и сохранить товар туда, так же'
                                            ' напишите ее название: ')
                                    shopping_list[new_category]={}
                                    shopping_list[new_category][name_product]=shopping_list[name_category][name_product]
                                    shopping_list[name_category].pop(name_product)
                                case 5:
                                    shopping_list[name_category].pop(name_product)
                                    print(f'Товар {name_product} удален из списка товаров')
                                case _:
                                    print('Неверный выбор')
                        case _:
                            print('Неверный выбор')
        case 4:
            day = input('Введите число, когда был приобретен товар: ')
            month = input('Введите номер месяца, когда был приобретен товар: ')
            year = input('Введите номер года, когда был приобретен товар: ')

            while not is_int(day):
                day = input('Число было введено с ошибкой, повторите попытку.Введите число, когда был приобретен товар: ')
            while not is_int(month):
                month = input(
                    'Номер месяца был введен с ошибкой, повторите попытку.Введите номер месяца, когда был приобретен товар: ')
            while not is_int(year):
                year = input('Год был введен с ошибкой, повторите попытку.Введите номер года, когда был приобретен товар: ')

            day, month, year = map(int, [day, month, year])
            while not is_date(day, month, year):
                day, month, year = map(int, input('Введенной даты не существует. Повторите попытку. '
                                                  'Введите дату, когда был приобретен товар в формате '
                                                  'Число. номер месяца. номер года: ').split('.'))
            date = datetime.date(year, month, day)
            for product in all_products:
                if all_products[product][1]==date:
                    print("{0} : {1}, {2}".format(product, *all_products[product]))
        case 5:
            print('Доступные команды:\n'
                  '1. Посмотреть товары категории "избранное".\n'
                  '2. Редактировать категорию "избранное".')
            choise8 = input('Введите номер команды, которую необходимо выполнить: ')
            while not is_int(choise8):
                choise8 = input(
                    'Номер команды был введен с ошибкой, повторите попытку. Введите номер команды, которую хотите совершить: ')
            choise8 = int(choise8)
            match choise8:
                case 1:
                    answer1 = input('Выводить товары вместе с ценой?(Ответьте да или нет: ')
                    while answer1 not in ['да', 'нет', 'Да', 'Нет']:
                        answer1 = input("Ответьте на предыдущий вопрос да или нет: ")
                    answer2 = input('Выводить товары отсортировав их по стоимости?(Ответьте да или нет: ')
                    while answer2 not in ['да', 'нет', 'Да', 'Нет']:
                        answer2 = input("Ответьте на предыдущий вопрос да или нет: ")
                    if answer2 in ['да', 'Да']:
                        print('1. Отсортировать по возрастанию\n'
                              '2. Отсортировать по убыванию')
                        choise5 = input('Введите номер команды, которую необходимо выполнить: ')
                        while not is_int(choise5):
                            choise5 = input(
                                'Номер команды был введен с ошибкой, повторите попытку. Введите номер команды, которую хотите совершить: ')
                        choise5= int(choise5)
                        match choise5:
                            case 1:
                                if answer1 in ['да', 'Да'] :
                                    for key, value in sorted(favorites.items(),
                                                             key=lambda item: item[1][0]):
                                        print("{0} :{1}".format(key, value))
                                if answer1 not in ['да', 'Да']:
                                    for key in sorted(favorites.items(),
                                                             key=lambda item: item[1][0]):
                                        print(key)
                            case 2:
                                if answer1 in ['да', 'Да']:
                                    for key, value in sorted(favorites.items(),
                                                             key=lambda item: -item[1][0]):
                                        print("{0} :{1}".format(key, value))
                                if answer1 not in ['да', 'Да']:
                                    for key in sorted(favorites.items(),
                                                      key=lambda item: -item[1][0]):
                                        print(key)
                    else:
                        if answer1 in ['да', 'Да']:
                            for key, value in favorites.items():
                                print("{0} :{1}".format(key, value))
                        if answer1 not in ['да', 'Да']:
                            for key in favorites.items():
                                print(key)
                case 2:
                    print('Товары в категории "избранное": ')
                    for key, value in favorites.items():
                        print("{0} :{1}".format(key, value))
                    name_product = input('Введите название товара, параметры которого хотите изменить')
                    while name_product not in favorites:
                        name_product = input('Такого товара нет в категории "избранное".\n'
                                             'Введите название товара, параметры которого хотите изменить')
                    print('Доступные команды:\n'
                          '1. Изменить название товара\n'
                          '2. Изменить цену товара\n'
                          '3. Удалить товар из категории "избранное"')
                    choise9 = input('Введите номер команды, которую необходимо выполнить: ')
                    while not is_int(choise9):
                        choise9= input(
                            'Номер команды был введен с ошибкой, повторите попытку. Введите номер команды, которую хотите совершить: ')
                    choise9 = int(choise9)
                    match choise9:
                        case 1:
                            new_name = input('Введите новое название товара: ')
                            favorites[new_name] = favorites[name_product]
                            favorites.pop(name_product)
                        case 2:
                            new_price = input('Введите измененную цену товара: ')
                            while not is_float(new_price):
                                new_price = input(
                                    "Повторите попытку. Введите цену товара в рублях, если в цене есть копейки, "
                                    "поставьте после целочисленной части рубля точку и введите копейки без"
                                    " лишних знаков: ")
                            new_price = float(new_price)
                            favorites[name_product][0] = new_price
                        case 3:
                            favorites.pop(name_product)
                            print(f'Товар {name_product} удален из категории "избранное"')
                        case _:
                            print('Неверный выбор')
        case 6:
            print('Для завершения нажмите "Enter" ')
            input()
            break
        case _:
            print('Неверный выбор')





