# authored by nklyp
# coding=gbk
# 56768

file = open('chemistry3.n3', 'r')
# file3 = open('chemistry3.n3', 'a')
fileChemName = open('name.txt', 'a')
lines = file.readlines()
print(lines.__len__())
count = 0
beyond = 'www'
nxt = 'Ethene, homopolymer'
'''
for line in lines:

    if line == '\n':
        if beyond != subject:
            beyond = subject
            file3.write('\n')
            continue

    splt = line.split('  ')
    subject = splt[0]

    if subject != beyond:
        file3.write(line)
    else:
        continue

'''
for line in lines:
    if line.find('<http://edukb.org/knowledge/0.1/property/chemistry#ChemicalFormula>') != -1:
        splt = line.split('  ')
        subject = splt[0]
        fileChemName.write(subject + '\n')
        count += 1

print(count)
file.close()
fileChemName.close()
# file3.close()



