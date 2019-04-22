class Student(object):
    def __init__(self, name, score):  # 类的第一个参数永远是self。表明创建的实例本身，不需要传，解释器自己会把实例变量传进去
        self.name = name              # 定义一些相关的属性
        self.score = score
    # 类的方法
    def print_class(self): # 方法的定义参数为类
        print('%s:%s'%(self.name,self.score))

wangkang = Student('wangkang', 100)
wangkang.print_class()


# 类封装数据
class Student2(object):
    def __init__(self,name,score):
        self.__name=name # private 只能内部访问
        self.__score=score
    def print_class(self):
        print('%s:%s'%(self.__name,self.__score))
    def get_name(self): # 外部代码访问private的属性
        return self.__name
    def get_score(self):
        return self.__score
    def set_name(self,name): # 外部代码更改属性
        self.__name=name
    def set_score(self,score):
        self.__score=score

fangjun=Student2("fangjun",19)
fangjun.print_class()
fangjun_name=fangjun.get_name()
print("他的名字叫做："+fangjun_name)
fangjun.set_score(100) # 外部代码更改属性
fangjun.print_class()


# 继承和多态
class Animal(object):
    def run(self):
        print("Animal is running")

class Dog(Animal): # 继承的表现方式
    def run(self):
        print("Dog is running")
    def humman_like(self):
        print("People like dogs")

dog=Dog()
dog.run()#子类自动继承父类的方法 若重载时，则采取子类的方法
dog.humman_like() # 子类自定义方法
print(isinstance(dog,Animal)) # 通过isinstance() 来判断是否是相应的类型
def run_twice(animal):
    animal.run()
    animal.run()
class Duck(Animal):
    def run(self):
        print("Duck is very cute")
duck=Duck()
run_twice(dog) #多态的优点
run_twice(duck)


# 判断是否有相关的属性
print(hasattr(fangjun,'name')) # private属性外部代码访问不了
print(hasattr(wangkang,'name')) # True
setattr(wangkang,'age',20) # 设置一个新属性
print(hasattr(wangkang,'age'))
print("wangkang年龄为："+str(getattr(wangkang,'age'))) # 获取相关的属性值
print(hasattr(dog,'run')) # 查找有没有对应的方法
print(getattr(wangkang,'gender','male'))# 若是获取不到该属性，则设置默认值

# dir()
# 获取某一对象的所有属性和方法
print(dir(Dog))


# 动态给实例绑定属性或方法 只对这一实例临时起作用
class School(object):
    def print_name(self):
        print("This is school")
hut=School()
hut.name="hunan nan university of technology" # 动态加属性
print(hut.name)

def set_address(self,address):
    self.address=address
from  types import MethodType
hut.set_address=MethodType(set_address,hut)
hut.set_address("hunan")
print(hut.address)
# 只对这一实例临时起作用，对于其他实例不起作用
hutt=School()
#print(bool(hutt.set_address("hunan zhuhou"))) # 这句会报错

# 给类添加方法
School.set_address=set_address


# 限制添加属性 __slots__
class Car(object):
    __slots__ = ('brand','price')

benze=Car()
benze.brand="Benze"
benze.price=1200000
#benze.colour="black"  #这句话会报错

print("benze的品牌叫做"+benze.brand)



