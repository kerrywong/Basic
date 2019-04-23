from multiprocessing import Process
import os
def run_proc(name):
    print('Run child process %s %s'%(name,os.getpid())) #父进程 产生PID
if __name__ =='__main__':
    print('Parent process %s'%os.getpid())
    p=Process(target=run_proc,args=('test',)) # 子进程
    print('child process will start')
    p.start()
    p.join() # 等待子进程结束后往下运行
    print('child process end')

from multiprocessing import Pool
import os,time,random
def long_time_task(name):
    print('Run task %s %s ...'%(name,os.getpid()))
    start=time.time()
    time.sleep(random.random()*3)
    end=time.time()
    print('Task %s runs %0.2f seconds' %(name,(end-start)))

if __name__=='__main__':
    print('Parent process %s.'%os.getpid())
    p=Pool(4)
    for i in range(5):
        p.apply_async(long_time_task,args=(i,)) # apply_async 异步非阻塞的 apply 是阻塞的
    print('waiting for all subprocess done...')
    p.close()
    p.join()
    print('all subprocess done')

    # subprocess
    import subprocess
    print("$ nslookup www.python.org") # $相当于输入命令了
    r=subprocess.call(['nslookup','www.python.org'])
    print('exit code',r)

#进程间通信
from multiprocessing import Process,Queue
def write(q): # 写进程
    print('Process to write:%s'%os.getpid())
    for value in ['A','B','C']:
        print('Put %s to queue' % value)
        q.put(value)
        time.sleep(random.random())

def read(q):# 写进程
    print('Process to read:%s'%os.getpid())
    while True:
        value=q.get(True)
        print('Get %s from queue'%value)

#进程间通信
from multiprocessing import Process,Queue
def write(q): # 写进程
    print('Process to write:%s'%os.getpid())
    for value in ['A','B','C']:
        print('Put %s to queue' % value)
        q.put(value)
        time.sleep(random.random())

def read(q):# 写进程
    print('Process to read:%s'%os.getpid())
    while True:
        value=q.get(True)
        print('Get %s from queue'%value)

if __name__=='__main__':
    q=Queue()
    pw=Process(target=write,args=(q,))
    pr=Process(target=read,args=(q,))
    pw.start()
    pr.start()
    pw.join() #pw结束
    pr.terminate()# 读进程被强制停止