import os
#合并文件
n=1
while n<=400:
    secondname = os.getcwd()+'/testdata/testdata/入院记录现病史-'+str(n)+".txtoriginal.txt"
    secondname1 ="/home/zutnlp/Desktop/test111.txt"
    f1 = open(secondname,"r")
    f2 = open(secondname1, "a")
    for line1 in f1.readlines():
        f2.write(line1)
    n=n+1
# m=401
# while m<=600:
#     name = os.getcwd() + "/firstresult/" + str(n)
#     name1 = os.getcwd() + "/secondresult/" + "200test"
#     f3 = open(name, "r")
#     f4 = open(name1, "a")
#     for line in f3.readlines():
#         f4.write(line)
#     m = m +
# x=1
# while x<=180:
#     endname = os.getcwd()+"/firstresult/"+str(x)
#     endname1 = os.getcwd()+"/secondresult/"+"valid2"
#     f5 = open(endname,"r")
#     f6 = open(endname1, "a")
#     for line in f5.readlines():
#         f6.write(line)
#     x=x+1
# f1.close()
# f2.close()
# f3.close()
# f4.close()
# f5.close()
# f6.close()
