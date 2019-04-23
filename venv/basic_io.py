#!/usr/bin/python3
# open
import io
import os

with open(r'C:\Users\yilus\PycharmProjects\Basic\venv\Files\a', 'r', encoding='utf-8') as f:
    # print(f.read())  # 小文件可以，一次读取
    for line in f.readlines():
        print(line.strip())  # 一行一行的读取 strip()是去掉\n

# 打开二进制文件：照片等
# open(path,'rb')

# 字符编码
# open(path,'r',encoding='gbk',error='ignore')

# write
with open(r'C:\Users\yilus\PycharmProjects\Basic\venv\Files\a', 'a') as f:
    # 当然可以指定编码形式encoding
    f.write("\nhello,world")  # 在后面追加一行

# StringIO
from io import StringIO  # 在内存读写str

f = StringIO()
print(f.write("hello"))
f.write(" world")  # 返回值是写入字符的个数
print(f.getvalue())  # 获取写入的值

'''
print("hello")
'''
'''

'''
f2 = StringIO('hello\nfangjun\n')
while True:
    s = f2.readline()
    if s == '':  # 为空，不是空格值得注意的一点，否则遇到死循环
        break
    print(s.strip())
# 读取二进制文件
from io import BytesIO

f3 = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(f3.read())

print(os.environ)  # 打印系统消息
print(os.path.abspath('.'))  # 打印当前的目录
# 创建新目录，首先展示新目录的完整路径表示使出来
# os.path.join(r'C:\Users\yilus\PycharmProjects\Basic\venv','testdir')
# 创建新目录
# os.mkdir(r'C:\Users\yilus\PycharmProjects\Basic\venv\testdir')
# 删除某一文件
# os.rmdir(r'C:\Users\yilus\PycharmProjects\Basic\venv\testdir')
path_pwd = os.getcwd()  # 获取当前该文件的目录
print(path_pwd)
print(os.listdir(path_pwd))
print(os.path.splitext(path_pwd + r'\basic_01.py'))  # 获取文件后缀名
# os.rename(path_pwd+r'\basic_09.py','basic_01.py') # 重命名文件
# os.remove(path_pwd+'\basic_09.py') # 删除文件

# 序列化 变量从内存中编程可存储或者是传输的过程，写入磁盘
import pickle

d = dict(name='Bob', age=20, score=88)
f4 = open('dump.txt', 'wb')
pickle.dump(d, f4)
f.close()

f4 = open('dump.txt', 'rb')
d2 = pickle.load(f4)  # 读取序列化
f4.close()
print(d2)

# JSON
import  json
print(json.dumps(d)) # 序列化
print(json.loads(json.dumps(d))) #反序列化
# 普通的类是不能Json化的 必须进行转化

class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score
def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }
s = Student('Bob', 20, 88)
print(json.dumps(s, default=student2dict))# jump的第二个参数相当于转化的函数
print(json.dumps(s, default=lambda obj:obj.__dict__))

