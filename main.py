def division(num1, num2):
    return num1 / num2


# измененный метод
def divisionModified(num1, num2):

    if type(num1) not in [int, float] or type(num2) not in [int, float]:
        return "Error: Type Error"
    if num2 == 0:
        return "Error: Division zero"
    else:
        return num1 / num2


# получить элемент списка
def getItem(items, index):
    return items[index]


# list1 = [5, 6, 2]
# result = getItem(list1, 1)
# print(result)


# стандартное тестирование
def test1():
    print(division(8, 2))
    print(division(2, 0))
    print("OK")


# test1()


def test2():
    assert divisionModified(8, 2) == 4
    assert divisionModified(8.8, 2) == 4.4
    assert divisionModified("Число", 2) == "Error: Type Error"
    assert divisionModified(2, 0) == "Error: Division zero"
    print("OK")


# test2()


def standart_test():
    num_list = [
        (2, 2), (4, 2), (-3, 2), (2, 0), (True, 4), (5, "")
    ]

    for num1, num2 in num_list:
        result = division(num1, num2)
        textResult = f'Деление {num1} / {num2} = {result}'
        print(textResult)
