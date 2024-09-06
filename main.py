def read_cook_book():
    with open('recipes.txt', encoding='UTF-8') as f:
        receipt_list = []
        receipt = []
        for line in f:
            data = line.strip()
            if data != '':
                receipt.append(data)
            else:
                receipt_list.append(receipt)
                receipt = []
        receipt_list.append(receipt)
    cook_book = {}
    for rec in receipt_list:
        ingridients = []
        for ingridient in rec[2:]:
            ingridient = ingridient.split(' | ')
            ingridients.append({'ingredient_name': ingridient[0], 'quantity': int(ingridient[1]), 'measure': ingridient[2]})
        cook_book[rec[0]] = ingridients
    return cook_book


def get_shop_list_by_dishes(dishes: list, person_count: int):
    cook_book = read_cook_book()
    shop_list = {}
    for dish in dishes:
        for ingr in cook_book[dish]:
            if ingr['ingredient_name'] in shop_list:
                shop_list[ingr['ingredient_name']]['quantity'] = shop_list[ingr['ingredient_name']]['quantity'] + ingr['quantity'] * person_count
            else:
                shop_list[ingr['ingredient_name']] = {'measure': ingr['measure'], 'quantity': ingr['quantity'] * person_count}
    return shop_list


def merge_files(file_list: list):
    file_dict = {}
    for file in file_list:
        with open(file, encoding='UTF-8') as f:
            data = []
            for line in f:
                data.append(line.strip())
            file_dict[file] = data
    sort_dict = dict(sorted(file_dict.items(), key=lambda item: len(item[1])))
    with open('result.txt', 'w', encoding='UTF-8') as f:
        for key, value in sort_dict.items():
            data = key + '\n' + str(len(value)) + '\n' + '\n'.join(value) + '\n'
            f.write(data)


print(read_cook_book())
print(get_shop_list_by_dishes(['Омлет', 'Фахитос'], 2))
merge_files(['1.txt', '2.txt', '3.txt'])

