#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import datetime

if __name__ == '__main__':
    # Список людей
    people = []

    # Кортеж ЗЗ
    zodiac_signs = (
        "овен",
        "телец",
        "близнецы",
        "рак",
        "лев",
        "дева",
        "весы",
        "скорпион",
        "стрелец",
        "козерог",
        "водолей",
        "рыбы"
    )

    # Организовать бесконечный цикл запроса команд.
    while True:
        # Запросить команду из терминала.
        # На Python с помощью ANSI-код можно делать цвет, фон и т.д.
        # \033[0m - сброс форматирования
        command = input("\033[0mEnter command: ").lower()

        # Выполнить действие в соответствие с командой.
        if command == 'exit':
            break

        # Добавить нового человека
        elif command == 'add':
            # Запросить данные человека
            name = input("Enter name: ")
            # Проверка ЗЗ
            while True:
                zodiac_sign = input("\033[0mEnter zodiac sign: ").lower()
                if zodiac_sign not in zodiac_signs:
                    print("\033[31mIncorrect zodiac sign")
                else:
                    break
            # Проверка Даты Рождения
            while True:
                birth = input("\033[0mEnter date of birth (yyyy.mm.dd): ")
                # Обработка исключения (проверка правильности даты)
                try:
                    datetime.datetime.strptime(birth, '%Y.%m.%d')
                except Exception:
                    print("\033[31mIncorrect data format")
                else:
                    break

            # Создать словарь
            human = {
                'name': name,
                'zodiac_sign': zodiac_sign,
                'birth': birth,
            }

            # Добавить словарь в список.
            people.append(human)

            # Отсортировать список в случае необходимости.
            if len(people) > 1:
                people.sort(key=lambda item: item.get('birth', ''))

        elif command == 'show':
            # Заголовок таблицы.
            line = (f'{"+" + "-" * 12 + "+" + "-" * 12 + "+"}'
                    f'{"-" * 15 + "+"}')
            print(line)
            print(f"|{'Name' :^12}|{'Birth ' :^12}|{'Zodiac_sign ' :^15}|")
            print(line)

            # Вывести данные о всех людях.
            for idx, human in enumerate(people):
                print(
                    f'|{human.get("name", "") :^12}'
                    f'|{human.get("birth", "") :^12}'
                    f'|{human.get("zodiac_sign", "") :^15}|'
                )
                print(line)

        # .startswith - Поиск строк с заданным началом строки
        elif command.startswith('select'):
            # Разбить команду на части для выделения номера года.
            # Параметр maxsplit - int, сколько раз делить строку.
            while True:
                parts = command.split(' ', maxsplit=1)
                if len(parts) == 1:
                    command = input("\033[31mEnter command "
                                    "select and Zodiac_sign: ").lower()
                    # Получить требуемый ЗЗ.
                else:
                    break

            # Инициализировать счетчик.
            count = 0
            zz = parts[1]
            # Заголовок таблицы.
            line = (f'\033[0m{"+" + "-" * 12 + "+" + "-" * 12 + "+"}'
                    f'{"-" * 15 + "+"}')
            print(line)
            print(
                f"|{'Name' :^12}|{'Birth ' :^12}"
                f"|{'Zodiac_sign ' :^15}|"
            )
            print(line)
            # Таблица с людьми
            for p in people:
                if zz == p.get('zodiac_sign'):
                    count += 1
                    print(
                        f'|{p.get("name", "") :^12}|'
                        f'{p.get("birth", "") :^12}|'
                        f'{p.get("zodiac_sign", "") :^15}|'
                    )
                    print(line)

            # Если счетчик равен 0, то люди не найдены.
            if count == 0:
                print("Люди с заданным ЗЗ не найдены")

        # Список команд с описанием
        elif command == 'help':
            # Вывести справку о работе с программой.
            print("\033[32mСписок команд:\n")
            print("add - добавить человека;")
            print("select <ЗЗ> - запросить людей с определенным ЗЗ;")
            print("show - показать список людей;")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")

        # Неопознанная команда
        else:
            print("\033[31mUnknown command")
