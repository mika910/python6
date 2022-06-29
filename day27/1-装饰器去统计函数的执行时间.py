# 作者: 王道 龙哥
# 2022年06月29日11时20分46秒
import time

def cal_execute_time(func):
    def call_func():
        start=time.time()
        func()
        end=time.time()
        print('use time {}'.format(end-start))
    return call_func

@cal_execute_time
def test1():
   print("-----test1----")
   for i in range(100000):
      pass

test1()