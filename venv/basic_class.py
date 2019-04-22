class Student(object):
    def __init__(self, name, score):  # 类的第一个参数永远是self。表明创建的实例本身，不需要传，解释器自己会把实例变量传进去
        self.name = name  # 定义一些相关的属性
        self.score = score

    # 类的方法
    def print_class(self):  # 方法的定义参数为类
        print('%s:%s' % (self.name, self.score))


wangkang = Student('wangkang', 100)
wangkang.print_class()


# 类封装数据
class Student2(object):
    def __init__(self, name, score):
        self.__name = name  # private 只能内部访问
        self.__score = score

    def print_class(self):
        print('%s:%s' % (self.__name, self.__score))

    def get_name(self):  # 外部代码访问private的属性
        return self.__name

    def get_score(self):
        return self.__score

    def set_name(self, name):  # 外部代码更改属性
        self.__name = name

    def set_score(self, score):
        self.__score = score


fangjun = Student2("fangjun", 19)
fangjun.print_class()
fangjun_name = fangjun.get_name()
print("他的名字叫做：" + fangjun_name)
fangjun.set_score(100)  # 外部代码更改属性
fangjun.print_class()


# 继承和多态
class Animal(object):
    def run(self):
        print("Animal is running")


class Dog(Animal):  # 继承的表现方式  多重继承则为class Child(Father1,..,FatherN)
    def run(self):
        print("Dog is running")

    def humman_like(self):
        print("People like dogs")


dog = Dog()
dog.run()  # 子类自动继承父类的方法 若重载时，则采取子类的方法
dog.humman_like()  # 子类自定义方法
print(isinstance(dog, Animal))  # 通过isinstance() 来判断是否是相应的类型


def run_twice(animal):
    animal.run()
    animal.run()


class Duck(Animal):
    def run(self):
        print("Duck is very cute")


duck = Duck()
run_twice(dog)  # 多态的优点
run_twice(duck)

# 判断是否有相关的属性
print(hasattr(fangjun, 'name'))  # private属性外部代码访问不了
print(hasattr(wangkang, 'name'))  # True
setattr(wangkang, 'age', 20)  # 设置一个新属性
print(hasattr(wangkang, 'age'))
print("wangkang年龄为：" + str(getattr(wangkang, 'age')))  # 获取相关的属性值
print(hasattr(dog, 'run'))  # 查找有没有对应的方法
print(getattr(wangkang, 'gender', 'male'))  # 若是获取不到该属性，则设置默认值

# dir()
# 获取某一对象的所有属性和方法
print(dir(Dog))


# 动态给实例绑定属性或方法 只对这一实例临时起作用
class School(object):
    def print_name(self):
        print("This is school")


hut = School()
hut.name = "hunan nan university of technology"  # 动态加属性
print(hut.name)


def set_address(self, address):
    self.address = address


from types import MethodType

hut.set_address = MethodType(set_address, hut)
hut.set_address("hunan")
print(hut.address)
# 只对这一实例临时起作用，对于其他实例不起作用
hutt = School()
# print(bool(hutt.set_address("hunan zhuhou"))) # 这句会报错

# 给类添加方法
School.set_address = set_address


# 限制添加属性 __slots__
class Car(object):
    __slots__ = ('brand', 'price')


benze = Car()
benze.brand = "Benze"
benze.price = 1200000
# benze.colour="black"  #这句话会报错

print("benze的品牌叫做" + benze.brand)


# property 负责把一个方法变成属性调用
class People(object):
    @property  # 实例操作的时候属性不是直接暴露的，而是通过getter和setter方法实现的
    def age(self):
        return self._age

    @age.setter  # property本身创建的装饰器
    def age(self, value):
        if not isinstance(value, int):
            raise ValueError('Age must be integer')
        if value <= 0:
            raise ValueError('Age must bigger than 0')
        self._age = value


xiaohong = People()
xiaohong.age = 9
print(xiaohong.age)


# __str__  返回的是用户看到的字符串
class Student3(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'This object name:%s' % self.name

    __repr__ = __str__  # __repr__ 返回的是程序开发者看到的字符串(调试作用的)


print(Student3('wangkang'))


# __iter__ 可以是对象成为一个迭代对象
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self  # 实力本身就是一个迭代对象，所以返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 10000:  # 退出循环的条件
            raise StopIteration()
        return self.a  # 返回下一个值


for n in Fib():  # Fib() 此时是一个迭代的对象  但是不能想list那样取值
    print(n)


# 改进
class Fib2(object):
    def __getitem__(self, item):  # 使对象变成list那种能取出下角标
        if isinstance(item, int):  # __getitem__ 参数为int的时候
            a, b = 1, 1
            for x in range(item):
                a, b = b, a + b
            return a
        if isinstance(item, slice):  # __getitem__ 参数为slice的时候
            start = item.start
            stop = item.stop
            if start is None:  # 没有对step进行处理
                start = 0
            a, b = 1, 1
            l = []
            for x in range(stop):
                if x >= start:
                    l.append(a)
                a, b = b, a + b
            return l


fib = Fib2()
print("The 7th is:%s" % fib[7])
print(fib[1:9:2])


# __getattr__ 动态返回一个属性
class Student4(object):
    def __init__(self, name):
        self.name = name

    def __getattr__(self, attr):
        if (attr == 'score'):
            return 99  # return lambda:99  调用时方法式调用
        return AttributeError("%s do not have this attribution" % self.name)

    def __call__(self, *args, **kwargs):  # __call__ 实例本身进行调用
        print("My name is %s" % self.name)


fangjun2 = Student4("fangjun")
print(fangjun2.sc)  # print(fangjun2.score())
fangjun2()  # 本身进行调用

# 判断对象能不能调用 可以使用callable()函数进行判断
print(callable(Student4("wangkang")))

# enum类
from enum import Enum, unique


@unique  # 检查一下有没有重复值
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6


seven_day = Weekday
print(seven_day(1))
print(seven_day.Thu.value)
print(seven_day.Thu)
for name, member in seven_day.__members__.items():
    print(name, '=>', member)


# 使用type()创建一个简单的类 总共需要三个参数
# 1.class的名称
# 2.继承的父类集合
# 3.class的方法名称与函数绑定
def print_hello(self, name='world'):
    print("hello,%s" % name)


Hello = type('Hello', (object,), dict(hello=print_hello))
h = Hello()
h.hello()
print(type(Hello))
print(type(h))


# metaclass 元类（了解） 控制类的创建行为
# __new__ 传的参数
# 1.当前准备创建的类的对象；
# 2.类的名字；
# 3.类继承的父类集合；
# 4.类的方法集合。
class listMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)


class Mylist(list, metaclass=listMetaclass):
    pass


l = Mylist()
l.add(1)
print(l)
