# 转义字符
'''
print("I\'m OK \nCome on! Everything will be OK")
print(r"I'm OK!!")# 转义多个字符
'''

# list（列表） 可以随便添加和删除
# list元素可以也是list
classmates=["A","B","C","D"]
print(classmates)

print(len(classmates)) # 求list的长度

classmates.pop(2) # 删除list指定位置的元素，默认为list尾
print(classmates)

classmates.insert(1,"D") # 指定位置插入元素
print(classmates)

classmates[2]="E" # 指定位置进行元素更改
print(classmates)

# tuple（元组） 不能更改
# tuple里面的元素可以是list
t=(1,2,3)
print(t)

t=(1,) # 这是元组一个元素的表示方法，后面要加一个逗号
print(t) # 否则会被认为数学中的括号

t2=(1,2,[1,3])
t2[2][1]=4 # list可以是可以更改的
print(t2)

# while&input 输入的是字符串
birth=input("你的生日年份是:")
if(int(birth) < 200): # 字符串进行转化成整数
    print("好老")
else:
    print("好年轻")


# for x in list/tuple
l=list(range(8)) # range(x) 随机生成0~x（不包括）的整数x
sum = 0;
for x in l:
    sum += x;
print(sum)


# dict (字典) 相当于自定义索引的list
d={"name" : "wangkang", "age": 24, "sender" : "male"}
print(d)
print(d["name"]) # 输出单个元素 若是不存在则会报错
print("sender" in d) # 判断key是否存在
d.get("name",1) # key存在则返回指定的值（自定义）
d.pop("sender")
d.update({'age':25, 'name': 'WangKang'}) # 批量修改 {} 以及key和为单引号
d.update({'gender':'male'}) # 当key不存在时，使用update()时自动添加
print(d)

# set 可以求集合的相关问题
set1=set([1,2,3,3,4]) # 声明的时候([...])
print(set1) # set 自动过滤重复的key
set1.add(3) # 添加重复元素 并没用
set1.add(5) # 这样才有用
set1.remove(2)
print(set1)

str1="abc"
str1.replace('a','A') # str为不可变量，只用重新赋值才有用
print(str1)

str2=str1.replace('a','A')
print(str2)














