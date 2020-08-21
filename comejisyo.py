# -*- coding: utf-8 -*-
import MeCab
tagger = MeCab.Tagger('-d /usr/local/lib/mecab/dic/ipadic -u /usr/local/lib/mecab/dic/userdic/ComeJisyoUtf8-2.dic')
text = '現在のADLは、寝返り・起き上がりは自立、立ち上がりは修正自立、移乗は介助が必要である。'

print(tagger.parse(text))
