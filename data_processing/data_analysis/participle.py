import jieba
import re
from sklearn.feature_extraction.text import TfidfVectorizer
import collections

input_data = './data'
out_data = './new_data'
out_data1 = './new_data1'


def regu():
    with open(input_data, 'r', encoding='utf-8')as f:
        for line in f.readlines():
            new_line = re.findall(u'[\u4e00-\u9fff]+', line)
            with open(out_data, 'a', encoding='utf-8')as f1:
                f1.write(''.join(new_line) + '\n')


def parti():
    with open(out_data, 'r', encoding='utf-8')as f:
        for line in f.readlines():
            new_line = jieba.cut_for_search(line)
            with open(out_data1, 'a', encoding='utf-8')as f1:
                f1.write(' '.join(new_line))


def remove_stopwords():
    stopwords_list = []
    after_stopwords_list = []
    with open('./中文停用词表.txt', 'r', encoding='utf-8')as f:
        for line in f.readlines():
            stopwords_list.append(line.strip('\n'))
    with open(out_data1, 'r', encoding='utf-8')as f1:
        for line in f1.readlines():
            for line2 in line.strip('\n').split(' '):
                if line2 in stopwords_list:
                    continue
                else:
                    after_stopwords_list.append(line2)
    coun = collections.Counter(after_stopwords_list)
    print(coun)


# def tfidf():
#     list = []
#     with open(out_data1, 'r', encoding='utf-8')as f:
#         for line in f.readlines():
#             list.append(line)
#     vectorizer = TfidfVectorizer(min_df=1)
#     vectorizer.fit_transform(list)
#     print(vectorizer.get_feature_names())
#     print(vectorizer.fit_transform(list).toarray())
if __name__ == '__main__':
    remove_stopwords()
