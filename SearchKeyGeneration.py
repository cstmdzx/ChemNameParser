# coding=gbk
# ����һϵ�в�ѯ�õĹؼ���
# author = 'nklyp'

fileForm = open('formula.txt', 'a')
for i in range(1, 50):
    fileForm.write('C' + str(i) + 'H*' + '\n')
fileForm.close()
