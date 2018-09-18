import jieba
input_data = r'C:\Users\墨宝宝大撒比\Desktop\data1\1.txt'
output_data = r'C:\Users\墨宝宝大撒比\Desktop\data1\2.txt'
output_data1 = r'C:\Users\墨宝宝大撒比\Desktop\data1\3.txt'
with open(input_data,'r',encoding='utf-8')as f:
    for line in f.readlines():
        char=line.split('\t')
        seg_list = jieba.cut(char[3], cut_all=False, HMM=True)
        res = " ".join(seg_list)
        with open(output_data1,'a',encoding='utf-8')as f1:
            f1.write(res)
# input_data = r'C:\Users\墨宝宝大撒比\Desktop\data1\1.txt'
# output_data = r'C:\Users\墨宝宝大撒比\Desktop\data1\2.txt'
# with open(input_data,'r',encoding='utf-8')as f:
#     for line in f.readlines():
#         char=line.split('\t')
#         with open(output_data,'a',encoding='utf-8')as f1:
#             f1.write(char[2]+'\n')