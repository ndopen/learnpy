template = '''<html>
<head>
    <title>{title}</title>
    </head>
    <body>
    <h1>{title}</h1>
    <p>{test}</p>
    </body>
</html>
'''
title = '创建和使用字典'
test = '字典由键 及其相应的值 组成，这种键-值对称为项 （item）。在前面的示例中，键为名字，而值为电话号码。每个键与其值之间都用冒号（: ）分隔，项之间用逗号分隔，而整个字典放在花括号内。空字典（没有任何项）用两个花括号表示，类似于下面这样：{} 。'

data = dict([('title', title), ('test', test)])
print(template.format_map(data))