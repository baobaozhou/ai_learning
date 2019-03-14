from data_deal import *

# '''
# 匹配实体类
# '''
#
#
# def match_entity():
#     dict_1 = bulid_entity_dict()
#     with open('./deal_data/tag_model_data', 'r', encoding='utf-8')as f:
#         for line in f.readlines():
#             tmp = re.findall(u'(?<=\\{{)[^\\}}]+', line)
#             for i in tmp:
#                 if re.match(u'[\u4e00-\u9fff]+', i):
#                     word = dict_1[i].split('\t')
#                     for j in word:
#                         result_str = line.replace('{{', '[').replace('}}', ']').replace(i, j)
#                         with open('./result_data/match_entity', 'a', encoding='utf-8')as f:
#                             f.write(result_str)


'''
匹配有关系的cpdp
'''


def match_cpdp():
    dict_2 = bulid_cpdp_dict()
    with open('./result_data/match_entity', 'r', encoding='utf-8')as f:
        for line in f.readlines():
            tmp = line.split('\t')
            with open('./result_data/match_cpdp', 'a', encoding='utf-8')as f:
                if tmp[0] == 'cd':
                    tmp_1 = dict_2['cd'].split('\t')
                    tmp_1.remove('')
                    for i in tmp_1:
                        tmp_2 = i.split(',')
                        result_str = line.replace('ComplexProperty', tmp_2[0]).replace('datatype', tmp_2[1])
                        f.write(result_str)
                        # print(result_str)
                # if tmp[0]=='c':
                #     tmp_1= dict_2['c'].split('\t')
                #     tmp_1.remove('')
                #     for i in tmp_1:
                #         result_str=line.replace('ComplexProperty',i)
                #         # print(result_str)
                elif tmp[0] == 'd':
                    tmp_1 = dict_2['d'].split('\t')
                    tmp_1.remove('')
                    for i in tmp_1:
                        result_str = line.replace('datatype', i)
                        f.write(result_str)


if __name__ == '__main__':
    match_cpdp()
