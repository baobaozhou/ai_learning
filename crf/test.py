# def toRow():
#     f1 = open('test111.txt', "r")
#     f2 = open('data', "w")
#
#     line = list(f1.readline())
#     n = 0
#     while n < len(line):
#         line[n] = line[n] + "\n"
#         n = n + cpdp_data
#     f2.writelines(line)
#     f2.close()
#     f1.close()
# if __name__=="__main__":
#     toRow()


def toRow():
    f1 = open('test111.txt', "r",encoding='utf-8')
    f2 = open('data', "w",encoding='utf-8')
    line=f1.readlines()
    # # print(line[cpdp_data])
    # for line in f1.readlines():
    #     char=list(line)
    #
    n=0
    while n<len(line):
        char=list(line[n])
        m=0
        while m<len(char):
            char[m]=char[m]+"\n"
            f2.write(char[m])
            m=m+1
        n=n+1
    f2.close()
    f1.close()
if __name__ == "__main__":
    toRow()

