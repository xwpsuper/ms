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
        print('|{:6.4f}| {}买入{}: {} x {}'.format(time.time() % 60, self.username, symbol, price, lot))
        time.sleep(random.random() * 0.03 + 0.02)
        return True if random.random() < 0.0005 else False

Send = Trader('XWP')
lock = threading.Lock()
# 任务1
'''
while not Send.buy(600001, 32.32, 12300):
    pass
'''

#任务2
'''
Done = False #多线程没有返回运行函数的方法，定义一个全局变量接收线程中的函数返回值
def run(symbol, price, lot):
    global Done
    lock.acquire()
    Done = Send.buy(symbol, price, lot)
    lock.release()
while not Done:
    threading.Thread(target = run, args =(600001, 32.32, 12300)).start()
    time.sleep(0.005)
'''
#任务3 
from concurrent.futures import ThreadPoolExecutor
#window自身开启线程消耗资源比较厉害，所以要使用线程池减小开启线程的消耗
threadpool = ThreadPoolExecutor(20)

Done = False
def run(symbol, price, lot):
    global Done
    # lock.acquire()    #加锁影响性能
    Done = Send.buy(symbol, price, lot)
    # lock.release()

t0 = time.time()
while not Done:
    if time.time() - t0 <= 6:
        threadpool.submit(run, 600001, 32.32, 12300)
        time.sleep(1)
        continue
    elif time.time() - t0 <= 8:
        threadpool.submit(run, 600001, 32.32, 12300)
        time.sleep(0.02)
        continue
    elif time.time() - t0 <= 100:
        threadpool.submit(run, 600001, 32.32, 12300)
        time.sleep(0.005)
        continue
    print('++++++++++++++')
    break
