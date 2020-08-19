# -*- coding: utf-8 -*-
import termextract.mecab
import termextract.core
import collections

# ファイルを読み込む
tagged_text = open("termextract.txt", "r", encoding="utf-8").read()

# 複合語を抽出し、重要度を算出
frequency = termextract.mecab.cmp_noun_dict(tagged_text)
LR = termextract.core.score_lr(frequency,
         ignore_words=termextract.mecab.IGNORE_WORDS,
         lr_mode=1, average_rate=1
     )
term_imp = termextract.core.term_importance(frequency, LR)

# 重要度が高い順に並べ替えて出力
data_collection = collections.Counter(term_imp)
for cmp_noun, value in data_collection.most_common():
    print(termextract.core.modify_agglutinative_lang(cmp_noun), value, sep="\t")
