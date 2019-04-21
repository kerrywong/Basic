# 自定义函数库的函数名字
a=abs
print(a(-1))

# 自定义函数
def factorial(n):
    if(n==0):
        return 1;
    else:
        return n*factorial(n-1)
def pass_test(n):
    if(n>=0):
        pass
    else:
        return abs(n)
print(factorial(5))
print(pass_test(3)) # pass()返回的是None

# 函数返回多个值，返回的形式tuple
def area_cur(length,width):
    area=length*width
    cur=(length+width)*2
    return area,cur
print(area_cur(2,3))

# 函数参数默认值
def value_test(n=1):
    return n
print(value_test()) # 若是没有传参，就是用默认值
print(value_test(3)) # 传参的情况

# 函数参数是list
def add_append(l=[]):
    l.append("end")
    return l
print(add_append())
print(add_append()) #调用一次，在之前的l的基础上添加end

def add_appends(l=None):
    if l is None: # 避免以上的情况
        l=[]
    else:
        l.append("end")
    return l

print(add_appends(["wangkang","come on"]))
print(add_appends(["work hard"]))

# 函数参数可变
def multi(list):
    sum=0
    for x in list:
        sum+=x*x
    return sum
print(multi([1,2,3])) # 传参的时候是list
print(multi((1,2,3))) # 传参的时候有时候可以是tuple
def multi2(*list): # 可变参数,统一以上两种情况
    sum = 0
    for x in list:
        sum += x * x
    return sum
print(multi2(1, 2, 3)) # 实参为tuple的情况
list_value=[1,2,3,4]
print(multi2(list_value[0],list_value[1],list_value[2],list_value[3])) # 实参为list的情况

# 关键字为参数
def info(name,age,**message):
    print('name:',name,'age:',age,'other:',message) # 稍微注意下格式的问题

info("wangkang",24,gender="male",city="zhuzhou") # 可以传多个值

# 命名关键字为参数
def info2(name,age,**message):
    if 'city' in message:
        pass
    if 'job' in message:
        pass
    print('name:', name, 'age:', age, 'other:', message)

info2("wangkang",24,gender="male",city="zhuzhou",job="teacher") # 可以传多个值

# 限制相关的命名关键字作为关键字
def info3(name,age,*,city,job): # 只接受* 后面的参数
    print('name:', name, 'age:', age, 'city:', city,'job:',job)

info3("wangkang",24,city="zhuzhou",job="teacher") # 可以传多个值,但是只接受相关的参数值
def info4(name,age,*mess,city,job): # 若有可变参数，则实参必须有
    print('name:', name, 'age:', age, 'city:', city,'job:',job)

info4("wangkang",24,city="zhuzhou",job="teacher") # 可变参数必须有参数

# 当然所有的函数的形参都可以使用默认参数







