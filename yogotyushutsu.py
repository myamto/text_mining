# -*- coding: utf-8 -*-
import termextract.mecab
import termextract.core
import collections
import MeCab
import csv
tagger = MeCab.Tagger('-d /usr/local/lib/mecab/dic/ipadic -u /usr/local/lib/mecab/dic/userdic/ComeJisyoUtf8-2.dic')
text = '現在のADLは、寝返り・起き上がりは自立、立ち上がりは修正自立、移乗は介助が必要である。'

# ファイルを読み込む
tagged_text = open("sample.txt", "r", encoding="utf-8").read()
#tagged_text = tagger.parse(text)

# 出力するファイルの選択
f = open("mecab_dic.csv", mode='w')

# 複合語を抽出し、重要度を算出
frequency = termextract.mecab.cmp_noun_dict(tagged_text)
LR = termextract.core.score_lr(frequency,
         ignore_words=termextract.mecab.IGNORE_WORDS,
         lr_mode=1, average_rate=1
     )
term_imp = termextract.core.term_importance(frequency, LR)

# 重要度が高い順に並べ替えて出力
write_list=[]
data_collection = collections.Counter(term_imp)
for cmp_noun, value in data_collection.most_common():
    #print(termextract.core.modify_agglutinative_lang(cmp_noun), value, sep="\t")
    f.write(termextract.core.modify_agglutinative_lang(cmp_noun) + "\n")
f.close()
