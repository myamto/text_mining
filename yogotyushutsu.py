# -*- coding: utf-8 -*-
import termextract.mecab
import termextract.core
import collections
import MeCab
import csv
tagger = MeCab.Tagger('-d /usr/local/lib/mecab/dic/ipadic -u /usr/local/lib/mecab/dic/userdic/ComeJisyoUtf8-2.dic')
text = '主訴は「手足が動きにくく、歩けない」である。これを足がかりに問題点をまとめてみる。本症例は左中大脳動脈梗塞であり、内包が障害されることから右側に重篤な運動麻痺や、皮質性の感覚障害がでると予想される。まず、心身機能、身体構造の問題点を統合していく。BRSTから上肢、手指かステージⅡ、下肢がⅢである。深部腱反射が右上下肢3＋であり、アシュワーススケールも上下肢2である。筋緊張については動作時に全体的に亢進している。さらに病的反射であるホフマン、トレムナー、バビンスキー反射が陽性であることから錐体路障害が確認できる。感覚は右半身の表在、深部ともに鈍麻レベルである。高次脳機能では失語がある。以上のことから機能面でまとめると、（1）片麻痺による運動障害、（2）感覚障害、（3）失語のある左中大脳動脈梗塞の症例となる。そこから問題点をICFに置き換えて整理すると1.b7601（複雑な随意運動の制御）、2.b7352（身体の片側の筋緊張）となる。活動面ではd4200（乗り移り）などが考えられる。本症例の心身機能、身体構造の問題点の順位は1番が片麻痺による運動障害、次に感覚障害、高次脳機能障害の順と考える。感覚と高次脳機能障害は今後の検査や症状の回復により入れ替わる可能性がある。寝返りと起き上がりは自立している。立ち上がりは手すりによる物的介助があれば可能レベル。トランスファーは手すりがあれば車椅子からベットは可能、ベットから車椅子は介助、監視レベルである。トイレ動作はトランスファー半介助レベルである。歩行はAFO着用で平行棒内介助レベルである。本症例では内包が圧迫されており、錐体路障害を呈している。文献4で言われているように本症例においても、BRSがⅡまたはⅢレベルであり、筋緊張やDTRに異常が出ており錐体路徴候がみられ、その症状を主体として基本動作能力が低下している。①複雑な随意運動の制御②身体の片側の筋緊張この2点からADL能力低下が認められる。左中大脳動脈梗塞は文献（7）より、通常は身体一側の脱力、不器用さ、または重い感じを示す。麻痺は運動の障害を意味し、もっとも頻度の高い症状が麻痺である。中大脳動脈の閉塞によって前頭葉の運動中枢が壊死するか、脳幹の梗塞で錐体路が壊死するかで発症する。本症例はBrnnstrom recavary stageの検査結果より上肢・手指がIIレベル、下肢がⅢレベルであり随意運動の制御が行えないことがわかる。また他部門からの情報より、上肢の麻痺は重篤であり、廃用手だと思われる。さらに、筋緊張検査結果からAshwarthスケール上下肢ともに2で、動作時には全体的に筋緊張が亢進することから、動作を行う際には筋緊張が亢進しうまく動作が行えないことがわかる。これらのことよりADL検査の結果、セフルケア・更衣・食事・入浴・トイレ動作・歩行に介助を要していると考える。そのため、運動麻痺を軽減させ筋緊張を低下させることで上肢・手指での動きの制限が少なくなればADL動作の自立度も上がり、自宅復帰の際にキーパーソンである夫の介助量も軽減できると考える。　移動において、自操は可能なものの右側に寄る傾向があるため病棟内でも困難があるが、これも右上肢の随意運動の制御ができず、また筋緊張も亢進しているため細かな動作が行えず右側に寄る傾向があるのではないかと考える。自宅では車椅子での生活が可能とあるが、自宅の廊下などは病棟内のりも狭いことが予測され壁に衝突してしまう恐れが予想される。しかし、介助があれば4点杖で介助歩行可能なため、下肢の運動麻痺を軽減させるとともに下肢筋力増強を行い、介助なしの4点杖歩行可能を目標とする。　また、合併症に高血圧があり身長165cmで体重が60kgあることから軽度肥満傾向にあるため、有酸素運動や食事改善を行うのがよいと考える。　患者は発症後どのくらいの期間経過しているか情報からはわからないが、もし発症後間もないならば年齢が75歳とまだ年齢的にも回復の見込みがあることから、早期より起立ー着席訓練や歩行訓練などの下肢訓練の量を多くするとともに有酸素運動トレーニングもしくは有酸素運動などを、積極的に実施する。文献（12）（15）より、「起立─着席訓練や歩行訓練などの下肢訓練の量を多くすることは、歩行能力の 改善のために強く勧められる」「有酸素運動トレーニングもしくは有酸素運動と下肢筋力強化を組み合わせたト レーニングは、有酸素性能力、歩行能力、身体活動性、QOL、耐糖能を改善す るので強く勧められる。」とあることから、下肢筋力増強と有酸素運動or有酸素運動トレーニングを行い、歩行能力・身体活動性・QOLの改善を図る。本症例は１ヶ月半前に左中大脳動脈梗塞を発症された70歳代の女性である。合併症としては高血圧があり、理学療法実施中には注意する必要がある。本人の全体像としては、意識は清明であり、コミュニケーションは運動性失語があり困難であるが、こちらの指示は通っていると思われる。看護師からの情報では性格は比較的穏和である。医師からの情報では、上肢の麻痺が重篤であり、下肢も筋緊張が高いが、年齢が若いため麻痺の回復が期待できることから理学療法は積極的に実施してほしいとのことである。現在の動作の寝返り、起き上がり自立、立ち上がりは手すりがあれば可能、トランスファーは手すりがあれば車椅子からベッドは可能でベッドから車椅子は介助・監視レベルである。移動は車椅子で自操可能であるが、右側による傾向があるために病棟内でも困難である。また、トイレ動作でトランスファーは半介助、食事はセッティング必要、入浴は全介助、更衣は半介助である。本症例の主訴は「手足が動きにくく、歩けない。」であり、歩行に関しては現在、AFO装着で平行棒内介助レベルで、セラピストの介助があれば4点支持杖で介助歩行可能である。まず、ベッドから車椅子のトランスファーについては、運動麻痺、筋緊張亢進が関係していると考えられる。BRST上肢・手指Ⅱであり、関節運動を伴う筋収縮ができない、下肢Ⅲで共同運動の出現、分離運動が出来ないためであると考えられる。車椅子の移動で右側による傾向があるのは、上肢Ⅲであるため、操作の調節がうまく出来ていないと考えられる。本症例は左中大脳動脈梗塞であり、深部腱反射は右側じょうかし+++、病的反射+となっており錐体路徴候の特徴がでている。特に上下肢ともに麻痺があり上肢の麻痺が強い。筋緊張は上下肢共に亢進している。感覚も右上下肢体幹鈍麻レベルであり、感覚麻痺も呈している。高次脳機能は失語があるがこちらの指示は通っている。活動ではトランスファーに異常があり、特にベッド→車椅子は介助・監視レベルである。トイレ動作も半介助であり問題となっている。車椅子からベッドへの移動は可能であることから下肢筋力はあまり問題にならないことが考えられる。よって、トランスファーにおいて主な原因として、筋緊張の亢進と感覚障害とBRSTが上肢、手指が2、下肢3であることが考えられる。車椅子への移動はベッドへの移動よりも座る場所が限定されていることにより正確な動作が必要となるが筋緊張が亢進し、下肢BRSTが3であり共同運動が出ているため正確な動作が行えていない。また、感覚麻痺もあるため自分の体がどうなっているのかの判断ができていない。さらに、上肢、手指のBRSTが2であることから手すりを使った支持も難しくなっていると考えられる。本症例は左中大脳動脈梗塞を2019年9月25日に発症した75歳女性である。    検査データから右側病的反射が陽性、深部腱反射は3＋なので錐体路障害の存在が明らかである。BRSから上肢・手指が2、下肢が3である。OTの情報から上肢は廃用手であると考えられているため、アプローチとしては下肢がメインとなる。筋緊張について、Ashworthは上肢・下肢共に2で、動作時には全体的に筋緊張が亢進するとのことである。感覚は右側半身が鈍麻で、動作じの感覚が認識されにくい。基本動作では立ち上がりが手すりがあれば可能、トランスファーは手すりありならば車椅子からベッドは可能だが、ベッドから車椅子は介助・監視レベルである。ADLで特に問題となるのはトイレ動作においてのトランスファーが半介助であることである。1日辺りの回数が多く、介助する側への負担が大きいため第一に解決したい。   まずは運動麻痺について考える。上肢はOTから廃用手とのことなので、アプローチは難しいので下肢へのアプローチが中心となる。現在1ヶ月半ほどなので、回復の余地はあると考え、脳卒中ガイドラインで「下肢の筋力トレーニングは筋力を増加させ、身体機能の改善に良い」「下肢訓練の量を増やすと歩行能力の改善に効果的」とあり、下肢の訓練は非常に効果的であるとされているため、治療の中心は下肢訓練となる。とくにトランスファーの訓練を増やす。トランスファーができると生活の幅が広がるため、まずは自立したい。ベッドから車椅子へのトランスファーが難しいとあり、原因が分からないが、その状況に似せた環境で立ち上がり、方向転換、座るの一連の動作を行う。特にトイレでのトランスファーで半介助なので、トイレの環境に似せた状況を想定したい。   次の問題としては移動である。車椅子で自走可能なものの、右側に寄ってしまうとのことなので危険である。原因としてはBRSの数値が低いことである。本症例は、発症から一ヶ月半の左中大脳動脈梗塞であり、合併症として高血圧症がある。主訴は、「手足が動きにくく、歩けない」であるので、この主訴を中心とし動作と問題点を以下に記載していく。本症例は、BRST:上肢II、手指II、下肢Ⅲの右片麻痺患者である。また、病的反射も陽性であり、錐体路徴候を示す所見もそろっている。このことから、手足が動きにくい原因となっているのは、運動麻痺が原因となっていることが考えられる。また、アシュワーススケール上下肢ともに2と筋緊張が亢進しており、動作時には全体的に筋緊張が亢進することから、筋緊張異常も手足が動きにくい原因として挙げられる。次に活動面にについて記載する。主訴として、歩けないことを訴えているので、なぜ歩けないのかについて考える。理由としてあげられるのが、運動麻痺、筋緊張異常、感覚障害があげられる。運動麻痺については、BRST:下肢Ⅲと共同運動パターンが見られるため、歩けない原因として挙げられる。また、筋緊張異常は、アシュワーススケール下肢が2とあり、筋緊張が亢進しているため、こちらも原因としてあげられる。感覚障害は、右側上下肢、体幹が表在、深部ともに鈍麻レベルであり、歩行の際に踏み出しが怖かったり、踏み出す足の位置の感覚がわからないなど歩行を妨げる原因となると考えられる。また、基本動作では、トランスファーが、ベッドから車椅子は介助・監視レベル、であり、ADLは、セルフケア、入浴、トイレ動作に介助が必要であり、歩行については、AFO装着で平行棒内介助レベルである。これらの原因としても運動麻痺、感覚障害、筋緊張異常がかんがえられる。運動麻痺については、年齢が若く、下肢は、一ヶ月半でⅢと今後回復が期待される。歩行やトランスファーを行うために、運動麻痺や筋緊張異常の回復を待つだけでなく、筋力増強トレーニング、関節可動域練習をすることで、歩行やトランスファーを獲得できるようにすべきと考える。以上のことから運動麻痺、筋緊張異常、感覚障害を中心にアプローチしていくとともに、筋力トレーニングや、関節可動域練習なども行なっていくべきだと考える。本症例は、左中大脳動脈梗塞である。主訴に、｢手足が動かしにくく、歩けない｣とある。この原因について、他部門からの情報により、反対側上肢の重篤な麻痺、下肢の筋緊張亢進、また理学的検査から、反対側上下肢の感覚鈍麻などが見られることが考えられる。これらの症状は診断名である中大脳動脈梗塞より起こり得るものである。現在発症から5週間が経過しておりこれらの症状が確認されることから、歩行の自立は可能性が低いと考えた。これによりワイ氏の今後の移動手段は車椅子になると考えた。さらに、主訴より、移動に制限がある事がひとつの問題として解釈できるため、トランスファーの自立をゴールとして設定できると考えた。とくに、ベットから車椅子の移乗動作が自立すれば介助量が減少するとができる。病棟内での移動は右による傾向があるため、危険でありここには介助が必要である。①深部腱反射:右側上下肢+++②感覚:右側上下肢・体幹　表在・深部ともに鈍麻レベル(③ BRS 上肢Ⅱ)　この2つ(3つ)から、右側の上肢が廃用手であると考えられる。文献(4)から詰まった動脈の反対側の片麻痺(特に上肢)や知覚麻痺、視力障害などが起こります。とあるように今回の症例は左中大脳動脈梗塞のため、反対側である右側の片麻痺や知覚麻痺、視力障害が起こると考えられる。しかし、医師からの情報にもあるように、75歳と若いため、麻痺の回復は見込めると予測して、理学療法を積極的に行うべきだと考える。　そして文献(8)から、感覚の鈍麻または消失が起こるほか、慢性期には疼痛が出現することがあり、QOLへの影響が大きい。とあり、今回の症例は感覚が表在深部ともに鈍麻レベルであり、ADL動作もセルフケアが半介助であることから、QOLは下がりつつあるものだと考えられる。　また、文献(7)から、身体一側の脱力、不器用さ、または、重い感じを示す。とあるように、身体の右側に上記のような症状が起きていると考えられる。しかし、手の巧緻性の向上、アプローチで、右側の改善を促し、基本動作は手すりがあれば基本的に可能であり、身体の左側を使うことも可能であることから軽減すると考えられる。本症例は約1ヶ月前に左中大脳動脈梗塞を発症された75歳の女性である。このことから、急性期は過ぎ回復期へと移行していると思われる。よって、検査からもあるように、筋緊張が低下している時期からは脱出して、亢進していることがAshwarthスケールの結果から読み取れる。筋緊張が上がると筋肉は収縮位をとりやすく、脱力しにくい状態になる。よって、麻痺側の下肢において、大きい筋肉である下腿三頭筋の収縮により足関節底屈位をとりやすくなっており、立位時に右下肢の足底面を床に接地させることは困難である可能性があるため、立位を保持するにあたり支持基底面の確保が難しくなり、立位保持が難しいことが可能性として考えられる。また、右側の下肢において表在感覚と深部感覚がともに鈍麻していることから足底の表在感覚や、位置覚が鈍いため荷重をかけることへの不安感や、かけ方が分からなくなってしまうことから左下肢にたよって立位をとろうとするものと考える。なので、左下肢の筋力があれば立位の保持はある程度の安定性が獲得出来ると思われる。　本症例は約1ヶ月半に左中大脳動脈を発症された70代女性である。合併症としては高血圧があり、現在は服薬にて血圧はコントロールされている。　本人の全体像として意識は清明であり、理学療法時の血圧は問題ないが、運動性失語があるため、コミュニケーションが困難である。現在、寝返り、起き上がりは自立、立ち上がりは手すりを使用して可能、ベッドから車椅子へのトランスファーでは介助、監視レベルである。　まずは、下記に現在の動作と機能面の問題点をあげていく。　立ち上がりで手すりがないと行えないのは運動麻痺が関係していると思われる。BRSTを行うと上肢Ⅱ、手指Ⅱ、下肢Ⅲとなり、下肢では、共同運動が見られた。「通常は身体一肢の脱力、不器用さ、または重い感じを示す。麻痺は運動の障害を意味し、もっとも頻度の高い症状である。」とされており、本症例においても運動麻痺が見られているため典型的な症例であるといえる。　感覚検査より、右側の上下肢体幹に表在深部感覚の鈍麻がみられた。ベッドから車椅子へのトランスファーで介助、監視を要することについてもこの運動麻痺とそれに加えて感覚障害が生じていることも関係していると思われる。中大脳動脈梗塞により重度の運動麻痺がでるとされる。BRST: 上肢Ⅱ、手指Ⅱ、下肢Ⅲより立ち上がり、トランスファーが自立できない要因になっている可能性がある。ADL動作も麻痺が原因となり介助が必要になっている可能性がある。感覚麻痺鈍麻より自身の体がどこにあるかわからず基本動作、ADLが介助が必要になっている可能性がある。寝返り・起き上がりは自立しており、立ち上がりは手すりがあれば可能である。次にトランスファーについては手すりがあれば車椅子からベッドへ移ることは可能だがベッドから車椅子は介助・監視が必要である。基本動作の段階としてできない段階がトランスファーであり、トランスファーができればトイレ動作が可能になる。本症例は発症から1ヶ月半経過した75歳の女性で、左中大脳動脈の梗塞である。意識は鮮明であり運動性失語があるが、こちらの説明内容はほとんど理解しているとあるため、理学療法の大きな阻害因子とはならないと考える。そして現在投薬により血圧は調節されているが、出血性梗塞の危険性があるために、リハビリの際はアンダーソンの基準に従って血圧に注意しながら理学療法を実施する必要があると考える。 理学療法評価に着目すると、BRSが上肢Ⅱ、手指Ⅱ、下肢Ⅲであり、深部腱反射の情報から右側の筋緊張が亢進した片麻痺が生じている。そして病的反射が陽性であるため、錐体路障害があることがわかる。つまり本症例は中大脳動脈が梗塞する事で内包がやられており、また中大脳動脈が支配している部位も梗塞のより栄養が届いていないことが想定される。それらの原因と感覚障害によって基本的動作能力の低下が起きていると考える。 一般的に麻痺は、発症からなるべく早くリハビリを開始することと、年齢が若いことが麻痺の回復の程度に関与すると言われている。本患者は年齢が75歳と比較的若いため、積極的に理学療法を実施することで麻痺はある程度回復すると考える。そして本症例は主訴で手足が動かしにくく、歩けないと述べている。そのためできれば実用性のある歩行レベルを獲得させたいが、現在の歩行レベルはAFOを用いての平行棒内介助レベルとそれほど高くない。しかし一般的に麻痺はBRSのレベルが二段階ほど回復することが多いため、本症例に関しても下肢のBRSは5まで回復する可能性があるため、道面らの予後予測によるとBRSが5ならば屋外歩行が自立とあるため、長期ゴールとして杖を用いて屋外歩行自立、道具を使わず屋内歩行自立を目指したい。しかし基本動作獲得としては歩行よりもトランスファーの獲得を目標したいと考える。なぜなら家屋環境を見たとき自宅は車椅子での生活が可能であるということから、もし歩けないとしても自宅で車椅子が利用できる。だからトランスファーができるかできないかで本患者の帰宅後の生活範囲が大きく変わると考える。そのため短期ゴールとして、トランスファーの自立も目指したい。その動作の阻害因子となると考える麻痺の程度、筋緊張亢進、感覚障害にアプローチしながら理学療法を実施していきたいと考える。　本症例は高血圧を起因とした左中大脳動脈梗塞である。年齢は75歳、身長165cm、体重60kgの女性である。全体像として、他部門情報より、比較的穏和な性格であり、血圧も薬によって調節されている。運動性失語のためコミュニケーションは困難である。主訴は『手足が動きにくく、歩けない』である。検査結果から想起される問題点とアプローチの優先順位を以下に記載する。　本症例のは手足が動かしにくいという異常現状がみられる。検査結果より、病的反射である、ホフマン、トレムナー、バビンスキー反射全てが陽性であり、深部腱反射も上下肢ともに＋＋＋であることから、錐体路徴候があると思われる。よって、上位運動ニューロンの障害によって症状が出ていると思われる。　検査結果より、筋緊張はアシュワーススケールより、上下肢共に2であり、筋緊張の亢進を認める。また、感覚は、上下四肢、体幹、表在、深部共に鈍麻レベルである。この２つが動作に大きく影響していると考えた点を以下に記載する。　検査結果より、立ち上がり、トランスファー、は、手すりがあれば可能である。ゆえに、健側上下肢の筋力はあると思われる。しかし、立位バランスが保てないため健側上肢でバランスを取って立ち上がっていると考えた。よって、左下肢に原因があり、バランスが保てないといえる。原因として、①共同運動パターンによるもの、②筋緊張異常、③左側の感覚が全て鈍麻であることが挙げられた。①について、共同運動パターンにより、クリアランスの確保、下肢の振り出しがうまく行えておらず、転倒の恐怖による影響があると考えた。②については、アシュワース2であり、筋緊張が亢進している。ゆえに、滑らかな正常歩行周期が、上手く行えず、異常歩行を生み出していると思われる。③について、感覚鈍麻により、足底接地のタイミングが分からず転倒の恐怖を生み出していると考える。上記の内の、②と③が混在することで、左下肢のフィードバックができず、トランスファーや歩行に介助を要してると考える。活動について、本症例はブルンストローム下肢2であるり道免らの予後予測により、麻痺の回復は本患者の年齢と照らし合わせると、2段階の回復が考えられる。ゆえに、長期ゴールを下肢のブルンストローム5と考え、一本杖屋外歩行自立とした。　本症例の主訴である「手足が動きにくく、歩けない」をもとに統合と解釈を行う　本症例の主訴に関与する検査結果はBRS下肢Ⅲ、深部腱反射 右側下肢＋＋＋、バビンスキー反射＋、Ashwarthスケール 下肢2、感覚 下肢表在・深部ともに鈍麻レベルである。これらの検査結果より本症例の疾患像を考察すると、1.運動麻痺、2.錐体路兆候、3.錐体外路兆候、4.筋緊張亢進、5.感覚障害、が見られる症例となる。　これらの情報と主訴の関係を考察すると、主訴の手足の動かしにくさは運動麻痺による分離運動不十分、筋緊張亢進による下肢の操作性困難、感覚障害による筋発揮困難によるものと考える。本症例はBRSⅢの情報より分離運動が不十分であることがうかがえる。また、BRSⅢ・Ashwarthスケールの情報より筋緊張の高さがうかがえる。これら二つがある状態では下肢の操作性は困難なものとなり、動作における随意運動は行いにくくなると考える。また、基本動作における介助ないしは半介助が伴う検査項目には立位を要するものが多く、立位状態では足底の感覚フィードバックによる筋収縮がなくては姿勢制御ができず、動作困難に繋がると考える。　以上より、本症例の問題点は1.複雑な随意運動の制御、2.身体片側の筋緊張と考える。優先順位に関しては、随意運動の制御には筋緊張の亢進が阻害因子の一つになることから2.身体片側の筋緊張が本症例では優先となると考える。　活動の問題点は本症例の主訴は歩きにくさに関係するものであることから代替手段として他の移動手段の獲得が優先となると考える。なので、基本動作より介助を要する1.乗り移りが活動の問題点として挙げられる。　統合より本症例の問題点は身体片側の筋緊張であることが示唆された。筋緊張に関して文献を用いて考察する。　文献6より、中大脳動脈梗塞では内包が障害されやすいことが示唆される。本症例においても内包が障害されており、一般的な症例であることがうかがえる。また、文献7より、運動麻痺が生じやすいことが示唆され、本症例でも運動麻痺が確認されており、本症例でも筋緊張に影響を与えやすいことがうかがえる。文献7では不器用さなどを訴えやすいとあり、これが主訴の動かしにくさに関与しているとも考える。本症例は左中大脳動脈梗塞であり、発症から1ヶ月が経過した症例である。主訴は「手足が動きにくく、歩けない。」であるため、その原因について統合を進めていく。BRSTは上肢・手指共にIIであり下肢はⅢレベルである。深部腱反射は右側上下肢共+++である。ホフマン反射、トレムナー反射、バビンスキー反射も陽性であることから錐体路徴候を示す所見がみられる。また、筋緊張は上下肢共に2であるが、動作時に全体的に筋緊張が亢進する。感覚については右側上下肢・体幹は表在・深部共に鈍麻レベルである。高次脳機能障害は失語があり、コミュニケーションが困難だが、こちらの話す内容はほとんど理解している。以上のことから基本動作について考える。寝返り・起き上がりは自立している。立ち上がりは手すりがあれば可能である。トランスファーは手すりがあれば車椅子→ベッドは可能、ベッド→車椅子は介助・監視レベルである。ベッド→車椅子は介助・監視が必要なレベルとして考えられることは、運動麻痺、動作時の筋緊張亢進、感覚鈍麻、などが考えられる。ADL検査はセルフケア軽介助、更衣は半介助、食事はセッティングが必要、入浴は全介助、トイレ動作はトランスファーは半介助、移動は車椅子で右側に寄る傾向がある。歩行はAFO装着で平行棒内介助レベルである。階段は不可能である。以上のことから心身機能の問題点として1.複雑な随意運動の制御（b7601）、2.触知覚（b1564）が挙げられる。また活動に関しては、1.乗り移り（d4200）を挙げる。本症例では発症から1ヶ月が経過しBRST上肢・手指Ⅱ、下肢Ⅲレベルであり75歳の患者であるため、上肢は実用手になるまで回復することは見込めないが、運動麻痺麻痺の改善として脳卒中ガイドライン2015によれば「麻痺側下肢の筋力トレーニングは、下肢筋力を増加させ、身体機 能を改善させるので勧められる」ため下肢の筋力トレーニングが有効であると考えられる。また、歩行に関しても脳卒中ガイドライン2015によると「立─着席訓練や歩行訓練などの下肢訓練の量を多くすることは、歩行能力の 改善のために強く勧められる」ことから下肢の筋力トレーニングを主として考えていく必要がある。この症例は、左中大脳動脈に梗塞のある75歳女性のものである。合併症に高血圧を有しているが、現在は薬で調整されている。理学的検査から、BRSが上肢・手指ともにⅡであり、重篤な麻痺が出現していると考えられる。深部腱反射は、右上下肢ともに亢進し、病的反射も出現していることから、錐体路に障害が及び、知覚の伝導路にも影響が出ている。筋緊張の亢進は、Ashwarthスケール2から分かるように顕著に示しており、心身機能の問題点に繋がっていると考える。つまり、この症例は、上下肢に麻痺と感覚障害を呈しており、動作時には、筋緊張が亢進する、典型的な左中大脳動脈梗塞である。「最も多く脳梗塞の60％～70％がこの場所で発生しています。詰まった動脈がある反対側の片麻痺（特に上肢）や知覚麻痺、視力障害などが起こります。」(http://www.sankikai.or.jp/tsurumaki/disease/brain/)より心身機能の問題点としては、①身体の片側の筋緊張(b7352)②触知覚(b1564)活動の問題点としては、①乗り移りが挙げられる。感覚鈍麻があれば、大きくQOLが低下することもある。また、動作時の筋緊張の亢進により、トランスファーに介助を要してしまう。活動の問題点として、乗り移りを提示したのは、対象者の生活の幅を広げるために、まず1番の問題点であるからである。アプローチとしては、残存している運動機能を活かしたトランスファーの改善をすることである。また、下肢の筋力トレーニングも麻痺のアプローチではじゅうようである。　本症例は1ヶ月半前に左中大脳動脈梗塞を発症させた75歳の女性である。合併症として高血圧があるが、理学療法中の血圧の問題はない。主訴は「手足が動きにくく、歩けない」である。これを踏まえて問題点を述べていく。　BRSTは、手指、上肢共にII、下肢Ⅲであり重篤な麻痺が認められ、分離運動が行えていないことが問題点として挙げられる。Dr.による情報で年齢が若い為、今後麻痺の回復はあると報告している為積極的に理学療法を行う必要があるが、（10）と脳卒中治療ガイドラインにある為大きく改善されない可能性もあると考えられる。　Ashwath スケールでは上・下肢共に2であり、筋緊張の増加はあるが容易に動かすことが出来ることが分かる。しかし、運動時には全体的に筋緊張が亢進する傾向にある為、何の運動時に亢進が認められるか確認が必要であると考えられる。また、この筋緊張の影響により　深部腱反射では、右側上下肢で著名な亢進が認められており、病的反射であるホフマン反射、トラムナー反射、バビンスキー反射も陽性となっている事から錐体路障害が認められる。そのため、中枢神経の上位運動ニューロンの障害があると考えられる。感覚では、右側が鈍麻となっており（8）にある様に慢性期には疼痛の出現が考えられる為注意が必要である。　基本動作では家庭環境で車椅子での移動が可能となっている為、階段昇降や、歩行の介助などは特に大きな問題点とは捉えないこととする。基本動作の問題点として、トイレ動作でのトランスファー半介助と入浴全介助を列挙した。key personが旦那さんということもあり旦那さんへの負担が大きくなってしまう為立ち上がりなどの実用性を高め自立又は近位見守りレベルまで改善する必要があると考える。（12）によると下肢筋力の強化が有用であるとある為、麻痺と改善と併用し下肢筋力トレーニングも必要であると考えられる。FIMの点数が低い為どの動作が困難なのか詳しく確認する必要がある。また、立ち上がりや、車椅子からベットへのトランスファーは手すりが有れば自立である為、住宅改修などを行い手すりを付けるなど対応が必要であると考える。本症例は75歳の女性の方で左中大脳動脈梗塞である。合併症に高血圧があり、現在は投薬によりコントロールされているが、副作用などの把握のため商品名など調べる必要がある。また患者さんは肥満傾向にあるため頻繁に血圧測定をする必要もあると考える。主訴は「手足が動きにくく、歩けない」ということである。まず始めに動作について問題点を挙げて行こうと思う。トランスファーについて考えてあく。本症例では手すりがあれば車椅子からベッドは可能であり、ベッドから車椅子は介助・監視レベルである。このトランスファーに違いがあるのは、高さの問題があると考える。通常であればベッドよりも車椅子の方が座面は低い。この患者さんの場合は 高い位置から低い位置に移動する場合に介助が必要となる。これらの原因を検査、測定結果から考えていくと運動麻痺、筋緊張の亢進、すいたいろ症状、感覚障害が挙げられる。ブルンストロームは下肢がⅢであるため、共同運動が出ている可能性がある。しかし、車椅子からベッドに移乗の場合は介助は不要である。そのため高い位置から手をついたときに力が入りにくいのではないかと考えて、また上肢の感覚障害も関与していると考える。このことからトランスファーの獲得をするため、上肢の筋力増強、感覚障害の緩和、筋緊張の緩和が必要となると考える。本症例は1月前に左中大脳動脈梗塞を発症した75歳の女性である。合併症として高血圧がある。現在は服薬によって血圧がコントロールされてるため、理学療法時にあまり問題にならない。患者の主訴として、「手足が動きにくく、歩けない」とある。そこから検査と関連づけてまとめていきたいと思う。BRSTは上肢と手指はⅡであり、下肢はⅢである。上肢と手指には連合反応、下肢には共同運動パターンが出現してると考えられる。そして深部腱反射が+++、病的反射であるホフマン反射・トレムナー反射・バビンスキー反射が陽性であるため、錐体路徴候があると言える。　次に感覚では右側上下肢・体幹に表在と深部ともに鈍麻レベルである。⑧により、この患者のQOLが低下していると考えられる。　次は高次脳機能についてである。高次脳機能障害として失語があり、その失語は運動性失語のためコミニケーションの阻害因子となってる。またその他の高次脳機能障害が発症されていると考えられるため、その他の高次脳機能の検査を追加する必要がある。　基本動作として問題点が挙げられるのがまずトランスファーである。手すりがあれば車椅子からベッドは可能であるが、ベッドから車椅子は介助・監視レベルである。さらにトイレ動作もトランスファーも半介助である。 本症例は左中大脳動脈梗塞であり、主訴は「手足の動きにくさである」。OTからの情報より、上肢の動作制限の原因は廃用手であることから、この統合解釈は下肢の動きにくさについて行う。 BRSTは下肢Ⅲであることから協同運動が起こる。腱反射は右下肢3＋であることから著名な亢進が起こっており、アシュワスより下肢2であることから筋緊張は亢進状態でこのことから錐体路症状がある。よって心身機能の問題点として(1)と(3)を選択する。 活動より移動は自操であるが困難であり、トランスファーは手すりがあれば可能、介助・監視レベルである。またトイレへのトランスファーは半介助である。よって問題点として活動の(1)を選択する。 本症例の下肢の動きにくさの問題店として運動麻痺による協同運動があることと述べた。文献（４）（６）より中大脳動脈梗塞により、被殻が障害されているため運動麻痺が考えられる。また錐体路症状は文献（７）より深部腱反射、アシュワスより筋緊張が亢進する。本症例はトランスファーに問題点があり、行えない理由として立ち上がりを自立出来ていないことである。協同運動が起こることそして手すりを使用しないと立ち上がりが出来ないことから、臀部の挙上が行えないと考えられる。また筋緊張を亢進が起こることにより、足関節伸展モーメントで腓腹筋の緊張が高まり、膝関節伸展位になりやすく、協同運動を起こることで行えない。文献(１２）（１４）より立ち上がりにアプローチすることで下肢の筋活動を促し立位の自立を行わせ、下肢筋力を増大させ身体機能の改善をはかる。本症例は、5週間前に左中大脳動脈梗塞を発症した患者である。主訴が、「手足が動きにくく、歩けない。」というものである。他部門からの情報にあるように、この患者は現在上肢の麻痺が重篤であり、下肢の筋緊張が高いことがわかる。これは、BRSTの上肢Ⅱ、手指Ⅱ、下肢Ⅲ、Ashwarthスケールが上下肢ともに2という結果からも判断できる。それに加えて、OTからの情報により、上肢すでに廃用手であると思われる。感覚に関しては、上下肢、体幹の深部、表在感覚がともに鈍麻レベルという結果が出ている。これらのことにより、本症例の問題点は1.身体の片側の筋緊張（b7352）、2.触知覚（b1564）であると考えられる。活動に関しては、立ち上がり、車椅子→ベッドのトランスファーは手すりがあれば可能であるが、ベッド→車椅子は介助・監視レベルで、トイレ動作におけるトランスファーは半介助である。このことから、活動における問題点は、3.乗り移り（d4200）だとかんがえられる。1.は、BRST下肢Ⅲが原因で起こっていると考えられ、筋緊張が高いことにより、多くの動作が制限されていると考えられる。この症例は左中大脳動脈梗塞を起こした75さいの患者さんである。BRST上肢、手指ともに2レベル、下肢は3レベルである。深部腱反射右側上下肢ともとに+++と過亢進している。またホフマン反射、トレムナー反射、バビンスキー反射ともに陽性であり、右側上下肢の下肢体幹表在深部の感覚障害もみられる。文献（最も多く脳梗塞の60％～70％がこの場所で発生しています。詰まった動脈がある反対側の片麻痺（特に上肢）や知覚麻痺、視力障害などが起こります。）このことから、梗塞により上位運動ニューロンが障害されていることがわかる。この患者さんの手足が動かない。という主訴にたいして、上肢のBRST2レベルと重篤であることから、まだ年齢的には若いが、回復には難しいと考えられる。しかし、下肢はBRST3であるので、回復の可能性はあると考えられる。乗り移りに関して、文献によると(麻痺側下肢の筋力トレーニングは、下肢筋力を増加させ、身体機 能を改善させるので勧められる)とあるので下肢へのアプローチを積極的に進める必要がある。更衣、入浴などが介助量が多く、上肢を多く使わないとならないが、運動障害、感覚障害がみられるため、動作を遂行しにくい原因となっている。［活動］この患者さんの自宅での環境は、車いすででの活動が可能となっている。しかし車いすの移動では、自走可能なものの右側に偏ってしまう傾向がある。文献では、(失語や失認をはじめとした多彩な高次機能障害が出現することがある。半側空間無視（空間のうち左右どちらかが意識からはずれてしまう）が多くみられる。)ということから、半側空間無視についても検査が必要である。つまり、問題点は心身機能では、随意運動の制御、感覚障害、活動では、反則空間無視があげられる。　本症例は1ヶ月半前に左中大脳動脈梗塞を発症させた75歳の女性である。合併症として高血圧があるが、理学療法中の血圧の問題はない。主訴は「手足が動きにくく、歩けない」である。これを踏まえて問題点を述べていく。　BRSTは、手指、上肢共にII、下肢Ⅲであり重篤な麻痺が認められ、分離運動が行えていないことが問題点として挙げられる。Dr.による情報で年齢が若い為、今後麻痺の回復はあると報告している為積極的に理学療法を行う必要があるが、（10）と脳卒中治療ガイドラインにある為大きく改善されない可能性もあると考えられる。　Ashwath スケールでは上・下肢共に2であり、筋緊張の増加はあるが容易に動かすことが出来ることが分かる。しかし、運動時には全体的に筋緊張が亢進する傾向にある為、何の運動時に亢進が認められるか確認が必要であると考えられる。また、この筋緊張の影響により　深部腱反射では、右側上下肢で著名な亢進が認められており、病的反射であるホフマン反射、トラムナー反射、バビンスキー反射も陽性となっている事から錐体路障害が認められる。そのため、中枢神経の上位運動ニューロンの障害があると考えられる。感覚では、右側が鈍麻となっており（8）にある様に慢性期には疼痛の出現が考えられる為注意が必要である。　基本動作では家庭環境で車椅子での移動が可能となっている為、階段昇降や、歩行の介助などは特に大きな問題点とは捉えないこととする。基本動作の問題点として、トイレ動作でのトランスファー半介助と入浴全介助を列挙した。key personが旦那さんということもあり旦那さんへの負担が大きくなってしまう為立ち上がりなどの実用性を高め自立又は近位見守りレベルまで改善する必要があると考える。（12）によると下肢筋力の強化が有用であるとある為、麻痺と改善と併用し下肢筋力トレーニングも必要であると考えられる。FIMの点数が低い為どの動作が困難なのか詳しく確認する必要がある。また、立ち上がりや、車椅子からベットへのトランスファーは手すりが有れば自立である為、住宅改修などを行い手すりを付けるなど対応が必要であると考える。'

#print("---------------------------------------------")
#print(tagger.parse(text))

# ファイルを読み込む
tagged_text = open("mecabu.txt", "r", encoding="utf-8").read()
#tagged_text = tagger.parse(text)

# 出力するファイルの選択
f = open("mecab_dic.csv", mode='w')

# 複合語を抽出し、重要度を算出
frequency = termextract.mecab.cmp_noun_dict(tagged_text)
LR = termextract.core.score_lr(frequency,
         ignore_words=termextract.mecab.IGNORE_WORDS,
         lr_mode=1, average_rate=1
     )
term_imp = termextract.core.term_importance(frequency, LR)

# 重要度が高い順に並べ替えて出力
write_list=[]
data_collection = collections.Counter(term_imp)
for cmp_noun, value in data_collection.most_common():
    #print(termextract.core.modify_agglutinative_lang(cmp_noun), value, sep="\t")
    f.write(termextract.core.modify_agglutinative_lang(cmp_noun) + "\n")
f.close()
