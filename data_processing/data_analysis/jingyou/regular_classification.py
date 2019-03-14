import re
# 保留全部中文
def save_zh():
    with open('processing_opinions_data.txt', 'r', encoding='utf-8')as f:
        for line in f.readlines():
            new_line = re.findall(u'[\u4e00-\u9fff]+', line.strip('\n'))
            with open('data1','a',encoding='utf-8')as f:
                f.write(''.join(new_line)+'\n')
context=[]
with open('data1','r',encoding='utf-8')as f:
    for line in f.readlines():
        context.append(line.strip('\n'))

# def regular():
a=0
b=0
c=0
d=0
e=0
h=0
k=0
l=0
m=0
# 自定义添加无法加工配件
with open('自定义添加无法加工配件','a',encoding='utf-8')as f:
    for line in context:
        if re.match(r'(.*)特种车(.*)自定义',line):
            f.write(line+'\t'+'自定义添加无法加工配件'+'\n')
            context.remove(line)
        elif re.match(r'(.*)不在(.*)加工范围内',line):
            f.write(line + '\t' + '自定义添加无法加工配件' + '\n')
            context.remove(line)
        elif re.match(r'(.*)未(.*)配件(.*)自定义',line):
            f.write(line + '\t' + '自定义添加无法加工配件' + '\n')
            context.remove(line)
        elif re.match(r'(.*)不(.*)资料(.*)自定义',line):
            f.write(line + '\t' + '自定义添加无法加工配件' + '\n')
            context.remove(line)
        elif re.match(r'(.*)无资料(.*)自定义',line):
            f.write(line + '\t' + '自定义添加无法加工配件' + '\n')
            context.remove(line)
        elif re.match(r'(.*)没有(.*)资料(.*)自定义',line):
            f.write(line + '\t' + '自定义添加无法加工配件' + '\n')
            context.remove(line)
        elif re.match(r'(.*)无数据(.*)自定义',line):
            f.write(line + '\t' + '自定义添加无法加工配件' + '\n')
            context.remove(line)
        elif re.match(r'(.*)未采集数据(.*)自定义',line):
            f.write(line + '\t' + '自定义添加无法加工配件' + '\n')
            context.remove(line)
        elif re.match(r'(.*)数据未开放(.*)自定义', line):
            f.write(line + '\t' + '自定义添加无法加工配件' + '\n')
            context.remove(line)
        elif re.match(r'(.*)未有标准名称(.*)自定义',line):
            f.write(line + '\t' + '自定义添加无法加工配件' + '\n')
            context.remove(line)
print(len(context))
with open('自定义添加未加工配件','a',encoding='utf-8')as f:
    for line in context:
        if re.match(r'(.*)未加工(.*)自定义',line):
            context.remove(line)
            f.write(line + '\t' + '自定义添加未加工配件' + '\n')
        elif re.match(r'(.*)未(.*)加工(.*)自定义',line):
            context.remove(line)
            f.write(line + '\t' + '自定义添加未加工配件' + '\n')
        elif re.match(r'(.*)暂无(.*)安排',line):
            context.remove(line)
            f.write(line + '\t' + '自定义添加未加工配件' + '\n')
print(len(context))
with open('自定义添加待加工配件','a',encoding='utf-8')as f:
    for line in context:
        if re.match(r'(.*)已通知(.*)自定义',line):
            context.remove(line)
            f.write(line + '\t' + '自定义添加未加工配件' + '\n')
        elif re.match(r'(.*)暂无(.*)安排',line):
            context.remove(line)
            f.write(line + '\t' + '自定义添加未加工配件' + '\n')