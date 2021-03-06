import codecs
import os
tag2=[]
def character_2_word(input_file, output_file):
    input_data = codecs.open(input_file, 'r', 'utf-8')
    output_data = codecs.open(output_file, 'w', 'utf-8')
    for lines in input_data.readlines():
        if lines == "\n":
            output_data.write("\n")
        else:
            char_tag_pair = lines.strip().split('\t')
            char = char_tag_pair[0]
            tag = char_tag_pair[-1]
            if tag == 'B-operationv':
                output_data.write(char)
            elif tag == 'I-operationv':
                output_data.write(char)
            elif tag=='E-operationv':
                output_data.write(char +'/operationv'+'\t')
            elif tag == 'B-part':
                output_data.write(char)
            elif tag == 'I-part':
                output_data.write(char)
            elif tag == 'E-part':
                output_data.write(char +'/part'+'\t')
            elif tag == 'B-symptom':
                output_data.write(char)
            elif tag == 'I-symptom':
                output_data.write(char)
            elif tag == 'E-symptom':
                output_data.write(char +'/symptom'+'\t')
            elif tag == 'B-medicine':
                output_data.write(char)
            elif tag == 'I-medicine':
                output_data.write(char)
            elif tag == 'E-medicine':
                output_data.write(char + '/medicine' + '\t')
            elif tag == 'B-describe':
                output_data.write(char)
            elif tag == 'I-describe':
                output_data.write(char)
            elif tag == 'E-describe':
                output_data.write(char +'/describe' + '\t')
            elif tag == 'O':
                output_data.write(char + '/O' + '\t')
    input_data.close()
    output_data.close()
if __name__ == '__main__':
    input_file=os.getcwd() + "/secondresult/180valid"
    output_file=os.getcwd() + "/thirdresult/dev.txt"
    character_2_word(input_file, output_file)
