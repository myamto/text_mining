# -*- coding: utf-8 -*-
TEXT = '私は図書館に行って本を借りた。雪の降り積もった日，祖母は病院で診てもらい,手術は成功した。'

import MeCab
tagger = MeCab.Tagger('-d /usr/local/lib/mecab/dic/ipadic -u /usr/local/lib/mecab/dic/userdic/ComeJisyoUtf8-2.dic')
def total_chunk(text):
    #import CaboCha
    #parser = CaboCha.Parser()
    tree = parser.parse(text)
    chunk_id = 0
    for i in range(0, tree.size()):
        token = tree.token(i)
        if token.chunk != None:
            chunk_id += 1

    return chunk_id

def total_chunk2(text):
    from pyknp import KNP
    knp = KNP()
    result=knp.parse(text)
    num=0
    for bnst in result.bnst_list():
        if not "".join(mrph.midasi for mrph in bnst.mrph_list()) == "None":
            print("".join(mrph.midasi for mrph in bnst.mrph_list()))
            num+=1

    return num

#print(total_chunk2(TEXT3))
