rule80 = 80
rule120 = 120
rule160 = 160


pace = input('当前数据：')

if rule80 <= pace and rule120 >= pace:
    print('平安驾驶,当前速度：{}'.format(pace))

elif rule80 > pace or rule120 <= pace and rule160 > pace:
    print('危险驾驶,当前速度：{}'.format(pace))

elif rule160 <= pace:
    print('严重超速,当前速度：{}'.format(pace))
else:
    print('数据错误')
