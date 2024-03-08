classifier
with open("import.txt", "r") as f:
    content = f.read()

words = []
idioms = []
phrases = []
sentences = []
others = []

for line in content.split("\n"):
    if "(n.)" in line or "(v.)" in line or "(adj.)" in line or "(adv.)" in line:
        if " " in line.split('(')[0]:
          print(line.split('(')[0])
          idioms.append(line)
          continue
        words.append(line)
    elif "=" in line or "A" in line or "B" in line or "sb." in line or "sth." in line or not line.endswith("."):
        phrases.append(line)
    elif line.endswith('.'):
        sentences.append(line)
    else:
      others.append(line)

with open("export.txt", "w") as f:
    if input("要按字母順序嗎y/n").lower()== 'y':
      words.sort()
      phrases.sort()
      sentences.sort()
  
    f.write("Words:\n")
    f.write("\n".join(words))
    f.write("\n\n")

    f.write("Idioms:\n")
    f.write("\n".join(idioms))
    f.write("\n\n")
  
    f.write("Phrases:\n")
    f.write("\n".join(phrases))
    f.write("\n\n")

    f.write("Sentences:\n")
    f.write("\n".join(sentences))
    f.write("\n\n")
    
    f.write("Others:\n")
    f.write("\n".join(others))
    f.write("\n\n")
    

stance(n.)立場
regard to 考慮到 衍：delve into = research on研究
contentment(n.)滿足
Happiness lies in contentment.
content(v.)滿足
revise(n.)修正 衍：amend, correct, modify
attribute sth. to sth. 歸因於
abstract(adj.)抽象
credit(n.)學分[C]；讚許，賒帳[U]
give sb. credit for sth. 因…給…讚許
union(n.)工會，聯盟；(v.)合併 衍：combination
confess to N./Ving = admit = candid = own up 坦白
resort(v.)採取(n.)度假勝地
resort to N./Ving = take action
stagger(v.)步履蹣跚
stagger from A to B
yield(v.)產生；讓步
yield to = concede to = make concession to = give in to
grim(adj.)悲觀的 = pessimistic
wary(adj.)謹慎的 = careful
vain(adj.)虛榮的 (n.)空虛
accountability(n.)問責
be justified to Ving = 做…是合理的
grueling(adj.)令人疲累的
come under fire(v.)被批評
a great amount of N.[U]
be subject to = 受…的控制
growth(n.)腫瘤
concentrated(adj.)密集的
inevitably(adv.)必然的
be comprised of = be made of
dub(v.)稱…為
benign(adj.)和善的
leverage(n.)力量
maneuver(v.)滑順華麗的操作
conversely(adj.)相反地 衍：adversely, counter, opposite
deposit(v.)存錢到銀行
consummate(adj.)完美的 (v.)完善
authentic(adj.)道地的
consent(n.)同意
unanimously(adv.)一致的
empower(v.)授權
exploit(v.)剝削
offspring(n.)後代
monetary(adj.)和錢相關的
dispute(n.)紛爭
tradeoff(n.)妥協
asset(n.)有價值的東西
tactic(n.)手法
critter(n.)小動物
gland(n.)腺體
deter(v.)威嚇
imperative(adj.)極為重要的
notorious(adj.)臭名昭著
pigment(n.)天然染色劑
hue(n.)色調
medium(n.)媒介 = agent
be devoid of = be lack of
dull(v.)使失去…
synthetic(n.)人造模仿天然物
resin(n.)樹脂
resonate(v.)引起共鳴
imposing(adj.)驚人的
illuminate(v.)照亮
pierce(v.)穿刺進
reservoir(n.)水庫
sanctuary(n.)避難所
splinter(n.)尖碎片
robust(adj.)強壯健康的；富有味道的
ample(adj.)大量或更多
coriander(n.)香草
cumin(n.)孜然
turmeric(n.)薑黃
stew(n.)燉肉
trio(n.)三個人或三件事
consistency(n.)一致性；質地
guests(n.)賓客
occasionally(adv.)偶爾地
engage in sth.從事
oblige(v.)有義務+to
entitle(v.)賦予
antics(n.)滑稽
prone(v.)傾向
rev up(v.)加速；提高；起飛；振奮；使情緒高漲
impulse buying(n.)衝動購物
temptation(n.)誘惑
spontaneous purchase(n.)即興購買
regret(n.)後悔
buyer's remorse(n.)購買者後悔
tempting(adj.)誘人的
irresistible(adj.)不可抗拒的
instant gratification(n.)即時滿足
shopping spree(n.)瘋狂購物
splurge(v.)揮霍、大津花費
buyer's high(n.)購物快感
retail therapy(n.)購物療法
window shopping(n.)逛街、看橱窗
guilty pleasure(n.)心痛的享受
indulge(v.)放縱
impulsive(adj.)衝動的
unplanned purchase(n.)非計劃購買
ultimatum(n.)最後通牒
wharf(n.)碼頭
yacht(n.)遊艇
pubulum(n.)精神糧食
foible(n.)怪癖
insert(v.)放
cultivate(v.)栽培；種植
furniture(n.)家具
in terms of就…而論
not to mention 更不用說
on no account 絕不
to sum up 總結
charge(v.)指控
specify(v.)指明
ironically(adv.)諷刺地
demonstration(n.)示範
engage in 從事
deposit(n.)存款
dilemma(n.)困境
disdain(n.)鄙視
sentiment(n.)感傷
punctuation(n.)標點符號
brochure(n.)手冊
adjacent(adj.)鄰近的
perplex(v.)困惑
integrate (v.)融入
uproar(n.)反對聲浪
unveil(v.)告訴
turn the other cheek轉過臉頰=忍耐包容
amateur(n.)素人
agility(n.)敏捷
hone(v.)磨練
deficient(adj.)不足的
evident(adj.)明顯的
release from hospital 出院
plot(n.)情節
coin(v.)創造
deprive from 被剝奪
endow with 被賦予
atrocity (n.)暴行
regime(n.)政權
plight(n.)困境
visa(n.)簽證
indicator(n.)
from the cradle to the grave=lifetime 
cradle(n.)搖籃
grave(n.)墳墓
advocacy(n.)提倡
administer(v.)掌管
script(n.)劇本
column(n.)專欄
excerpt(n.)摘錄片段
medallion(n.)獎牌；紀念章
fare(n.)票價
infancy(n.)起步階段
sarcastic(adj.)諷刺的
neutral(adj.)中立的
intricate(adj.)錯綜複雜的
