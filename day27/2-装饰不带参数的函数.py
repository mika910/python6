# 作者: 王道 龙哥
# 2022年06月29日11时25分29秒
from time import ctime, sleep


def timefun(func):
    def wrapped_func():
        print("%s called at %s" % (func.__name__, ctime()))
        return func()

    return wrapped_func


# foo = timefun(foo)
# foo先作为参数赋值给func后，foo接收指向timefun返回的wrapped_func
@timefun
def foo():
    print("I am foo")


foo()
sleep(2)
foo()

print(foo.__name__)  # wrapped_func
