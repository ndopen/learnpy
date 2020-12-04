import json

FILENAME = 'Usernumber.json'
number = input("输入内容，如果需要显示查询的数据，请出入show,否则输入其他任何内容")

def store():
    """
    存储用户
    """
    with open(FILENAME, 'w') as filename:
        json.dump(number, filename)
        print('数据存储成功，输入show打印数据')



def show():
    """
    显示问候
    """
    with open(FILENAME, 'r') as filename:
        filename = json.load(filename)
        print(filename)

def index(number):
    """
    用户输入
    判断用户输入的关键字给予回复
    """
    if number == "show":
        show()
    else:
        store()


index(number)