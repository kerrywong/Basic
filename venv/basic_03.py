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


