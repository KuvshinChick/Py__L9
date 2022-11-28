#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    # Создать словарь.
    school = {
        '1А': 13,
        '1Б': 18,
        # '1В': 5,
        '2А': 18,
        '2Б': 19,
        # '3А': 22,
        # '3Б': 11,
        # '4А': 22,
    }

    # Организовать бесконечный цикл запроса команд.
    while True:
        # Запросить команду из терминала.
        # На Python с помощью ANSI-код можно делать цвет, фон и т.д.
        # \033[0m - сброс форматирования
        command = input("\033[0mEnter command: ").lower()

        # Выполнить действие в соответствие с командой.
        if command == 'exit':
            break

        # Добавить новый класс
        elif command == 'add':
            while True:
                class_name = input("Enter class: ")
                if class_name in school:
                    print(f"\033[31m{f'Класс {class_name} уже существует'}")
                else:
                    class_num = int(input("Enter number of pupils: "))
                    school[class_name] = class_num
                    break

            # Сортировка по ключу
            school = dict(sorted(school.items()))

        # Показать все классы
        elif command == 'show':
            # Заголовок таблицы.
            line = f'{"+" + "-"*7 + "+" + "-"*32 + "+"}'
            print(line)
            print(f"|{'Class' :^7}|{'Number of pupils ' :^32}|")
            print(line)

            # Вывести данные о всех классах.
            for k, v in school.items():
                print(f'|{k :^7}|{v :^32}|')
            print(line)

        # Изменить число учеников в классе
        elif command == 'change':
            while True:
                class_name = input("\033[0mEnter class: ")
                if class_name in school:
                    class_num = int(input("Enter number of pupils: "))
                    school[class_name] = class_num
                    break
                else:
                    print(f"\033[31m{f'Класс {class_name} не найден'}")

        # Удалить класс
        elif command == 'remove':
            while True:
                class_name = input("\033[0mEnter class: ")
                if class_name in school:
                    del school[class_name]
                    break
                else:
                    # \033[31m - 31m - управляющий цветом(красный) код
                    print(f"\033[31m{f'Класс {class_name} не найден'}")

        # Кол-во учеников в школе
        elif command == 'sum':
            for k, v in school.items():
                # Проссумировать значения словаря
                s = sum(school.values())
            print(f"Общее кол-во учеников в школе: {s}")

        # Список команд с описанием
        elif command == 'help':
            # Вывести справку о работе с программой.
            print("Список команд:\n")
            print("change - изменить число обучающихся;")
            print("add - добавить новый класс;")
            print("remove - расформировать класс;")
            print("sum - общее кол-во учащихся;")
            print("show - показать список классов;")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")

        # Неопознанная команда
        else:
            print("\033[31mНеизвестная команда")
