#!/usr/bin/python3.7
import threading
from multiprocessing import dummy
from multiprocessing import pool
import queue
import os


class Mythread(threading.Thread):
    def __init__(self, id):
        super(Mythread, self).__init__()
        self.id=id

    def run(self):#run为初始化后默认执行函数
        print('Hello,World')
        print(self.id)#变量通过绑定self实例解决
        q.put(self.id)


class ThreadPools(object):
    def __init__(self, target):
        pass


class MyProcess(object):
    def __init__(self, target):
        pass


class ProcessPools(object):
    def __init__(self, target):
        pass


def says_threading(Thread_id):
    print('Hello,World!')
    print(Thread_id)
    q.put(Thread_id)


def says_processsing(i):
    print(i)
    print(os.getpid())


if __name__ == "__main__":
    print('请输入执行类型：1.面向对象多线程;5.面向过程多线程')
    a = input()
    thread = []
    q=queue.Queue()
    if a == "1":
        for i in range(5):
            thread.append(Mythread(i))# 生成
        for i in range(5):
            thread[i].start()# 启动
        for i in range(5):
            thread[i].join()# 等待执行
        while not q.empty():
            char_=q.get()
            print(char_)
    elif a == "2":
        pass
    elif a == 3:
        pass
    elif a == 4:
        pass
    elif a == "5":
        for i in range(5):
            thread.append(threading.Thread(target=says_threading,args=(i,)))
        for i in range(5):
            thread[i].start()
        for i in range(5):
            thread[i].join()
        while not q.empty():
            char_=q.get()
            print(char_)
    elif a == 6:
        pass
    elif a == 7:
        pass
    elif a == 8:
        pass
    elif a=="9":
        pass
