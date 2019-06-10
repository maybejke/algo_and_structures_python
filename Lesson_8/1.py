"""
1. Закодируйте любую строку из трех слов по алгоритму Хаффмана.
"""


############ попытался разобраться в этом чуде, пока мне кажется это каким-то космическим приемом. И кстати не
# работает count почему у мен, но не суть.
# from collections import Counter, deque
#
#
# def haffman_tree(s):
#     sorted_elems = deque(sorted(count.items(), key=lambda item: item[1]))
#     if len(sorted_elems):
#         while len(sorted_elems) > 1:
#             weight = sorted_elems[0][1] + sorted_elems[1][1]
#             comb = {0: sorted_elems.popleft()[0],
#                     1: sorted_elems.popleft()[0]}
#             for i, _count in enumerate(sorted_elems):
#                 if weight > _count[1]:
#                     continue
#                 else:
#                     sorted_elems.insert(i, (comb, weight))
#             else:
#                 sorted_elems.append((comb, weight))
#     else:
#         weight = sorted_elems[0][1]
#         comb = {0: sorted_elems.popleft()[0], 1: None}
#         sorted_elems.append((comb, weight))
#     return sorted_elems[0][0]
#
# code_table = dict()
#
# def haffman_code(tree, path=''):
#     if not isinstance(tree, dict):
#         code_table[tree] = path
#     else:
#         haffman_code(tree[0], path=f'{path}0')
#         haffman_code(tree[1], path=f'{path}1')
#
# s = "beep boop beer!"
#
# haffman_code(haffman_tree(s))
#
# for i in s:
#     print(code_table[i], end=' ')
# print()

string = "beep boop beer!"
print("Исходная строка: " + string)

class Node:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def children(self):
        return self.left, self.right


def make_haffman_tree(node, code=""):
    if type(node) is str:
        return {
            node: code
        }

    l, r = node.children()

    result = {}

    result.update(make_haffman_tree(l, code + "0"))
    result.update(make_haffman_tree(r, code + "1"))

    return result

frequencies = {}
for char in string:
    if char not in frequencies:
        frequencies[char] = 0
    frequencies[char] += 1

tree = frequencies.items()

while len(tree) > 1:
    tree = sorted(tree, reverse=True, key=lambda x: x[1])
    char1, count1 = tree[-1]
    char2, count2 = tree[-2]
    tree = tree[:-2]
    tree.append(
        (Node(char1, char2), count1 + count2)
    )

code_table = make_haffman_tree(tree[0][0])

coded = []
for char in string:
    coded.append(code_table[char])

print(coded)

"""
# Большое пожелание на будующие курсы - все-таки такие задания писать прямо на уроке.
# Потому что возможно я и понимаю приблизительно что здесь происходит, но это проблематично и  четкого понмиаю как писать
# код в данной ситуации у меня нет. Как хаффман работает я вспомнил благодаря вашим лекциям спасибо. 
Как это реализовано на питоне - сомневаюсь.
"""