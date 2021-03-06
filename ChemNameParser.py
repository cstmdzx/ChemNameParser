# author = 'nklyp'
# 从ChemName网站上爬取名称，化学式，相对分子质量，结构式
import string
import urllib.parse
import urllib.request
import re
import time


def gethtml(url):
    page = urllib.request.urlopen(url)

    url2 = page.read()
    return url2


patternGetChemName = re.compile(r'<h1 id="Top">(.+)</h1>')
patternGetChemFormula = re.compile(r'Formula</a>:</strong>(.+)</li>')
patternGetMolecularWeight = re.compile(r'Molecular weight</a>:</strong>(.+)</li>')
patternGetChemStructure = re.compile(r'Chemical structure:</strong> <img src="(.+)"')
patternSearch = re.compile(r'<li><a href="(.+)">')

fileRDF = open('chemistry.n3', 'a')
fileChemForm = open('formula2.txt', 'r')
fileError = open('error.txt', 'w')
allChemForm = fileChemForm.readlines()

errorNum = 0
count = 0

for eachLine in allChemForm:
    # 先从文档中拿一个关键词出来
    eachLine = eachLine.replace('\n', '')
    searchByForm = 'http://webbook.nist.gov/cgi/cbook.cgi?Formula=' + eachLine + '&NoIon=on&Units=SI'
    try:
        resultForm = gethtml(searchByForm)
        resultForm = resultForm.decode('gbk')
    except:
        print('爬不到网站')
        time.sleep(60)
    findallChemForm = patternSearch.findall(resultForm)  # 这个关键词的搜索结果

    if findallChemForm.__len__() == 0:  # 代表没有结果 或者只有一个结果被重定向了
        html = resultForm
        # 处理name
        chemNameMatch = patternGetChemName.search(html)
        print(chemNameMatch)
        if chemNameMatch:
            chemName = chemNameMatch.group(1)
        else:
            fileError.write('X\n')
            errorNum += 1
            continue
            # 证明是没有结果，或者这个页面爬错了,

        # 处理分子式
        chemFormulaMatch = patternGetChemFormula.search(html)
        if chemFormulaMatch:
            chemFormula = chemFormulaMatch.group(1)
            chemFormula = chemFormula.replace("<sub>", "")
            chemFormula = chemFormula.replace("</sub>", "")
            chemFormula = chemFormula.replace(" ", "")
            print(chemFormula)
            fileRDF.write(chemName + '  ' + '<http://edukb.org/knowledge/0.1/property/chemistry#ChemicalFormula>' +
                          '  ' + chemFormula + '\n')

        # 处理相对分子质量
        chemMolecularWeightMatch = patternGetMolecularWeight.search(html)
        if chemMolecularWeightMatch:
            chemMolecularWeight = chemMolecularWeightMatch.group(1)
            chemMolecularWeight = chemMolecularWeight.replace(" ", "")
            print(chemMolecularWeight)
            fileRDF.write(chemName + '  ' +
                          '<http://edukb.org/knowledge/0.1/property/chemistry#RelativeMolecularMass>' +
                          '  ' + chemMolecularWeight + '\n')

        # 处理结构式
        chemStructureMatch = patternGetChemStructure.search(html)
        if chemStructureMatch:
            chemStructure = chemStructureMatch.group(1)
            chemStructure = 'http://webbook.nist.gov/' + chemStructure
            print(chemStructure)
            fileRDF.write(
                chemName + '  ' + '<http://edukb.org/knowledge/0.1/property/chemistry#StructureType>' + '  ' + '<' + chemStructure + '>' + '\n')
        fileRDF.write('\n')
        count += 1
        continue
    if findallChemForm.__len__() == 1:  # 代表只有一个结果,还没想好怎么处理
        continue
    if findallChemForm.__len__() > 1:
        for eachChemFormHtml in findallChemForm:
            eachChemFormHtml = 'http://webbook.nist.gov' + eachChemFormHtml
            try:
                html = gethtml(eachChemFormHtml)
                html = html.decode("gbk")
            except:
                print('爬不到化学式')
                # time.sleep(10)
                continue
            # 处理name
            chemNameMatch = patternGetChemName.search(html)
            print(chemNameMatch)
            if chemNameMatch:
                chemName = chemNameMatch.group(1)
            else:
                fileError.write('X\n')
                continue
                # 证明这个页面爬错了

            # 处理分子式
            chemFormulaMatch = patternGetChemFormula.search(html)
            if chemFormulaMatch:
                chemFormula = chemFormulaMatch.group(1)
                chemFormula = chemFormula.replace("<sub>", "")
                chemFormula = chemFormula.replace("</sub>", "")
                chemFormula = chemFormula.replace(" ", "")
                print(chemFormula)
                fileRDF.write(chemName + '  ' + '<http://edukb.org/knowledge/0.1/property/chemistry#ChemicalFormula>' +
                              '  ' + chemFormula + '\n')

            # 处理相对分子质量
            chemMolecularWeightMatch = patternGetMolecularWeight.search(html)
            if chemMolecularWeightMatch:
                chemMolecularWeight = chemMolecularWeightMatch.group(1)
                chemMolecularWeight = chemMolecularWeight.replace(" ", "")
                print(chemMolecularWeight)
                fileRDF.write(chemName + '  ' +
                              '<http://edukb.org/knowledge/0.1/property/chemistry#RelativeMolecularMass>' +
                              '  ' + chemMolecularWeight + '\n')

            # 处理结构式
            chemStructureMatch = patternGetChemStructure.search(html)
            if chemStructureMatch:
                chemStructure = chemStructureMatch.group(1)
                chemStructure = 'http://webbook.nist.gov/' + chemStructure
                print(chemStructure)
                fileRDF.write(chemName + '  ' + '<http://edukb.org/knowledge/0.1/property/chemistry#StructureType>' + '  ' + '<' + chemStructure + '>' + '\n')
            fileRDF.write('\n')
            count += 1
fileRDF.close()
fileChemForm.close()
fileError.close()
print(count)
print(errorNum)
