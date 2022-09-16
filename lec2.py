# with open('file.txt', 'a') as data:
#     data.write('line 1\n')
#     data.write('line 2\n')





# colors = ['red', 'green', 'blue123\n']
# data = open('file.txt', 'a')
# data.writelines(colors) #разделителей не будет
# data.write('LINE 2\n')
# data.write('LINE 3\n')
# data.close()



# path = 'file.txt'
# data = open(path, 'r')
# for line in data:
#     print(line)
# data.close()

# exit()

# Функции

# import lec as l #использовали функцию из соседнего файла
# print(l.f(1))
#-----------

# def new_string(symbol, count = 3):
#     return symbol * count

# print(new_string('!', 5)) #!!!!!
# print(new_string('!')) #!!!
# print(new_string(4)) #12
#------------

# def concatinatio(*params):
#     res: str = "" # для работы с числами необходимо поменять на int
#     for item in params:
#         res += item
#     return res

# print(concatinatio('a', 's', 'd', 'w')) # asdw
# print(concatinatio('a', '1')) # a1
# print(concatinatio(1, 2, 3, 4)) # TypeError:
#-------------

# Рекурсия

# def fib(n):
#     if n in [1, 2]:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)

# list = []
# for e in range(1, 10):
#     list.append(fib(e))
# print(list) # 1 1 2 3 5 8 13 21 34
# ---------------

# Кортеж - это не изменяемый "список"

# a = (3, 4, 32, 2)
# # print(a)
# # print(a[-1])

# for item in a:
#     print(item)
#-----------------

# Словари

# dictionary = {}
# dictionary = \
#     {
#         'up': 'u',
#         'left': 'l',
#         'down': 'd',
#         'rigth': 'r'
#     }

# print(dictionary)
# print(dictionary['left'])

# for v in dictionary: #или keys()
#     print(dictionary[v])
#--------------

# Множества

# colors = {'red', 'green', 'blue'}

# print(colors)
# colors.add('red')
# print(colors)
# colors.add('grey')
# print(colors)
# colors.remove('red')
# print(colors)
# colors.discard('red')
# print(colors)
# colors.clear()
# print(colors)
#-------------------

# a = {1, 2, 3, 5, 8}
# b = {2, 5, 8, 13, 21}
# c = a.copy()
# u = a.union(b)
# i = a.intersection(b)
# dl = a.difference(b)
# dr = b.difference(a)

# q = a \
#     .union(b) \
#     .difference(a. intersection(b))

# s = frozenset(a) #не изменяемые множества

# Списки --------------------

# list1 = [1, 2, 4, 5, 5]
# list2 = list1

# for e in list1:
#     print(e)

# print()

# for e in list2:
#     print(e)

# print()

list1 = [1, 2, 3, 6, 7]

# print(len(list1))
# print(list1.pop()) # pop() удаляет елемент
# print(list1)
# print(list1.pop())
# print(list1)
# print(list1.pop())
# print(list1)
# print(list1.pop())

# print(list1.insert(2, 11)) # insert(куда, что) добавляет елемент
# print(list1)

print(list1.append(11)) # append() добавляет елемент в конец
print(list1)
