from collections import Counter
from konlpy.tag import Twitter
import pytagcloud

import codecs
# with open('../crop/CSVfile/TSs.txt','r') as txt:

f = codecs.open("../crop/CSVfile/TSs.txt","r","utf-8")
txt = f.read()

nlp = Twitter()
nouns = nlp.nouns(txt)
count = Counter(nouns)

tag2 = count.most_common(20)
taglist = pytagcloud.make_tags(tag2, maxsize=80)
pytagcloud.create_tag_image(taglist, '../static/wordcloud.png', size=(900, 600), fontname='NanumBarunGothicBold', rectangular=False)

f.close()