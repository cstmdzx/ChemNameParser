# /usr/bin/env python
# coding=utf8

import httplib
import md5
import urllib
import random
import re

fileChemNameTranslation = open('ChemNameTranslation.txt', 'a')
fileName = open('name.txt', 'r')
lines = fileName.readlines()

patternGetTranslation = re.compile(r'"dst":"(.+)"}')

appid = '20160626000023997'
secretKey = 'f_9jwdg80ns5SdsqIhy8'


httpClient = None
myurl = '/api/trans/vip/translate'

fromLang = 'en'
toLang = 'zh'
salt = random.randint(32768, 65536)

httpClient = httplib.HTTPConnection('api.fanyi.baidu.com')





for q in lines:
    httpClient = httplib.HTTPConnection('api.fanyi.baidu.com')
    try:
        print q
        sign = appid + q + str(salt) + secretKey
        m1 = md5.new()
        m1.update(sign)
        sign = m1.hexdigest()
        myurl = myurl + '?appid=' + appid + '&q=' + urllib.quote(
            q) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(
            salt) + '&sign=' + sign
        httpClient.request('GET', myurl)

        # response是HTTPResponse对象
        response = httpClient.getresponse()
        content = response.read()
        translationMatch = patternGetTranslation.search(content)
        translation = translationMatch.group(1)
        translationResult = translation.decode('unicode_escape')
        print translationResult
        translationResult = translationResult.encode('gb2312')
        print translationResult
        fileChemNameTranslation.write(translationResult + '\n')
        httpClient.close()
    except Exception, e:
        print e



fileChemNameTranslation.close()
