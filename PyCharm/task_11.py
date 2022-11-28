#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    # Создать словарь.
    dict = {
        0: "cat",
        1: "dog",
        2: "rat",
        3: "humster",
        4: "parrot",
        5: "fish"
    }
    # Создать новый пустой словарь.
    dict_new = {}

    # Применения метода items()
    dict_items = dict.items()

    # Создание обратного словаря
    for k, v in dict_items:
        dict_new[v] = k

    print(dict)
    print(dict_new)
