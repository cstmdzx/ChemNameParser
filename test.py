# authored by nklyp
# coding=gbk
import string
import urllib.parse
import urllib.request
import re


def gethtml(url):
    page = urllib.request.urlopen(url)
    url2 = page.read()
    return url2

fileChemForm = open('formular.txt', 'r')
allChemForm = fileChemForm.readlines()

patternSearch = re.compile('<li><a href="(.+)">')


for eachLine in allChemForm:
    eachLine = eachLine.replace('\n', '')
    searchByForm = 'http://webbook.nist.gov/cgi/cbook.cgi?Formula=' + eachLine + '&NoIon=on&Units=SI'
    resultForm = gethtml(searchByForm)
    resultForm = resultForm.decode('gbk')
    findallChemForm = patternSearch.findall(resultForm)
    if findallChemForm.__len__() == 0:#代表没有结果
        continue
    if findallChemForm.__len__() > 1:
        for eachChemFormHtml in findallChemForm:
            eachChemFormHtml = 'http://webbook.nist.gov' + eachChemFormHtml
            print(eachChemFormHtml)
    print(findallChemForm.__len__())
    print('\n')



