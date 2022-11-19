import random
card1 = []
card2 = []
mcards = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#取一副牌并洗牌
def makecard():
    ret = []
    for i in range(1, 14):
        ret.append((i, u"方块"))
        ret.append((i, u"梅花"))
        ret.append((i, u"红心"))
        ret.append((i, u"黑桃"))
    ret.append((14, u"大王"))
    ret.append((14, u"小王"))
    return ret
cards=makecard()
random.shuffle(cards)
#发牌各9张
send_card_num=0
while send_card_num<9:
    x = cards[0]
    card1.append(x)
    cards.pop(0)
    send_card_num+=1
while send_card_num<18:
    x = cards[0]
    card2.append(x)
    cards.pop(0)
    send_card_num+=1
#展示手牌
def showcards(showc):
    for e in showc:
        print("%s\t%s"%(e[0], e[1]))
#判断是否胡牌
def win (wcard):
    num=0
    flag=1
    while num<10:
        win_card_num=0
        for card in wcard:
            if card[0] == wcard[num][0]:
                win_card_num+=1
        if win_card_num % 2 !=0:
            flag = 0
        num+=1
        if num ==10 and flag==1:
            return True
        elif flag ==0:
            return False
#测试数据
# a=[(1,"eee"),(1,"e"),(2,"gg"),(1,"ghh"),(3,"gee"),(3,"ooo"),(4,"gggss"),(4,"iii"),(5,"ert"),(5,"ooojj")]
# b=[(1,1),(1,1),(2,1),(2,2),(3,3),(3,3),(4,3),(4,"iii"),(5,"ert"),(5,"ooojj")]
# c=[(2,"eee"),(1,"e"),(3,"gg"),(1,"ghh"),(3,"gee"),(3,"ooo"),(6,"gggss"),(4,"iii"),(5,"ert"),(5,"ooojj")]
# if win(a):
#     print("a")
# else:
#     print("!a")
# if win(b):
#     print("b")
# else:
#     print("!b")
# if win(c):
#     print("c")
# else:
#     print("!c")
#弃牌
def movecard(cards,mcards):
    cards_in = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for card in cards:
        cards_in[card[0]-1] +=1
    i =0
    locate = 0
    while(i<10):
        x=cards[i][0]-1
        if cards_in[x]+ mcards[x] == 4 and cards_in[x]%2==1:
            locate=i
            break
        elif cards_in[x]==3:
            locate=i
            break
        elif cards_in[x]==cards_in[13] and cards_in[13]==1:
            locate=i
            break
        if cards_in[x]%2==1:
            locate=i
        i+=1
    mcards[cards[locate][0]-1]+=1
    discard = cards[locate]
    cards.pop(locate)
    return cards,mcards,discard
#测试数据
# mc=movecard(c,mcards)
# c=mc[0]
# mcards=mc[1]
# showcards(c)
# discard=mc[2]
# print(u"扔掉的牌是：")
# print(discard[0],discard[1])
#判断是否取牌
def judgecard(cards,discard):
    flag=1
    cards_in = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for card in cards:
        cards_in[card[0] - 1] += 1
    i = 0
    position = discard[0]-1
    while i<14:
        if cards_in[position]==3 or cards_in[position]==1:
            flag =0
            break
        i+=1
    if flag == 1:
        print("机器选择取牌")
        return True
    else:
        print("机器选择不取牌")
        return False
# if judgecard(a,discard):
#     x=cards[0]
#     card2.append(x)
#     cards.pop(0)
#     mcards[discard[0] - 1] += 1
# else:
#     card2.append(discard)
#测试取牌
# print("a")
# showcards(a)
# print("discar is %s,%s" %(discard[0],discard[1]))
#程序开始
#发牌
print(u"你被发到的手牌是:")
showcards(card1)
#玩家取牌
card1_grab=cards[0]
card1.append(card1_grab)
cards.pop(0)
send_card_num+=1
print(u"你取得的牌是:%s\t%s"%(card1_grab[0],card1_grab[1]))
print(u"你现在的手牌是:")
showcards(card1)
if win(card1):
    print("恭喜您赢得比赛！")
    exit()
else:
    print("您未胡牌，请选择弃牌位置(1-10):")
while send_card_num<54:
    card_location = int(input())
    while card_location <1 or card_location>10:
        print("输入位置错误，请重新输入:")
        card_location = int(input())
    mcards[card1[card_location-1][0] - 1] += 1
    discard = card1[card_location-1]
    card1.pop(card_location-1)
    # print("您现在的手牌是:")
    # showcards(card1)
    if judgecard(card2,discard):
        x=cards[0]
        card2.append(x)
        cards.pop(0)
        mcards[discard[0] - 1] += 1
    else:
        card2.append(discard)
    if win(card2):
        print("电脑的手牌为:")
        showcards(card2)
        print("抱歉，电脑赢得比赛！")
        exit()
    else:
        # showcards(card2)
        # print("换了之后的牌")
        mc=movecard(card2,mcards)
        card2=mc[0]
        mcards=mc[1]
        # showcards(card2)
        discard=mc[2]
        print(u"电脑弃牌：")
        print("%s\t%s"%(discard[0],discard[1]))
    print("你现在的牌")
    showcards(card1)
    print("请选择取弃牌堆的牌（0）或者摸牌（1）")
    catch = int(input())
    if catch == 1:
        x=cards[0]
        card1.append(x)
        cards.pop(0)
        mcards[discard[0] - 1] += 1
        print(u"您取得的牌为:%s,%s" % (x[0], x[1]))
    else:
        card1.append(discard)
    print("您目前的牌为:")
    showcards(card1)
    if win(card1):
        print("恭喜您赢得比赛！")
        exit()
    else:
        print("您未胡牌，请选择弃牌位置(1-10):")
