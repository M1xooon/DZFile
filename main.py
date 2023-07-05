def get_cooking_book():
    with open('recipes.txt', encoding="utf-8") as file_to_read:
        while True:
            recipe_name = file_to_read.readline().strip()
            if recipe_name.strip() == '':
                break
            number_of_ingredients = int(file_to_read.readline().strip())
            list_of_ingredients = []
            for i in range(number_of_ingredients):
                ingredient = file_to_read.readline().strip().split(' | ')
                ingredients = {'ingredient_name': ingredient[0], 'quantity': int(ingredient[1]),
                               'measure': ingredient[2]}
                list_of_ingredients.append(ingredients)
            cook_book.update({recipe_name: list_of_ingredients})


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for ingredient in cook_book[dish]:
            new_shop_list_item = dict(ingredient)
            new_shop_list_item['quantity'] *= person_count
            if new_shop_list_item['ingredient_name'] in shop_list:
                shop_list[new_shop_list_item['ingredient_name']]['quantity'] += new_shop_list_item['quantity']
            else:
                shop_list[new_shop_list_item['ingredient_name']] = new_shop_list_item
    return shop_list


def print_shop_list(shop_list):
    for shop_list_item in shop_list.values():
        print('{}: {} {}'.format(shop_list_item['ingredient_name'],
                                 shop_list_item['quantity'],
                                 shop_list_item['measure']))


def create_shop_list():
    person_count = int(input('Введите количество человек: '))
    dishies = input('Введите блюда: ').title().split(', ')
    shop_list = get_shop_list_by_dishes(dishies, person_count)
    print_shop_list(shop_list)

def rewrite_file():
    with open('1.txt', encoding="utf-8") as file_to_read:
        data1 = file_to_read.readlines()
    with open('2.txt', encoding="utf-8") as file_to_read:
        data2 = file_to_read.readlines()
    with open('3.txt', encoding="utf-8") as file_to_read:
        data3 = file_to_read.readlines()
    with open('final_file.txt', 'w', encoding="utf-8") as file_to_write:
        if len(data1)<=len(data2) and len(data1)<=len(data3):
            file_to_write.write('1.txt'+'\n')
            file_to_write.write(str(len(data1))+'\n')
            file_to_write.writelines(data1)
            file_to_write.write('\n')
            if len(data2)<=len(data3):
                file_to_write.write('2.txt' + '\n')
                file_to_write.write(str(len(data2)) + '\n')
                file_to_write.writelines(data2)
                file_to_write.write('\n')
                file_to_write.write('3.txt' + '\n')
                file_to_write.write(str(len(data3)) + '\n')
                file_to_write.writelines(data3)
                file_to_write.write('\n')
            else:
                file_to_write.write('3.txt' + '\n')
                file_to_write.write(str(len(data3)) + '\n')
                file_to_write.writelines(data3)
                file_to_write.write('\n')
                file_to_write.write('2.txt' + '\n')
                file_to_write.write(str(len(data2)) + '\n')
                file_to_write.writelines(data2)
                file_to_write.write('\n')

        elif len(data2)<=len(data3) and len(data2)<=len(data1):
            file_to_write.write('2.txt' + '\n')
            file_to_write.write(str(len(data2)) + '\n')
            file_to_write.writelines(data2)
            file_to_write.write('\n')
            if len(data1) <= len(data3):
                file_to_write.write('1.txt' + '\n')
                file_to_write.write(str(len(data1)) + '\n')
                file_to_write.writelines(data1)
                file_to_write.write('\n')
                file_to_write.write('3.txt' + '\n')
                file_to_write.write(str(len(data3)) + '\n')
                file_to_write.writelines(data3)
                file_to_write.write('\n')
            else:
                file_to_write.write('3.txt' + '\n')
                file_to_write.write(str(len(data3)) + '\n')
                file_to_write.writelines(data3)
                file_to_write.write('\n')
                file_to_write.write('1.txt' + '\n')
                file_to_write.write(str(len(data1)) + '\n')
                file_to_write.writelines(data1)
                file_to_write.write('\n')

        else:
            file_to_write.write('3.txt' + '\n')
            file_to_write.write(str(len(data3)) + '\n')
            file_to_write.writelines(data3)
            file_to_write.write('\n')
            if len(data1) <= len(data2):
                file_to_write.write('1.txt' + '\n')
                file_to_write.write(str(len(data1)) + '\n')
                file_to_write.writelines(data1)
                file_to_write.write('\n')
                file_to_write.write('2.txt' + '\n')
                file_to_write.write(str(len(data2)) + '\n')
                file_to_write.writelines(data2)
                file_to_write.write('\n')
            else:
                file_to_write.write('2.txt' + '\n')
                file_to_write.write(str(len(data2)) + '\n')
                file_to_write.writelines(data2)
                file_to_write.write('\n')
                file_to_write.write('1.txt' + '\n')
                file_to_write.write(str(len(data1)) + '\n')
                file_to_write.writelines(data1)
                file_to_write.write('\n')


cook_book = {}
get_cooking_book()
create_shop_list()
rewrite_file()

