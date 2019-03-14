import csv
import re
import collections

'''
加载实体类value值
'''


def load_entity_data():
    with open('./origin_data/entity_data', 'r', encoding='utf-8')as f:
        for line in csv.reader(f):
            with open('./deal_data/dict_entity_data', 'a', encoding='utf-8')as f:
                f.write(','.join(line).split(',')[1] + '\t')


'''
加载其他类value值
'''
def load_cpdp_data():
    list = []
    with open('./origin_data/cpdp_data', 'r', encoding='utf-8')as f:
        for line in f.readlines():
            tmp = line.replace('"', '').split(',')
            list.append(tmp)
        del list[0]
        with open('./deal_data/dict_cpdp_data', 'a', encoding='utf-8')as f:
            for i in list:
                if i[0] is None or len(i[0]) == 0:
                    f.write('d' + '\t' + i[0] + '\t' + i[1])
                elif i[1] is None or len(i[1]) == 0:
                    f.write('c' + '\t' + i[0] + '\t' + i[1])
                else:
                    f.write('cd' + '\t' + i[0] + '\t' + i[1])
'''
加载词表
'''
def load_vocab_data():
    list_3=[]
    list_1=[]
    list_2=[]
    with open('./origin_data/synonymyTable.txt','r',encoding='utf-8')as f:
        for line in f.readlines():
            tmp = line.split('\t')
            # print(tmp)
            del tmp[0]
            if len(tmp) == 2:
                list_3.append(tmp[0])
    d=collections.Counter(list_3)
    for k,v in d.items():
        if v > 1:
            list_1.append(k)
    length=len(list_1)
    # 用list存储不同的变量
    for i in range(length):
        list_2.append('')
    with open('./deal_data/dict_vocab_data', 'a', encoding='utf-8')as f_2:
        with open('./origin_data/synonymyTable.txt', 'r', encoding='utf-8')as f_1:
            for line_1 in f_1.readlines():
                temp_1 = line_1.split('\t')
                del temp_1[0]
                if len(temp_1) == 2:
                    if temp_1[0] not in list_1:
                        f_2.write(temp_1[0]+'\t'+temp_1[1].strip('\n')+'\n')
                    elif temp_1[0] in list_1:
                        n = 0
                        while n < length:
                            if list_1[n] == temp_1[0]:
                                list_2[n]+=temp_1[1].strip('\n')+','
                            n=n+1
            for i,j in zip(list_2,list_1):
                temp_2=i.strip(',')
                temp_3=temp_2.split(',')
                temp_4=list(set(temp_3))
                temp_5=','.join(temp_4)
                f_2.write(j+'\t'+i+'\n')

'''
加载模板
'''


def tag_model():
    with open('./origin_data/model', 'r', encoding='utf-8')as f:
        for line in f.readlines():
            word = line.split('\t')[3]
            with open('./deal_data/tag_model_data', 'a', encoding='utf-8')as f:
                if re.match(r'(.*)ComplexProperty(.*)datatype', word):
                    f.write('cd' + '\t' + word)
                elif re.match(r'(.*)ComplexProperty', word):
                    f.write('c' + '\t' + word)
                elif re.match(r'(.*)datatype', word):
                    f.write('d' + '\t' + word + '\n')


'''
构造其他类字典
'''


def bulid_cpdp_dict():
    with open('./deal_data/dict_cpdp_data', 'r', encoding='utf-8')as f:
        tag = ''
        tag_1 = ''
        tag_2 = ''
        for line in f.readlines():
            tmp = line.split('\t')
            if tmp[0] == 'cd':
                tag += tmp[1] + ',' + tmp[2].strip('\n') + '\t'
                dict = {'cd': tag}
            elif tmp[0] == 'c':
                tag_1 += tmp[2].strip('\n') + '\t'
                dict['c'] = tag_1
            elif tmp[0] == 'd':
                tag_2 += tmp[2].strip('\n') + '\t'
                dict['d'] = tag_2
        return dict




'''
构造词表字典
'''
def bulid_vocab_dict():
    dict={}
    with open('./deal_data/dict_vocab_data','r',encoding='utf-8')as f:
        for line in f.readlines():
            tmp=line.split('\t')
            tmp_1 = tmp[1].strip('\n')
            dict.update({tmp[0]:tmp_1})
        return dict





if __name__ == '__main__':
    print(bulid_vocab_dict())
# #     # load_entity_data()
# #     # load_cpdp_data()
#     print(bulid_entity_dict())
#     print(bulid_cpdp_dict())
# #     # tag_model()

