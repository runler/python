import time
from threading import Thread
from multiprocessing import Process

def piao(name):
    print('%s piaoing'%name)
    time.sleep(2)
    print('%s piao end'%name)


if __name__ == '__main__':
    p1 = Process(target=piao,args=('Process',))
    p1.start() # 开启后先申请资源，才会执行piao
    t1 = Thread(target=piao,args=('Thread',))
    t1.start() # 开启后立马执行piao里的代码
    print('主线程')