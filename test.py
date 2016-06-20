# authored by nklyp
# coding=gbk


file = open('chemistry.n3', 'r')
lines = file.readlines()
count = 0
for line in lines:
    if line == '\n':
        count += 1
print(count)



