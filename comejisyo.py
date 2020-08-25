# -*- coding: utf-8 -*-
import MeCab
tagger = MeCab.Tagger('-d /usr/local/lib/mecab/dic/ipadic -u /usr/local/lib/mecab/dic/userdic/ComeJisyoUtf8-2.dic')
text = '現在のADLは、寝返り・起き上がりは自立、立ち上がりは修正自立、移乗は介助が必要である。'

#tikan=[]
#for line in tagger.parse(text).splitlines():
#    if "看" in line.split(",")[-1]:
#        tikan.append(line.split("\t")[0])

#for word in tikan:
#    text = text.replace(word, "ケガ")

term_list = open("physiotherapical_term.csv", "r", encoding="utf-8").read()

# 出力するファイルの選択
f = open("physio_term.csv", mode='w')

te=[]
for term in term_list.splitlines():
    #word = termextract.core.modify_agglutinative_lang(cmp_noun)
    parse_result = tagger.parse(term).splitlines()[:-1] #最後のEOSの記述を無視するため-1している
    if len(parse_result) != 1: #分かち書きの結果が１行（分かち書きされない）のものは複合語として既に既存の辞書に登録があるとみなし削除
        f.write(term + "\n")
        #line = u"%s,,,,名詞,一般,*,*,*,*,%s,*,*" % (word,word) #コストは後から算出する
        #line = u"%s,1285,1285,5000,名詞,一般,*,*,*,*,%s,*,*" % (word,word) #コストを入れておくときはこちら
        #f.write(line + "\n")
f.close()
