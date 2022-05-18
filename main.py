from pprint import pprint as p

name_list = ['ingredient_name', 'quantity', 'measure']


def read_recipe(path):
    with open(path, encoding='utf-8') as f:
        # Reading file
        cook_book = {}
        for row in f:
            cook_book[row.strip()] = []
            how_many_ingredients = f.readline()
            for i in range(int(how_many_ingredients)):
                ingredient_row = f.readline().strip().split(' | ')
                zip_ = {}
                for y, z in zip(name_list, ingredient_row):
                    zip_[y] = z
                cook_book[row.strip()].append(zip_)
            f.readline()
        return cook_book


def get_shop_list_by_dishes(dishes, person_count, path):
    # Create shopping list
    cook_book = read_recipe(path)
    shopping_list = {}
    for dish in dishes:
        for j in cook_book[dish]:
            if j[name_list[0]] in shopping_list.keys():
                quantity = int(shopping_list[j[name_list[0]]][name_list[1]]) + int(j[name_list[1]]) * person_count
                shopping_list[j[name_list[0]]] = {name_list[2]: j[name_list[2]], name_list[1]: quantity}
            else:
                quantity = int(j[name_list[1]]) * person_count
                shopping_list[j[name_list[0]]] = {name_list[2]: j[name_list[2]], name_list[1]: quantity}
    p(shopping_list, sort_dicts=False)


get_shop_list_by_dishes(['Омлет', 'Омлет', 'Запеченный картофель', 'Утка по-пекински', 'Фахитос', 'Запеченный картофель'], 17, 'recipes.txt')


file_list = ['1.txt', '2.txt', '3.txt']


def merging_file():
    # Merging file from file_list in result.txt
    row_in_file = {}
    for file in file_list:
        lines = 0
        with open(file, encoding='utf-8') as f:
            for line in f:
                lines += 1
            row_in_file[file] = lines
    sorted_dict = {}
    sorted_keys = sorted(row_in_file, key=row_in_file.get)
    for i in sorted_keys:
        sorted_dict[i] = row_in_file[i]
    with open('result.txt', 'w', encoding='utf-8') as f:
        for i, j in sorted_dict.items():
            with open(i, encoding='utf-8') as source:
                f.write(i + '\n' + str(j) + '\n')
                for k in source:
                    f.write(k)
                f.write('\n')


merging_file()
