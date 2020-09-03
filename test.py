# -*- coding: utf-8 -*-
TEXT = '私は図書館に行って本を借りた。雪の降り積もった日，祖母は病院で診てもらい,手術は成功した。'
#import MeCab
#tagger = MeCab.Tagger('-d /usr/local/lib/mecab/dic/ipadic -u /usr/local/lib/mecab/dic/userdic/ComeJisyoUtf8-2.dic')
def total_chunk(text):
    import CaboCha
    parser = CaboCha.Parser()
    tree = parser.parse(text)
    chunk_id = 0
    for i in range(0, tree.size()):
        token = tree.token(i)
        if token.chunk != None:
            chunk_id += 1

    return chunk_id


print(total_chunk(TEXT))
