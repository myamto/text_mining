# -*- coding: utf-8 -*-
import CaboCha
import MeCab
tagger = MeCab.Tagger('-Ochasen')

## 夏目漱石「こころ」上一より　src="https://www.aozora.gr.jp/cards/000148/files/773_14560.html"
TEXT = "私はその人を常に先生と呼んでいた。だからここでもただ先生と書くだけで本名は打ち明けない。これは世間を憚る遠慮というよりも、その方が私にとって自然だからである。私はその人の記憶を呼び起すごとに、すぐ「先生」といいたくなる。筆を執っても心持は同じ事である。よそよそしい頭文字などはとても使う気にならない。私が先生と知り合いになったのは鎌倉である。その時私はまだ若々しい書生であった。暑中休暇を利用して海水浴に行った友達からぜひ来いという端書を受け取ったので、私は多少の金を工面して、出掛ける事にした。私は金の工面に二、三日を費やした。ところが私が鎌倉に着いて三日と経たたないうちに、私を呼び寄せた友達は、急に国元から帰れという電報を受け取った。電報には母が病気だからと断ってあったけれども友達はそれを信じなかった。友達はかねてから国元にいる親たちに勧まない結婚を強しいられていた。彼は現代の習慣からいうと結婚するにはあまり年が若過ぎた。それに肝心の当人が気に入らなかった。それで夏休みに当然帰るべきところを、わざと避けて東京の近くで遊んでいたのである。彼は電報を私に見せてどうしようと相談をした。私にはどうしていいか分らなかった。けれども実際彼の母が病気であるとすれば彼は固より帰るべきはずであった。それで彼はとうとう帰る事になった。せっかく来た私は一人取り残された。学校の授業が始まるにはまだ大分だいぶ日数があるので鎌倉におってもよし、帰ってもよいという境遇にいた私は、当分元の宿に留まる覚悟をした。友達は中国のある資産家の息子で金に不自由のない男であったけれども、学校が学校なのと年が年なので、生活の程度は私とそう変りもしなかった。したがって一人ひとりぼっちになった私は別に恰好な宿を探す面倒ももたなかったのである。宿は鎌倉でも辺鄙な方角にあった。玉突だのアイスクリームだのというハイカラなものには長い畷を一つ越さなければ手が届かなかった。車で行っても二十銭は取られた。けれども個人の別荘はそこここにいくつでも建てられていた。それに海へはごく近いので海水浴をやるには至極便利な地位を占めていた。私は毎日海へはいりに出掛けた。古い燻ぶり返った藁葺の間を通り抜けて磯へ下りると、この辺へんにこれほどの都会人種が住んでいるかと思うほど、避暑に来た男や女で砂の上が動いていた。ある時は海の中が銭湯せんとうのように黒い頭でごちゃごちゃしている事もあった。その中に知った人を一人ももたない私も、こういう賑やかな景色の中に裹まれて、砂の上に寝ねそべってみたり、膝頭を波に打たしてそこいらを跳ね廻るのは愉快であった。私は実に先生をこの雑沓の間あいだに見付け出したのである。その時海岸には掛茶屋が二軒あった。私はふとした機会からその一軒の方に行き慣なれていた。長谷辺に大きな別荘を構えている人と違って、各自に専有の着換場を拵えていないここいらの避暑客には、ぜひともこうした共同着換所といった風なものが必要なのであった。彼らはここで茶を飲み、ここで休息する外に、ここで海水着を洗濯させたり、ここで鹹はゆい身体からだを清めたり、ここへ帽子や傘かさを預けたりするのである。海水着を持たない私にも持物を盗まれる恐れはあったので、私は海へはいるたびにその茶屋へ一切を脱ぎ棄てる事にしていた。"

def kanji_shiyoritsu(text):  #漢字の使用率を求める
    import re

    kanji_count = 0

    for i in range(len(text)):
        re_kanji = re.compile(r'^[\u4E00-\u9FD0]+$')
        if re_kanji.fullmatch(text[i]) is not None:
            kanji_count = kanji_count + 1

    return kanji_count/len(text)

def sentence_average_length(text): #文の平均の長さ
    return len(text)/len(text.split("。"))

def goji_datsuji(text):  #誤字脱字
    import urllib.request
    import urllib.parse
    import json
    import requests

    API = "https://api.a3rt.recruit-tech.co.jp/proofreading/v2/typo"
    KEY = "DZZ7YKQlkiRT68jZ19tProuty4CtLC3j"

    each_500_char_list=[]
    sentences=""
    for stc in text.split("。"):
        if len(sentence + stc) < 500:
            sentences = sentences + stc + "。"
        else:
            each_500_char_list.append(sentences)
            sentences = stc + "。"

    each_500_char_list.append(sentences)

    goji_datsuji = []

    for text_500_char in each_500_char_list:
        values = {
        'apikey': KEY,
        'sentence':text_500_char,
        'sensitivity':"medium",
        }
        # パラメータをURLエンコードする
        params = urllib.parse.urlencode(values)
        # リクエスト用のURLを生成
        url = API + "?" + params

        #リクエストを投げて結果を取得
        r = requests.get(url)
        #辞書型に変換
        data = json.loads(r.text)

        for alert in data["alerts"]:
            goji_datsuji.append(alert["word"])

    return goji_datsuji

def keijoshi_average(text): #平均系助詞の数
    keijoshi=[]
    keijoshi=[line for line in tagger.parse(text).splitlines() if "係助詞" in line.split()[-1]]

    return len(keijoshi) / (len(text.split("。")) - 1)

def kudokuten(text): #句読点間の平均文字数
    return len(text) / (text.count("、") + text.count("。"))

def kakariuke_average_distance(text): #係り受け平均距離
    return len(text) / (text.count("、") + text.count("。"))



print(kudokuten(TEXT))
