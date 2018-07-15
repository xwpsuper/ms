'''
Python习题: 写一个简单的股票抢单器。

前置0. 假定已经有封装好的交易类Trader，见最后
任务1. 不停调用Trader抢单直到抢中为止
任务2. 使用多线程调用Trader, 使下单间隔为0.005秒, 抢中以后终止
任务3. 多阶段调用, 在开启任务的前3分钟, 下单间隔为1秒1次, 第4分钟0.2秒一次, 第5分钟0.02秒一次, 第6分钟0.002秒一次
'''

import time
import random
import threading

class Trader(object):
    def __init__(self, username):
        self.username = username
    def buy(self, symbol, price, lot):
        print(f'|{time.time() % 60:6.3f}| {self.username}买入{symbol}: {price} x {lot}')
        time.sleep(random.random() * 0.03 + 0.02)
        return True if random.random() < 0.05 else False

class Mythread(threading.Thread):
    def __init__(self, func, args):
        threading.Thread.__init__(self)
        self.func = func
        self.args = args
    def run(self):
        self.func(*self.args)
 
def successed(username, symbol, price, lot):
    while Trader(username).buy(symbol, price, lot):
        return True

qd = successed
list1 = ['XWP', '600000', 32.32, 12300]

def one_thread(func, args):
    while True:
        t = Mythread(qd, list1)
        t.start()
        break

interval = 0.01

while True:
    time.sleep(0.002)
    print(time.time() % 60)
    one_thread(qd, list1)

