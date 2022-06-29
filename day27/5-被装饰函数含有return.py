# 作者: 王道 龙哥
# 2022年06月29日11时31分54秒
from time import ctime, sleep

def timefun(func):
    def wrapped_func():
        #print(get_info.__name__)
        print("%s called at %s" % (func.__name__, ctime()))
        func()  #一般情况下为了让装饰器更通用，加上return
    return wrapped_func

@timefun
def get_info():
    return '这是重要的任务'

print(get_info())