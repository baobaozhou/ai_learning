import codecs
import os
# def character_2_word(input_file, output_file):
#     input_data = codecs.open(input_file, 'r', 'utf-8')
#     output_data = codecs.open(output_file, 'w', 'utf-8')
#     for lines in input_data.readlines():
#         if lines == "\n":
#             output_data.write("\n")
#         else:
#             char = lines.split('\t')
#             output_data.write(char[0])
#     input_data.close()
#     output_data.close()
# if __name__ == '__main__':
#     input_file=os.getcwd() + "/secondresult/600train"
#     output_file=os.getcwd() + "//secondresult/600train1"
#     character_2_word(input_file, output_file)
###

# ##########分词后加上特定标签
# def word(input_file, output_file):
#     input_data = codecs.open(input_file, 'r', 'utf-8')
#     output_data = codecs.open(output_file, 'w', 'utf-8')
#     for lines in input_data.readlines():
#         char=lines.split(' ')
#         lenth = len(char)
#         output_data.write('-DOCSTART-'+'\n')
#         output_data.write(char[0] +' '+'B-part'+'\n')
#         n=1
#         while n< lenth-1:
#             output_data.write(char[n]+' '+'O'+'\n')
#             n=n+1
#     output_data.write('\n')
#     input_data.close()
#     output_data.close()
# if __name__ == '__main__':
#     n = 400
#     counter = 1
#     while counter <= n:
#         count = str(counter)
#         path = './test/'
#         input_file = path + count
#         path2 = './forthresult/'
#         output_file = path2 + count
#         word(input_file, output_file)
#         counter += 1

########去掉错误的列
# def word(input_file, output_file):
#     input_data = codecs.open(input_file, 'r', 'utf-8')
#     output_data = codecs.open(output_file, 'w', 'utf-8')
#     for lines in input_data.readlines():
#         if lines == "\n":
#             output_data.write("\n")
#         else:
#             char=lines.replace('test_text_00000','z')
#             char1=char.split(' ')
#             del char1[1]
#             char2=char1
#             del char2[3]
#             char3=char2
#             str = " ".join([char3[0],char3[1],char3[2],char3[3]])
#             output_data.write(str)
#     input_data.close()
#     output_data.close()
# if __name__ == '__main__':
#     input_file = os.getcwd() + "/030_test.txt"
#     output_file = os.getcwd() + "/test.txt"
#     word(input_file, output_file)

########换成中文
def chose(line):
    if (line.count("B-part") == 1):
        return "解剖部位"
    elif (line.count("B-operationv") == 1):
        return "手术"
    elif (line.count("B-medicine") == 1):
        return "药物"
    elif (line.count("B-symptom") == 1):
        return "独立症状"
    elif(line.count('B-describe')==1):
        return "症状描述"
    else:
        return "other"
def word(input_file, output_file):
    input_data = codecs.open(input_file, 'r', 'utf-8')
    output_data = codecs.open(output_file, 'w', 'utf-8')
    for line in input_data.readlines():
        if line == "\n":
            output_data.write("\n")
        else:
            char = line.split(' ')
            output_data.write(char[0]+' '+char[1]+' '+char[2]+' '+chose(line)+'\n')
    input_data.close()
    output_data.close()
if __name__ == '__main__':
    input_file = './test.txt'
    output_file = './test1.txt'
    word(input_file, output_file)
