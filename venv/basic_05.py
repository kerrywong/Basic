# try...except...else...finally
try:
    a=input("Please input a number:")
    r=10/int(a)
    print("The result is %s"%str(r))
except ValueError as e:
    print('ValueError:',e)
except ZeroDivisionError as e:
    print("ZeroDivisionError:",e)
else:
    print("no error")
finally:
    print("finally...")
print("END")

# Use Stack
def foo(s):
    return  10/int(s)

def bar(s):
    return foo(s)*2

def main():
    bar('0')

#main()   # 若错误没有被捕获，则一直往上抛，最后被解释器捕获，打印一个错误

# Record error
import logging # 记录错误信息的模块
def main2():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)
#main2()
print("End")

#Throw error
class Foo2Error(ValueError):
    pass

def foo2(s):
    n=int(s)
    if n==0:
        raise Foo2Error("invalid value:%s"% s) # 抛出异常
    return 10/n

#foo2('0')

# 调试
# print()函数  以及 assert eg: assert n!=0,"n is not zero"
# import logging
# logging.basicConfig(level=logging.INFO) # 在引入模块后添加一行配置
# import pdb
# pdb.set_trace()  # 设置断点，运行在这里会自动暂停

# 单元测试
import unittest
from MyModules.test_module import Dict
class TestDict(unittest.TestCase):
    def test_init(self):
        d=Dict(a=1,b='test')
        self.assertEqual(d.a,1)
        self.assertEqual(d.b,'test')
        self.assertTrue(isinstance(d,dict))

    def test_key(self):
        d=Dict()
        d['key']='value'
        self.assertEqual(d.key,'value')

    def test_attr(self):
        d=Dict()
        d.key="value"
        self.assertTrue('key'in d)
        self.assertEqual(d['key'],'value')

    def test_keyerror(self):
        d=Dict()
        with self.assertRaises(KeyError):
            value=d['empty']

    def test_attrerror(self):
        d=Dict()
        with self.assertRaises(AttributeError):
            value=d.empty

unittest.main()

# setUp和setDown  调用一次测试方法的前后分别被执行
