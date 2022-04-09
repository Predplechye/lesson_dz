"""
Реализовать вывод информации о промежутке времени в зависимости от его
продолжительности duration в секундах:
a. до минуты: <s> сек;
b. до часа: <m> мин <s> сек;
c. до суток: <h> час <m> мин <s> сек;
d. * в остальных случаях: <d> дн <h> час <m> мин <s> сек.
"""


def naive_realisation(duration: int):
    total_time = ''
    """
    Решение задачи БЕЗ использования циклов.
    Переменная total_time - строковая переменная,
    содержащая в себе промежуток времени в нужно формате
    """

    time = int(input('Enter the time: '))
    second = time % 60
    minute = time // 60 % 60
    hour = time // 3600
    # day не понимаю, как вычислить дни
    print(f'{hour} час {minute} мин {second} сек')

    return total_time


def one_cycle_realisation(duration):
    total_time = ''
    """
    Решение задачи с использования циклов.
    Можно два, но высший пилотаж через 1 цикл.
    Переменная total_time - строковая переменная,
    содержащая в себе промежуток времени в нужно формате
    """
    # В этом решении не могу понять, как выйти из цикла и собрать результаты воедино
    time = int(input('Enter the time: '))

    while time > 0:
        if time % 60:
            print(time, 'сек')
        elif time // 60 % 60:
            print(time, 'мин')
        elif time // 3600:
            print(time, 'час')
        else:
            print('Не правильно')
    return total_time


if __name__ == '__main__':
    duration = 628
    print(naive_realisation(duration))
    print(one_cycle_realisation(duration))
