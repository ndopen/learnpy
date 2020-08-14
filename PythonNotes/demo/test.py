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

# 找出小于100的最大平方值
# from math import sqrt
# for n in range(99, 0, -1):
#     root = sqrt(n)
#     if root == int(root):
#         print(n)
#         break


#　while为true,执行循环代码，用户无任何输入，代码继续循环，word为空值
# word = 'hello'
# while word:
#     word = input('please enter a word:')
#     print('the word was', word)

# while 始终为true,执行循环内代码,if not word判断用户输入情况，如not word为true时执行break结束循环
# while True:
#     word = input('please enter a word:')
#     if not word: 
#         break
#     print(word)

# while循环 else执行控制
# from math import sqrt
# for n in range(99, 81, -1):
#     root = sqrt(n)
#     if root == int(root):
#         print(n)
#         break
# else:
#     print('while else')

# girls = ['alice', 'bernice', 'clarice']
# boys = ['chris', 'arnold', 'bob']
# letterGirls = {}

# for girl in girls:
#     letterGirls.setdefault(girl[0], []).append(girl)
# print([b+'+'+g for b in boys for g in letterGirls[b[0]]])
# print(letterGirls)

# for target_list in expression_list:
#     pass
# else:
#     pass

print('qer')