import csv
import unicodecsv as csv
import re
import threading, datetime

from selenium import webdriver
from bs4 import BeautifulSoup as bs


# ------------------------------------------------------------------------------

from collections import Counter
from konlpy.tag import Twitter
import pytagcloud

import codecs



driver = webdriver.PhantomJS('phantomjs-2.1.1-windows/bin/phantomjs')

driver.get('https://search.naver.com/search.naver?where=news&sm=tab_jum&ie=utf8&query=ts%EC%83%B4%ED%91%B8')

html = driver.page_source
soup = bs(html, 'html.parser')


def reLoad():
    wr.writerow([title, day, linke, img])

with open('./CSVfile/TSs.csv', 'wb') as csvfile:
    txt = open('./CSVfile/TSs.txt', 'w', encoding='utf-8')

    wr = csv.writer(csvfile, encoding='utf-8-sig')
    tss = soup.select('ul.type01 > li')
    result = []

    for show in tss:
        title = show.select('a._sp_each_title')[0].get_text().strip().replace(',', '')
        contents = show.select('dl dd')[0].get_text().strip()
        days = show.select('dl > dd.txt_inline')[0].get_text().strip()

        regex = re.compile('\d\d\d\d.\d\d.\d\d|\d\w\s\w')
        day = regex.findall(days)

        linke = show.a.get('href')

        if show.img != None:
            img = show.img["src"]
        else:
            img = None

        txt.write(title)

        reLoad()
        print(title, contents, day, linke, img)

