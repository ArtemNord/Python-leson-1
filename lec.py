from xmlrpc.client import boolean


# print('Hello World')
# int
# float
# boolean
# str
# list
# None

# value = None
# a = 123
# b = 1.23
# # print (type(a))
# # print (type(b))
# value = 12334
# # print (type(value))
# s = 'hello world'

# print (s) # вывод строки
# print (a, ' - ' ,b, ' - ',s)
# print ('{1} - {2} - {0}'.format (a, b, s))
# print (f'{a} - {b} - {s}')

# f = False
# print(f)

# list = ['1', '2', '3', 'hello']
# print(list)

# Ввод и вывод данных
# print(), input()

# print ('Введите а');
# a = int (input())
# print ('Введите b');
# b = int (input())
# print (a, '+', b, '=', a+b)
# # print ('{} {}'.format(a, b))
# # print (f'{a} {b}')

# Арифметические операции
# a = 1.3123
# b = 3
# c = round(a * b, 5)
# print (c)

# Сокращенная операция присваивания
# a = 3
# a += 5
# print (a)

# Логические операции
# Можно генирировать тройные неравенства
# func = 1
# T = 4
# x = 123
# print(func<T>(x))

# f = [1,2,3,4]
# print (f)
# print (not 2 in f) # 2ки нет в массиве f (это не правда, поэтому получаем false)

# is_odd = not f[0] % 2
# print (is_odd)

# Управляющие конструкции
# if, if-else

# a = int (input('a = '))
# b = int (input('b = '))
# if a > b:
#     print(a)
# else:
#     print(b)

# username = input ('Введите имя: ')
# if username == 'Наташа':
#     print ('Ура, это же Наташа!')
# elif username == 'Марина':
#     print ('Я так ждал Вас, Марина!')
# elif username == 'Артем':
#     print ('Артем - ЛУЧШИЙ!!!')
# else:
#     print ('Привет, ', username)

# while & for
# original = 23
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
# else:
#     print('Пожалуй')
#     print('хватит )')
# print(inverted)

# for i in 'qwe - rty':
#     print (i)

# text = 'Шарлотка в этот раз удалась'

# print (text [0])
# print (text [1])
# # print (text [len(text)])
# print (text [len(text)-1])
# print (text [-5])
# print (text [:])
# print (text [0:2])
# print (text [len(text)-2:])
# print (text [2:9])
# print (text [6:-18])
# print (text [0:len(text):6])
# print (text [::6])
# text = text[2:9] + text[-5] + text[:2]

# numbers = [1,2,3,4,5]
# print(numbers)
# ran = range(1,6)
# print(type(ran))
# numbers = list(ran)
# print (type(numbers))

# print(numbers)
# numbers[0] = 10
# print(f'{len(numbers)} len')
# print(numbers)
# for i in numbers:
#     i *= 2
#     print(i)
# print(numbers)

# colors = ['red', 'green', 'blue']

# for e in colors:
#     print(e) # red green blue

# for e in colors:
#     print(e*2) #redred greengreen blueblue

# colors.append('gray') #добавить в конец
# print(colors == ['red', 'green', 'blue', 'gray']) # True
# colors.remove('red') #del colors[0] # удалить элемент
# print(colors)

def f(x):
    if x == 1:
        return 'Целое'
    elif x == 2.3:
        return 23
    else:
        return

arg = 2
print(f(arg))
print(type(f(arg)))