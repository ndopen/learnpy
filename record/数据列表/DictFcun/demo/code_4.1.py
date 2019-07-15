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

    #　打印标签 
    labels = {
        'phone' : '电话号码',
        'addr' : '地址'
    }

    # 判断查询内容
    if request == 'q':
        key = 'phone'
    elif request == 'a':
        key = 'addr'
    else:
        print('输入错误!')

    # 查询人员数据并返回数据
    if name in people:
        print("{}{}：{}".format(name, labels[key],people[name][key]))
    else:
        print('查询数据失败!')


name = input('输入姓名:')
request = input('查询电话号码输入（q），查询地址输入（a）:')

peoque(name,request)