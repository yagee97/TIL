# -*- coding:utf-8 -*-
from collections import Counter
from pathlib import Path
import operator

p = Path('./Input_Data').glob('**/*.txt')  # 모든 디렉토리 밑에 있는 text파일만 읽어온다
word_list = []
wordDict = Counter()
noun_list = []

for index in p:
    f = open(index, 'r', encoding='utf-8')
    sentences = f.readlines()  # 한 파일에 있는 모든 문장을 읽어옴
    f.close()

    for sentence in sentences:
        sen = sentence.replace('\n', '')
        for word in sen.split('\t'):
            for temp in word.split('+'):
                if '/NNG' in temp or '/NNP' in temp:
                    wordDict[temp] += 1

dic = {}
for noun, freq in wordDict.most_common(5015):
    dic[noun] = freq

file = open("output.txt", "w", encoding='utf-8')

arr = sorted(dic.items())
sortedArr = sorted(arr, key=operator.itemgetter(1), reverse=True)

for i in range(0, len(sortedArr)):
    for j in range(0, 2):
        file.write(str(sortedArr[i][j])+'\t')
    file.write('\n')

file.close()
