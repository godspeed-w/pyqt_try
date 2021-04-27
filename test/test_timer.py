import threading

def say_hello(arg=''):
    timer_online = threading.Timer(1, say_hello,('world',))
    timer_online.start()
    print('hello ',arg)


say_hello()