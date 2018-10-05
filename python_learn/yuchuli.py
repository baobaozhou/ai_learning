#识别类型的函数
def chose(line):
    if(line.count("解剖部位")==1):
        return "part"
    elif(line.count("手术")==1):
        return "operationv"
    elif (line.count("药物") == 1):
        return "medicine"
    elif (line.count("独立症状") == 1):
        return "symptom"
    else:
        return "describe"
def selectStrat(line):
    str = "".join(line)
    a = str.split('\t', 3)
    return int(a[1])
#返回开始
def selectEnd(line):
    str = "".join(line)
    a = str.split('\t', 3)
    return int(a[2])
#返回结束
def firstStep(line,file):
    n=0
    f=open(file,"w")
    while n<len(line):
        f.write(line[n]+'\t'+'O'+'\n')
        n=n+1
    f.close()
def secondStep(file,start,end,tag,line):
    f = open(file, "r")
    t = f.readlines()
    print(t)
    n = start
    while n < end:
        if n == start:
            t[n] = line[n]+ '\t'+'B-' + tag + '\n'
            n = n + 1
        else:
            t[n] = line[n]+ '\t'+'I-' + tag + '\n'
            n = n + 1
    t[n-1]=line[n-1] + '\t'+'E-' + tag + '\n'
    f = open(file, "w")
    f.writelines(t)
    f.close()
n=1
while n<=600:
    filename = "./chushiwenben/入院记录现病史-" + str(n) + ".txtoriginal.txt"
    txtname = "./chushiwenben/入院记录现病史-" + str(n) + ".txt"
    finalname = "./firstresult/" + str(n)
    f1=open(txtname,"r")
    f2=open(filename,"r")
    line2=f2.readline()
    line1=f1.readline()
    firstStep(line2,finalname)
    while line1:
        # print(line1)
        # print(chose(line1))
        # print(selectStrat(line1))
        # print(selectEnd(line1))
        secondStep(finalname, selectStrat(line1), selectEnd(line1), chose(line1), line2)
        line1=f1.readline()
    n=n+1
    f1.close()
    f2.close()

