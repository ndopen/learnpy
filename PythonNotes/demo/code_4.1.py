def __init__():
    """users date"""


def peoque(name, request='a'):
    #　人员数据
    people = {
        'cock' : {
            'phone':'127342331',
            'addr':'china',
        },
        'zhou' : {
            'phone':'213412342',
            'addr':'japan',
        },

        'wang' : {
            'phone':'234212344',
            'addr':'Singapore',
        }
    }

    # 标签简写
    # 简码标签，获取对比用户输入的值，［思路待实现］
    kyes = {'q':'phone', 'a':'addr'}

    #　打印标签 
    labels = {
        'phone' : '电话号码',
        'addr' : '地址'
    }

    key = request

    # 判断查询内容
    if request == 'q':
        key = 'phone'
    else:
        key = 'addr'

    # 查询人员数据并返回数据
    person = people.get(name, {})
    label = labels.get(key, key)
    result = person.get(key, '查询数据为空!')

    print("{} {} : {}.".format(name, label, result))


name = input('输入查询人姓名：')
request = input('输入想查询的内容（＂ｑ＂为地址＼＂ａ＂为地址）')

peoque(name, request)
# print(peoque)