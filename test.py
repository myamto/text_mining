# -*- coding: utf-8 -*-

text = '現在のADLは、寝返り・起き上がりは自立、立ち上がりは修正自立、移乗は介助が必要である。'

import CaboCha
parser = CaboCha.Parser()
tree = parser.parse(text)
chunkId = 0
for i in range(0, tree.size()):
    token = tree.token(i)
    if token.chunk != None:
        print(chunkId, token.chunk.link, token.chunk.head_pos,
            token.chunk.func_pos, token.chunk.score)
        chunkId += 1

    print(token.surface, token.feature, token.ne)
