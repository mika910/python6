# 作者: 王道 龙哥
# 2022年06月29日11时44分54秒

class Test:
    # init中相当于外部函数的功能
    def __init__(self,func):
        print("-----初始化-----")
        print("func name is %s"%func.__name__)
        self.func=func
    #call相当于装饰器中调用函数
    def __call__(self, *args, **kwargs):
        print('这个是什么验证')
        return self.func(*args, **kwargs)


@Test   # 相当于test = Test(test)
def test():
    print("----test---")

test()