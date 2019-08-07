# 斐波那契数(每个列表数据都是前两个的和)
# fids = [0, 1]
# num = int(input('How many Fibonacci numbers do you want? '))

# for i in range(num-2):
#     fids.append(fids[-2] + fids[-1])
# print(fids)

# def fibs(num):
#      result = [0, 1]
#      for i in range(num-2):
#          result.append(result[-2] + result[-1])
#      return result
# fibs(20)

# print(callable(fibs))

# CreateFuntion
def hello(name):
    return 'hello' + name
hello('cock')