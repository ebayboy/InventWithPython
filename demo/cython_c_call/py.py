import time

def fib_python(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib_python(n - 1) + fib_python(n - 2)

if __name__ == '__main__':
    t1 = time.time()
    print("python:斐波那契数列第40项的结果为:{}".format(fib_python(30)))
    t2 = time.time()
    print("使用python运行递归斐波那契数列程序的运行时间为: {}s".format(t2 - t1))
