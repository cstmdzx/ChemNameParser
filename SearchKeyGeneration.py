# coding=gbk
# 生成一系列查询用的关键词
# author = 'nklyp'

fileForm = open('formula2.txt', 'a')
for cn in range(1, 50):
    # 检索词生成，主要涉及烷烃，以及加入氧原子，氯原子，溴原子的化学式
    # 同时考虑一下包含两种的情况
    for hn in range(2, (2 * cn + 3)):
        if hn % 2 == 1:
            continue
        fileForm.write('C' + str(cn) + 'H' + str(hn) + '\n')
        fileForm.write('C' + str(cn) + 'H' + str(hn) + 'O?' + '\n')
        # fileForm.write('C' + str(cn) + 'H' + str(hn) + 'O2' + '\n')
        '''
        if hn > 2:
            fileForm.write('C' + str(cn) + 'H' + str(hn - 1) + 'Cl' + '\n')
            fileForm.write('C' + str(cn) + 'H' + str(hn - 2) + 'Cl2' + '\n')
            fileForm.write('C' + str(cn) + 'H' + str(hn - 3) + 'Cl3' + '\n')
            fileForm.write('C' + str(cn) + 'H' + str(hn - 4) + 'Cl4' + '\n')
        if hn > 2:
            fileForm.write('C' + str(cn) + 'H' + str(hn - 1) + 'Br' + '\n')
            fileForm.write('C' + str(cn) + 'H' + str(hn - 2) + 'Br2' + '\n')
            fileForm.write('C' + str(cn) + 'H' + str(hn - 3) + 'Br3' + '\n')
            fileForm.write('C' + str(cn) + 'H' + str(hn - 4) + 'Br4' + '\n')
        '''
    fileForm.write('C' + str(cn) + 'H*' + 'Cl?' + '\n')
    fileForm.write('C' + str(cn) + 'H*' + 'Br?' + '\n')
    fileForm.write('C' + str(cn) + 'H*' + 'Cl?O?' + '\n')
    fileForm.write('C' + str(cn) + 'H*' + 'Br?O?' + '\n')
    # fileForm.write('C' + str(cn) + 'H*' + '\n')
fileForm.close()
