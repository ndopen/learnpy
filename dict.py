from typing import List


def dict(dict_data):
    """
    docstring
    """
    pass



dict_data = {
    "hello Python interpreter" : "解釋器",
    "traceback" : "回溯",
    "defined" : "定义",
    "format" : "格式"
    
}

getkeys = sorted(dict_data.keys())
getvalues = dict_data.values()


# print(dict_data['defined'])

print(getkeys)
print(getvalues)

for keys, values in dict_data.items():
    print(f"they keys:{keys} in dict_data")
    print(f'they values:{values} in dict_data')