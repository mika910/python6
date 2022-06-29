# 作者: 王道 龙哥
# 2022年06月29日11时28分59秒
def set_func(func):
    def call_func(*args, **kwargs):
        print("---这是权限验证1----")
        print("---这是权限验证2----")
        # func(args, kwargs)  # 不行，相当于传递了2个参数 ：1个元组，1个字典
        # 拆包的过程，*args拆包到位置参数，**kwargs拆包到关键字参数
        func(*args, **kwargs)

    return call_func


@set_func  # 相当于 test1 = set_func(test1)
def test1(num, *args, **kwargs):
    print("-----test1----%d" % num)
    print("-----test1----", args)
    print("-----test1----", kwargs)


test1(100)
test1(100, 200)
test1(100, 200, 300, mm=100)
