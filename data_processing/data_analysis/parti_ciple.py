import re

# 保留全部中文
def save_zh():
    with open('data', 'r', encoding='utf-8')as f:
        for line in f.readlines():
            new_line = re.findall(u'[\u4e00-\u9fff]+', line.strip('\n'))
            with open('data1','a',encoding='utf-8')as f:
                f.write(''.join(new_line)+'\n')

# gbk to utf-8
def transla():
    with open('final.txt', 'r', encoding='gbk')as f:
        for line in f.readlines():
            with open('dict', 'a', encoding='utf-8')as f:
                f.write(line)
# 分词
def participle():
    import jieba
    # 加载词典
    jieba.load_userdict('dict')
    # 添加特殊单词
    jieba.add_word('无')
    jieba.add_word('点选')
    jieba.add_word('数据')
    with open('data1','r', encoding='utf-8')as f:
        for line in f.readlines():
            with open('data2', 'a', encoding='utf-8')as f:
                f.write(' '.join(jieba.cut(line)))

# 去掉停用词
def remove_stopwords(sentence):

    stopwords_list = []
    word = ''
    with open('./百度停用词表.txt', 'r', encoding='utf-8')as f:
        for line in f.readlines():
            stopwords_list.append(line.strip('\n'))
    for vocab in sentence.split(' '):
        if vocab not in stopwords_list:
            word+=vocab+' '
    return word

if __name__ == '__main__':
    # save_zh()
    # transla()
    # participle()
    with open('data2','r',encoding='utf-8')as f:
        for line in f.readlines():
            with open('part_data','a',encoding='utf-8')as f:
                f.write(remove_stopwords(line).strip(' '))
