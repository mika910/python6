# 作者: 王道 龙哥
# 2022年06月29日11时27分17秒
# 作者: 王道 龙哥
# 2022年06月29日11时25分29秒
from time import ctime, sleep

def timefun(func):
    def wrapped_func(a,b): #和func的参数个数保持一致
        print("%s called at %s" % (func.__name__, ctime()))
        func(a,b)
    return wrapped_func

@timefun
def foo(a,b):
    print(a+b)

foo(3,5)
# sleep(2)
foo(2,4)