# -*- coding: utf-8 -*-
import CaboCha
parser = CaboCha.Parser()
import MeCab
tagger = MeCab.Tagger('-d /usr/local/lib/mecab/dic/ipadic -u /usr/local/lib/mecab/dic/userdic/ComeJisyoUtf8-2.dic')
