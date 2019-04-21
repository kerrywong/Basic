# 切片
l=[1,2,3,4,5,6]
print(l[1:3:2]) # l[m:n:p] 下角标m~（n-1）的元素 隔p个元素（没有赋值的时候默认为1）
print(l[::2]) # m,n默认值为list的第一个下角标和最后一个下角标
print(l[:3]) # m没有赋值的时候默认为0
print(l[-3:-1]) # l[-m:-n]从倒数m个开始到倒数（n+1）个，n默认值为0

# 迭代
# 可以迭代对象的有：list tuple dict set str generator(yield generator function)
# 可以使用isinstance()判断对象是否可以迭代
from collections import Iterable
print(isinstance({},Iterable))

d={'name':"wangkang","age":24,"gender":"male"}
# 默认情况下，dict迭代的是key。
for x in d:
    print(x)
# 如果要迭代value，可以用for value in d.values()
for x in d.values():
    print(x)
# 如果要同时迭代key和value，可以用for k, v in d.items()。
for x,y in d.items():
    print(str(x)+":"+str(y))

# 列表生成式
print([x*x for x in range(1,11)]) # 注意生成的是list
print([x*x for x in range(1,11) if x%2==1])
print([x for x in range(1,101) if x%7==0])
print(['组合有：'+m+n for m in 'ABC' for n in 'abc'])

# 生成器
def fib(max):
    n,a,b=0,1,1
    while n<=max:
        yield b
        a,b=b,a+b
        n+=1
    return 'done'  # 返回的就是一个生成器
for x in fib(10):
    print(x)  # 通过迭代将生成器的值输出

# 生成器遇一次就停一次
def odd():
    print("step 1")
    yield(1)
    print("step 2")
    yield(2)
    print("step 3")
    yield(3)
t=odd()
print(next(t))
print(next(t))
print(next(t))


# 函数名本身可以作为参数
def fun(a,b,f):
    return f(a)+f(b)
def mul(a):
    return a*a
print(fun(1,2,mul))
# 变量可以指向函数
f=abs
print(f(-9))


# map() 两个参数（一个是函数，另一个Inteable），返回是一个Iterator
l=[1,2,3,4,5,6,7]
def f(x):
    return x*x
print(map(f,l)) # 使用自定义函数
print(list(map(f,l))) # 将generator转化为list

print(list(map(str,[1,2,3,4]))) # 使用已带的函数

# reduce 相当于前一次的结果作为后一次的第一个参数 作用对象是list
from functools import reduce
def add(x,y):
    return x*10+y
print(reduce(add,[1,2,3,4,5,6]))


# filter filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。
# 返回值是Iterator
def not_empty(s):
    return s and s.strip();
print(list(filter( not_empty,[' ','a','b',' ','c'])))


# sorted() 排序
list_sort=[1,2,4,6,3,-4,5]
print(sorted(list_sort))
print(sorted(list_sort,key=abs)) #按照绝对值 key是可以指定的函数
list_sort2=["asdf","Abahs","cdiegh","dfgg"]
print(sorted(list_sort2)) # 字符按照ASCII大小进行比较
print(sorted(list_sort2,key=str.upper)) # 全部转化为大写字母排序








