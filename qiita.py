# -*- coding: utf-8 -*-
import sys

import MeCab
tagger = MeCab.Tagger('-d /usr/local/lib/mecab/dic/ipadic -u /usr/local/lib/mecab/dic/userdic/ComeJisyoUtf8-2.dic')

#del sys.modules['MeCab']
del MeCab
del tagger

import CaboCha
parser = CaboCha.Parser()
