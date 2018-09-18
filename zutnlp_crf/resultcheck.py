import sys
f=open("jisuan","r")
true=0
OtoBI=0
BItoO=0
all=0
line=f.readline()
while line:
    if(line=="\n"):
        line = f.readline()
    else:
        l=line.split("\t")
        if (l[1] in l[2]):
            if "O" in l[1]:
                true=true
            else:
                true=true+1
        else:
            if "O" in l[1]:
               OtoBI=OtoBI+1
            else:
               BItoO=BItoO+1
        line=f.readline()
        all=all+1
P=true/(true+OtoBI)
R=true/(true+BItoO)
F1=(P*R*2)/(P+R)
print("P:"+str(P))
print("R:"+str(R))
print("F："+str(F1))
f.close()