


a = '1+5-6*2/0'

try:
    print(eval(a))
except BaseException:
    print('error')

