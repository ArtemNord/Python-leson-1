# Ускоренная обработка данных:
# lambda, filter, map, zip, enumerate, List, Comprehension

# lambda

# def f(x):
#     x ** 2

# g = f
# print(f(1))
# print(g(1))

# def f(x):
#     return x ** 2

# g = f

# print(type(f))
# print(type(g))

# print(f(4))
# print(g(4))


# def calc1(x):
#     return x + 10

# # print(calc1(10))

# def calc2(x):
#     return x * 10

# # print(calc2(10))

# def math(op, x):
#     print(op(x))

# math(calc1, 10)


# def sum(x, y):
#     return x + y



# def mylt(x, y):
#     return x * y

# def calc(op, a, b):
#     print(op(a, b))
#     # return op(a, b)

# calc(lambda x, y: x + y, 4, 5)


# List Comprehension

# list = []

# for i in range(1, 101):
#     # if(i % 2 == 0):
#         list.append(i);

# print(list)

# def f(x):
#     return x ** 3

# list = [(i, f(i)) for i in range(1, 21) if i % 2 == 0]

# print(list)
#----------------------------------------------------------

# file = (1, 2, 3, 5, 8, 15, 23, 38)

# def f(x):
#     return x ** 2

# list = [(i, f(i)) for i in file if i % 2 == 0]

# print(list)

# path = '/GB/II chetvert/Python/Python-leson-1/file.txt'
# f = open(path, 'r')
# data = f.read() + ' '
# f.close()

# numbers = []

# while data != '':
#     space_pos = data.index(' ')
#     numbers.append(int(data[:space_pos]))
#     data = data[space_pos + 1:]

# out = []
# for e in numbers:
#     if not e % 2:
#         out.append((e, e ** 2))
# print(out)


# data = '1 2 3 5 8 15 23 38'. split()

# res = map(int, data)
# res = filter(lambda x: not x % 2, res)
# res = list(map(lambda x: (x, x ** 2), res))
# print(res)


# map

# li = [x for x in range(1, 21)]

# li = list(map(lambda x: x + 10, li))

# print(li)


# data = list(map(int, input().split()))
# print(data)


# data = list(map(int, '1 2 3'.split()))

# for e in data:
#     print(e)

# print('--')

# for e in data:
#     print(e)


# filter() - функция

# data = [x for x in range(10)]

# res = list(filter(lambda x: not x % 2 == 0, data))
# print(res)


# zip() - функция

# users = ['user1', 'user2', 'user3', 'user4', 'user5']
# ids = [4, 5, 9, 14, 7]
# salary =[111, 222, 333]

# data = list(zip(users, ids, salary))
# print(data)

# enumerate() - функция

# users = ['user1', 'user2', 'user3', 'user4', 'user5']
# ids = [4, 5, 9, 14, 7]
# salary =[111, 222, 333]

# data = list(enumerate(users))
# print(data)