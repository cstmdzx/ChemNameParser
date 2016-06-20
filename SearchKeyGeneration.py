# coding=gbk
# 生成一系列查询用的关键词
# author = 'nklyp'

fileForm = open('formula.txt', 'a')
for i in range(1, 50):
    fileForm.write('C' + str(i) + 'H*' + '\n')
fileForm.close()
