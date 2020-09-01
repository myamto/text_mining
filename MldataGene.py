# -*- coding: utf-8 -*-
import numpy as np
import csv
import MldataGeneFunc as func

def main():
    label_ls = []  # 初期化
    text_ls = []  # 初期化
    f_input = open("data/taining_data.csv", 'r')  # fileのopen
    f_output = open("mldata.csv", mode='w')  # 出力するファイルの選択
    data = csv.reader(f_input)  # ファイルの読み込み(str型)
#------------------------------1---------------------------------
    for row in data:
        label_ls.append(int(row[0]))  # ラベルを取得
        text_ls.append(str(row[1]))  # テキストを取得
#------------------------------2---------------------------------
    for i, text in enumerate(text_ls):
        kanji_shiyoritsu = func.kanji_shiyoritsu(text)
        sentence_average_length = func.sentence_average_length(text)
        #goji_datsuji = func.goji_datsuji(text)
        keijoshi_average = func.keijoshi_average(text)
        kudokuten = func.kudokuten(text)

        d=str(rabel_ls[i]) + "," + str(kanji_shiyoritsu) + "," + str(sentence_average_length) + "," + str(keijoshi_average) + "," + str(kudokuten)
        f_output.write(d + "\n")

    f_output.close()

if __name__ == '__main__':
    main()
