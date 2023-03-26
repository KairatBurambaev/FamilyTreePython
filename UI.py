import json
from Person import Person

class Ui:
    def command_msg(tree):
        print('Вывести дерево введите 1')
        print('Найти человека введите 2')
        print('Добавить человека введите 3')
        print('Закончить работу c деревом введите 4')

        num = int(input('Введите номер действия: '))

        match num:
            case 1:
                print('\n',tree.as_dict(),'\n')
                Ui.command_msg(tree)
            case 2:
                name = str(input('Введите имя человека: '))
                for root in tree.as_dict()['roots']:
                    if root['name'] == name:
                        msg = '\n' + 'Имя: ' + root['name'] + ' ' + str(root['birth_year']) +'\n'
                        for child in root['children']:
                            if len(root['children']) > 0:
                                msg += 'Ребёнок: ' + child['name'] + ' ' + str(child['birth_year']) + '\n'
                print(msg)
                Ui.command_msg(tree)    
            case 3:
                new_person_name = str(input('Введите имя: '))
                new_person_birth_year = int(input('Введите год рождения: '))
                new_person_name = Person(new_person_name, new_person_birth_year)
                tree.add_person(new_person_name)
                with open('family_tree.json', 'w') as file:
                    json.dump(tree.as_dict(), file)
                print('\n')
                Ui.command_msg(tree)

            case 4:
                print('Досвидание!')
                exit()