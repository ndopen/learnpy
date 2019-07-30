# name =''
# while not name or name.isspace():
#     name = input('please enter your name:')
# print('hello {}'.format(name))

# language = ['zh', 'en', 'de', 'jp']
# for lang in language:
#     print(lang)

# d = {'x':1, 'y':2, 'z':3}
# for key in d:
#     print(key, 'vlues', d[key])

# for value in d.values():
#     print(value)

# for key, value in d.items():
#     print(key,value)

# name = ['cock', 'zhangsan', 'lisi', 'cock']
# age = [23, 19, 48]

# names = list(zip(name,age))

# for index, string in enumerate(names):
#     if 'cock' in string:
#         # names[index] = '[censored]'
#         print(names[index], index)

# s = ['E', 'c', 'D', 'A']
# d = {'d':2, 'c':7, 'i':0}
# print(' '.join(reversed('Hello,String')))
# print(sorted(s, key=str.lower))
# print(list(reversed(s)))

from math import sqrt

for n in range(99, 0, -1):
    root = sqrt(n)
    if root == int(root):
        print(n)
        break
