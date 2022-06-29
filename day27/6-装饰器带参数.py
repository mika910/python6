# 作者: 王道 龙哥
# 2022年06月29日11时39分10秒
from time import ctime


# pre是形参，缺省值为''空字符串
# 三层def
def timefun_arg(pre=''):
    def timefun(func):
        def wrapped_func():
            print("%s called at %s --%s" % (func.__name__, ctime(), pre))
            return func()  # 一般情况下为了让装饰器更通用，加上return

        return wrapped_func

    return timefun


# foo = timefun_arg('wangdao')->return timefun(foo)->return wrapped_func->return func()
# 1.调用timefun_arg('wangdao')，得到返回值timefun
# 2.将步骤1得到的返回值，即timefun返回，然后timefun(foo)
# 3.将timefun(foo)的结果返回，即wrapped_func
# 4.让foo=wrapped_fun,即foo现在指向wrapped_func

# 传入pre值
@timefun_arg('wangdao')
def foo():
    print('I am foo')


@timefun_arg('python')
def too():
    print('I am too')


foo()
too()
