# coding:utf-8
import multiprocessing as mul
import os


class myProcess(mul.Process):

    def __init__(self, num, func):
        super(myProcess, self).__init__()
        self.num = num
        self.func = func

    def run(self):
        print("my Process", os.getpid())
        print(self.num)
        self.func()




def foo():
    print("process %s is running" % os.getpid())

if __name__ == '__main__':

    p1 = myProcess(1, foo)
    # p2 = myProcess(2, foo)
    p1.start()
    # p2.start()
    p1.join()
    # p2.join()
    print('ending...')





