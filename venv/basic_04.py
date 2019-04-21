# 函数作为返回值
def lazy_sum(*args):
    def sum_list():
        sum=0
        for x in args:
            sum = sum + x
        return sum
    return sum_list

f1=lazy_sum(1,2,3)
print(f1) # 返回的是函数整整体（本身，参数，函数值）
print(f1()) # 使用f1函数里面返回值

f2=lazy_sum([1,2,3]) # 每次调用的时候都会返回一个新函数 故不能相比较
print(f1==f2)  # 结果肯定是false


# 闭包问题 内部函数变量还被新函数引用
def count():
    fs=[]
    for x in range(1,5):
        def f():
            return x*x
        fs.append(f)
    return fs
f1=count()[0]
f2=count()[1]
f3=count()[2]
# 答案都是16 出现这种问题在于返回函数不要引用任何循环变量，或者后续会发生变化的变量。
# 所有函数创建完才返回，此时变量便成为了最后一个参数
print(str(f1())+" "+str(f2())+" "+str(f3()))

#  改进
def count2():
    def g(x):
        def f():
            return x*x
        return f
    l=[]
    for x in range(1,5):
        l.append(g(x))
    return l
l=count2()
print(l)
print(l[0]())
print(l[1]())
print(l[2]())


# 匿名函数 自定义参数和相关的关系
f=lambda x:x*x  # 返回的是一个函数
print(f(4))
f2=lambda x,y:x+y
print(f2(2,3))

# 装饰器
# 在函数调用前后自动打印日志，但又不希望修改now()函数的定义，
# 这种在代码运行期间动态增加功能的方式
def now():
    print("hello")

f=now
f()
print(f.__name__) # 获取函数名

import functools
def log(func):
    def wrapper(*args,**message):
        print("call %s()"%func.__name__)
        return func(*args,**message)
    return wrapper;

@log # 装饰器  新的函数同名函数 不影响以前的函数
def now():
    print("hello world")
now()
print(now.__name__) # 此时now()函数指向wrapper


#偏函数
print(int('1234',base=8)) # 字符串以几进制（默认为十进制）形式转化为十进制
def int2(x,base=2): # 自定义转化二进制
    return int(x,base)
print(int2('1010010'))

int3=functools.partial(int,base=2) # 内置的偏函数
int4=functools.partial(max,10) # 将10 自动添加到max函数参数的左边
print(int4(1,2,9))
print(int3('1111'))
