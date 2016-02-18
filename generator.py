import re
import collections
import random
import math
import nltk
import string
from nltk.corpus import stopwords

s=set(stopwords.words('english'))
vocablist = [x for x in relcounter.most_common() if x[0] not in s]

jstring = 'var wordlist = ['
for tup in vocablist:
    jstring += "{'word': '" + tup[0] + "', 'count': " + str(tup[1]) + "}, "
jstring = jstring[:-2]
jstring += '];'

f = open('wordlist.js', 'w')
f.write(jstring)