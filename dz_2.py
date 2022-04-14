'''
def sum_list_1(dataset: list) -> int:
    """Вычисляет сумму чисел списка dataset, сумма цифр которых делится нацело на 7"""
    i = 1
    while i < 1001:
        a = i ** 3
        razbivka = sum([int(b) for b in str(a)])
        nechetak7 = razbivka % 7
        if nechetak7 == 0:
            dataset.append(a)
            i += 2
        else:
            i += 2
            continue

    return dataset


def sum_list_2(dataset: list) -> int:
    list2 = []
    for number in dataset:
        sum17 = number + 17
        razbivka = sum([int(b) for b in str(sum17)])
        nechetak17 = razbivka % 7
        if nechetak17 == 0:
            list2.append(sum17)

    return list2 # Верните значение полученной суммы


if __name__ == '__main__':
    my_list = []  # Соберите нужный список по заданию
    result_1 = sum_list_1(my_list)
    print(result_1)
    result_2 = sum_list_2(my_list)
    print(result_2)
'''
# 2. Создать список, состоящий из кубов нечётных чисел от 1 до 1000 (куб X - третья степень числа X):
# Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7. Например, число «19 ^ 3 = 6859»
# будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7. Внимание: использовать только
# арифметические операции!
# К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка, сумма цифр
# которых делится нацело на 7.
# * Решить задачу под пунктом b, не создавая новый список.

