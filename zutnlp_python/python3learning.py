# #可变参数
# def report_card(name,*grades):
#     total=0
#     for grade in grades:
#         total+=grade
#     print(name,'total:',total)
# report_card('zhouhuiquan',93,91,99)
#
# #关键字参数
# def register(name,e_mail,**other):
#     other={'city','home','sex'}
#     print('name:',name,'e_mail:',e_mail,'other:',other)
# register('zhouhuiquan','1030626864@qq.com')
#
# #变量
# def fun():
#     global a
#     a = 20
#     return a+100
# fun() #用之前必须运行fun()函数
# print('a now:', a)

# #读写文件
# def io():
#     f=open('f:/Pycharm/python/1','r')
#     f1=open('f:/Pycharm/python/2','w')
#     # line=f.readlines()
#     for line in f.readlines():
#         char=line.split(' ')
#         f1.write(char[0]+'\n'+char[1])
#     f.close()
#     f1.close()
# io()

# #读文件夹里的文件
# def io_folder():
#     n=1
#     while n<=2:
#         firstname='f:/Pycharm/python/1/'+str(n)
#         secondname='f:/Pycharm/python/2'
#         f=open(firstname,'r')
#         f1 = open(secondname, 'a')
#         for line in f.readlines():
#             f1.write(line)
#         n=n+1
#         f.close()
#         f1.close()
# io_folder()

# #读取操作的区别
# def read_difference():
#     firstname='f:/Pycharm/python/1/1'
#     f=open(firstname,'r')
#     # char=f.read() #整个文本，str类型
#     # char = f.readline() #第一行，str类型,有长度属性,可以被list，以一长度为一个元素
#     char=f.readlines() #所有行，list类型，以第一行为一个元素,有长度
#     print(type(char))
#     print(char)
#     print(len(char))
#     print(char[0])
# read_difference()

# #输入操作
# a=input()
# print('我输入的是：',a)

# #列表操作
# a=['zhou',2,3,4,5]
# a.remove('zhou')
# del a[1]
# a.sort(reverse=True)
# print(a)

# #字典
# dict={'1':'直肠癌','2':'手术'}
# print(dict.get('1'))
# char=list(dict.items())
# print(char)
# for k,v in dict.items():
#     print(k,v)

# #导入模块
# import time as t
# from time import localtime
# print(localtime())

# #while中break/continue
# while True:
#     b= input('type somesthing:')
#     if b=='1':
#         continue
#     else:
#         pass
#     print('still in while')
# print ('finish run')

# #zip/lambda/map
# a=[1,2,3]
# b=[4,5,6]
# # print(list(zip(a,b)))
# for k,v in zip(a,b):
#     k=k/2
#     v=v*2
#     # print(k,v)
# def fun(x,y):
#     return(x+y)
# print(list(map(fun,[1,3],[2,4])))

# #thread
# import threading
# #multiprocessing
# import multiprocessing as mp
# def fun(x,y):
#     # print('PID is',threading.current_thread())
#     print(x,y)
#     # threading.current_thread() 当前运行的线程
#     # threading.active_count() 当前有几个进程
# #     # threading.enumerate() 线程的名字
# def main():
#     p=mp.Process(target=fun, args=(10,2))
#     p.start()
#     p.join()
# #     add_thread=threading.Thread(target=fun)
# #     add_thread.start()
# if __name__=='__main__':
#     main()
#
# import multiprocessing as mp
# def job(q):
#     res = 0
#     for i in range(10):
#         res+=i
#     q.put(res)    #queue
# def job1(q):
#     x=10
#     z=100
#     c=x*z
#     q.put(c)
#
# if __name__=='__main__':
#     q = mp.Queue()
#     p1 = mp.Process(target=job,args=(q,))
#     p2 = mp.Process(target=job1,args=(q,))
#     p1.start()
#     p2.start()
#     p1.join()
#     p2.join()
#     res1 = q.get()
#     res2 = q.get()
#     print(res1+res2)

# import pickle
# pkl文件是打包好的字典文件
# a_dict = {'da': 111, 2: [23,1,4], '23': {1:2,'d':'sad'}}
# # 打包
# file = open('pickle_example.pickle', 'wb')
# pickle.dump(a_dict, file)
# file.close()
#
#
# # 解包
# with open('pickle_example.pickle', 'rb') as file:
#     a_dict1 =pickle.load(file)
#
# print(a_dict1)
import tkinter as tk
window=tk.Tk()
window.title('my window')
window.geometry('400x400')
var=tk.StringVar()
def show():
    var.set('17!up up')
lable=tk.Label(window,textvariable=var,bg='green',font=('Arial',12),width=15,height=2)
button=tk.Button(window,text='hit me',width=15,height=2,command=show)
lable.pack()#放在位置
button.pack()
window.mainloop()