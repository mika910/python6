# 作者: 王道 龙哥
# 2022年06月29日11时48分36秒
from functools import wraps

def my_decorator(func):
    @wraps(func) #让函数名和备注称为原有的函数的，而不是装饰器的
    def wper(*args, **kwargs):
        '''decorator'''
        print('Calling decorated function...')
        return func(*args, **kwargs)
    return wper

# example=my_decorator(example)
@my_decorator
def example():
    """example的doc"""
    print('Called example function')

# example.__name__ ==example
# example.__doc__ == example的doc
# 加了wraps后，打印example就是原本的名字和注释
# 如果不加wraps，打印的是装饰器里面的
print(example.__name__, example.__doc__)
example()