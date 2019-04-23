import time,threading,multiprocessing

# 新线程执行的代码
def loop():
    print('thread %s is running' % threading.current_thread().name)
    n=0
    while n<5:
        n+=1
        print('thread %s >>> %s'%(threading.current_thread().name,n))
        time.sleep(1)
    print('thread %s ended'% threading.current_thread().name)

print('thread %s is running...'% threading.current_thread().name)
t=threading.Thread(target=loop,name='LoopThread')# 自定义子线程的名字 默认为Thread-1
t.start()
t.join()
print('thread %s ended' % threading.current_thread().name)# 从线程结束后，主线程也就结束了

balance=0
lock=threading.Lock() # 声明一个线程锁
def change_int(n):
    global balance
    balance=balance+n
    balance=balance-n
def run_thread(n):
    for i in range(10000):
        lock.acquire() # 获取一个锁
        try:
            change_int(n)
        finally:
            lock.release() # 用完一个锁之后就释放点

t1=threading.Thread(target=run_thread,args=(5,))
t2=threading.Thread(target=run_thread,args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)


'''
def loop2():
    x=0
    while True:
        x=x^1
for i in range(multiprocessing.cpu_count()):  # 多核CPU
    t = threading.Thread(target=loop())
    t.start()
'''




# ThreadLocal 当前进程
local_school=threading.local()
def process_student():
    std=local_school.student #获当前进程相关联的student
    print('hello %s in %s' %(std,threading.current_thread().name))

def process_thread(name):
    local_school.student=name #绑定ThreadLocal的student
    process_student()

t1=threading.Thread(target=process_thread,args=('Alice',),name='Thread-A')
t2=threading.Thread(target=process_thread,args=('Bob',),name='Thread-b')
t1.start()
t2.start()
t1.join()
t2.join()