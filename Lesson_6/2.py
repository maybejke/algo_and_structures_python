"""
2. Создать пользовательский класс данных (или использовать) один из классов,
реализованных в курсе Python.Основы. Реализовать класс с применением слотов
и обычным способом. Для объекта обычного класса проверить отображение словаря
атрибутов. Сравнить, сколько выделяется памяти для хранения атрибутов обоих
классов.
"""

from pympler.asizeof import asizeof


class Class1:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname


class Class2:
    __slots__ = ['name', 'surname']

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname


a = Class1('Alexey', 'Rakitin')
b = Class2('Alexey', 'Rakitin')

print(a.__dict__)
print(b.__slots__)
print(asizeof(a))
print(asizeof(b))

# 392 используя слотс памятив  2 раза меньше.
# 168