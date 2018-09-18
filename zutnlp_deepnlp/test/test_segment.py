#coding=utf-8
from __future__ import unicode_literals

from zutnlp_deepnlp import segmenter

tokenizer = segmenter.load_model(name ='zh')
# n=400
# while
# with open('/home/zutnlp/Desktop/zutnlp/testdata/testdata/入院记录现病史-4.txtoriginal.txt','r',encoding='utf-8')as f:
#     lines=f.readline()
# segList = tokenizer.seg(lines)
# text_seg = " ".join(segList)
# with open('/home/zutnlp/Desktop/test4.txt','w',encoding='utf-8')as z:
#     z.write(text_seg)
n=1
while n<=400:
    filename = "/home/zutnlp/Desktop/zutnlp/testdata/testdata/入院记录现病史-" + str(n) + ".txtoriginal.txt"
    # finalname='/home/zutnlp/Desktop/zutnlp/zutnlp_yuliao/forthresult'
    with open(filename, 'r', encoding='utf-8')as f:
        lines=f.readline()
    segList = tokenizer.seg(lines)
    text_seg = " ".join(segList)
    f=open(str(n),'w')
    f.write(text_seg)
    n=n+1


