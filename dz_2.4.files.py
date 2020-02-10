from pprint import pprint


# Задача №1
def create_cook_book(input_file_name):
    cook_book = {}

    try:
        # читаем файл. разбиваем на строки. записываем строки в список lst для более удобной работы
        with open(input_file_name, encoding='utf-8') as f:
            lst = [line.strip() for line in f]

        # тут долго ломал голову как лучше начать и взять название блюда... ничего лучше в голову не пришло...
        for i, c in enumerate(lst):
            if c.isdigit():
                # если элемент == цифра ==> берем название блюда из предшествующего элемента
                cook_book[lst[i-1]] = []

                # собираем ингридиенты в срезе с индекса после кол-ва ингр-ов до : индекс + кол-во ингр-ов + 1
                for slice in lst[i+1:i+int(c)+1]:
                    ingredient_name = slice.split('|')[0]
                    quantity = int(slice.split('|')[1])
                    measure = slice.split('|')[2]

                    cook_book[lst[i-1]].append({'ingredient_name':ingredient_name,
                                                'quantity':quantity,
                                                'measure':measure})
        return cook_book

    except FileNotFoundError:
        return(f'Файл: {input_file_name} не найден.')
    except Exception as error:
        return f'Ошибка - {error}'


# Задача №2
# в качестве второго аргумента решил передавать результат работы функции
def get_shop_list_by_dishes(dishes, cooking_book, person_count):
    ing_dict = {}

    for key in cooking_book.keys():
        for dish in dishes:
            if key == dish:
                for dictionary in cooking_book[key]:
                    # пробежимся по ключам словаря
                    for k in dictionary:
                        if k == 'ingredient_name':
                            ing_dict[dictionary[k]] = {'measure': dictionary['measure'],
                                                       'quantity': dictionary['quantity'] * person_count}

    return ing_dict


#####################################
# ВЫВОД
# Задача №1
print('Задача №1:\n')
pprint(create_cook_book('recipes.txt'))
print('\n' * 3)


# Задача №2
print('Задача №2:\n')
pprint(get_shop_list_by_dishes(['Омлет', 'Омлет'], create_cook_book('recipes.txt'), 5))