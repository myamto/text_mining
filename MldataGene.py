# -*- coding: utf-8 -*-
import numpy as np
import csv
import MldataGeneFunc as func
print("hello youtube")

def main():
    #x = []  # 初期化
    #y = []  # 初期化
    #f_input = open("data/data_a.csv", 'r')  # fileのopen
    f_output = open("mldata.csv", mode='w')  # 出力するファイルの選択
    #data = csv.reader(f_input)  # ファイルの読み込み(str型)
#------------------------------1---------------------------------
    '''
    for row in data:
        x1 = []
        y.append(int(row[0]))  # ラベルを取得
        for i in range(1, len(row)):  # 1列目から最後の列まで
            x1.append(float(row[i]))
        x.append(x1)
    x = np.array(x)  # xをnumpy行列に変換
    y = np.array(y)  # yをnumpy行列に変換
    '''
    rabel=1
    text="現在のADLは、寝返り・起き上がりは自立、立ち上がりは修正自立、移乗は介助が必要である。"
#------------------------------2---------------------------------
    kanji_shiyoritsu = func.kanji_shiyoritsu(text)
    sentence_average_length = func.sentence_average_length(text)
    #goji_datsuji = func.goji_datsuji(text)
    keijoshi_average = func.keijoshi_average(text)
    kudokuten = func.kudokuten(text)



    d=str(rabel) + "," + str(kanji_shiyoritsu) + "," + str(sentence_average_length) + "," + str(keijoshi_average) + "," + str(kudokuten)
    f_output.write(d + "\n")

    f_output.close()

if __name__ == '__main__':
    main()
