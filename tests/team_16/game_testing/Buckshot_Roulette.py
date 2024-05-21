import random
import time
import math
import pickle
import os
'''未來想法:
1.增加一些皇后效果
2.增加國王系列道具，只有莊家可以直接獲得
3.大廳，讓玩家選擇放棄之後獲得金錢，金錢可以在大廳用來購買物品
4.增加一些額外賭注讓玩家在每局開始前選擇，例如莊家先手獎金2.5倍，無法獲得皇后/莊家可獲得國王獎金2倍，限定道具使用次數/無道具獎金1.5倍等
5.商店可賣人工心臟，每次死亡可以使用人工心臟復活，但是價格很高且使用會消耗95%的金錢
6.劇情線和結局
7.教學模式
8.改成用滑鼠操作的GUI
9.朦朧國王:免疫每局第一次傷害
10.狂暴國王:接下來5次傷害翻倍
11.狡詐國王:知道前三發子彈是什麼
12.貪婪國王:偷走玩家所有非皇后物品
13.試煉模式前對話
14.薩邁爾的大廳互動
15.成就系統
16.莉莉斯的對話
'''
#大廳物件
class NPC:
    def __init__(self,name):
        self.name = name
        pass
    def challenge_mode_dialogue(self,win_count):
        #每場結束時說的話
        pass
    def challenge_mode_reward(self,player_lobby):
        #試煉獎勵
        pass
    def say_normal_dialogue(self):
        #正常時說的話
        pass
    def before_challenge(self):
        #試煉開始前說的話
        pass

class all_item:
    def __init__(self,name,description):
        self.name_hide = name
        self.name = '你尚未解鎖這個道具'
        #self.name = name
        self.description_hide = description
        self.description = '???'
        #self.description = description
        self.unlock = False
    def unlock_item(self,show_text):
        if self.unlock == False:
            self.unlock = True
            self.name = self.name_hide
            self.description = self.description_hide
            if show_text:
                print('圖鑑解鎖了',self.name_hide)
                time.sleep(0.7)

class achievement(all_item):
    def __init__(self,name,description,hint):
        all_item.__init__(self,name,description)
        self.name = '???'
        self.description = hint
    def unlock_item(self):
        if self.unlock == False:
            self.unlock = True
            self.name = self.name_hide
            self.description = self.description_hide
            print('已解鎖成就 ',self.name)
            time.sleep(0.7)

class shop_item:
    def __init__(self,name,price,stock,raise_multiply,description = ''):
        self.name = name
        self.price = price
        self.stock = stock
        self.description = description
        self.required_item = None
        self.raise_count = 0
        self.raise_multiply = raise_multiply
        if self.stock == 3:
            self.set_required_item('五連勝標記')
        if self.stock == 1:
            self.set_required_item('二十連勝標記')
    def raise_price(self):
        self.raise_count += 1
        self.price = int(self.price*self.raise_multiply)
        self.stock -= 1
        if self.stock == 0:
            self.description = '已售完'
            self.price = math.inf
        if self.raise_count/(self.raise_count+self.stock) == 0.2:
            self.set_required_item('五連勝標記')
        elif self.raise_count/(self.raise_count+self.stock) == 0.4:
            self.set_required_item('十連勝標記')
        elif self.raise_count/(self.raise_count+self.stock) == 0.6:
            self.set_required_item('二十連勝標記')
        elif self.raise_count/(self.raise_count+self.stock) == 0.8:
            self.set_required_item('五十連勝標記')

        if self.raise_count/(self.raise_count+self.stock) == 0.25:
            self.set_required_item('五連勝標記')
        elif self.raise_count/(self.raise_count+self.stock) == 0.5:
            self.set_required_item('十連勝標記')
        elif self.raise_count/(self.raise_count+self.stock) == 0.75:
            self.set_required_item('二十連勝標記')

        if self.raise_count == 0 and self.stock == 3:
            self.set_required_item('五連勝標記')
        elif self.raise_count == 1 and self.stock == 2:
            self.set_required_item('十連勝標記')
        elif self.raise_count == 2 and self.stock == 1:
            self.set_required_item('二十連勝標記') 

        if self.raise_count == 0 and self.stock == 1:
            self.set_required_item('二十連勝標記')

    def show_item(self,index):
        print(index,self.name,':',self.price,'元')
        print('    ',self.description)
        if self.required_item != None:
            print('     需要',self.required_item,'才能購買')
    def set_required_item(self,item):
        self.required_item = item
    def check_required_item(self,player):
        if self.required_item == None:
            return True
        if self.required_item in player.unlockable_item:
            return True
        return False

class shopkeeper(NPC):
    def __init__(self):
        NPC.__init__(self,'利維坦')
        self.shop=[]
        self.shop.append(shop_item('人工心臟',5000000,10,12,'死亡時可以使用人工心臟復活，手術需消耗50%財產'))
        self.shop.append(shop_item('道具欄位',1000000,10,2.15,'增加離開賭桌後可保存的道具數量'))
        self.shop.append(shop_item('永久隨機皇后',4000000,3,30,'開局時獲得隨機皇后道具'))
        self.shop.append(shop_item('永久額外血量',1000000,4,20,'開局時獲得額外血量'))
        self.shop.append(shop_item('永久未知藍圖',1000000,3,7,'開局時獲得未知藍圖道具'))
        self.shop.append(shop_item('解鎖琉璃皇后',4444444444,1,1,'象徵希望的靈魂將在賭局中出現'))
        self.shop.append(shop_item('解鎖惡魔試煉',99999999999,1,1,'通往地獄的大門為你敞開'))
        self.normal_dialogue = ['利維坦: 小老弟買顆心臟吧，你死了可就沒人陪我聊天了',\
                                '利維坦叼了根菸，悠閒地滑著手機',\
                                '利維坦不在，店裡空無一人，商品靜靜的陳列著',\
                                '利維坦把玩著手銬和槍械零件，似乎沒注意到你',\
                                '另一名賭客和你擦身而過，口中念念有詞',\
                                '利維坦: 你看起來有點疲憊，要不要來點刺激的? 說著，她晃了晃手中的神祕藥包',\
                                '利維坦: 賭局中道具就是真理，沒有道具欄位怎麼贏，你說對吧?',\
                                '利維坦: 這位客官，既然都來了，何不買張藍圖試試手氣?',\
                                '利維坦: 你問琉璃皇后是什麼? 買下來不就知道了嗎?',\
                                '利維坦: 如果你嫌命太長，要不要試試惡魔試煉? 前提是你要有錢就是了(笑',\
                                '利維坦: 一口氣用光8個道具，然後一槍轟在自己臉上，這種白癡真的有夠帥']
    
    def player_buy_item(self,index):
        self.shop[index].raise_price()

    def say_normal_dialogue(self):
        print(self.normal_dialogue[random.randint(0,len(self.normal_dialogue)-1)])

    def challenge_mode_dialogue(self,win_count,computer):
        #每場結束時說的話
        if win_count == 5:
            print('利維坦: 好傢伙，是我輸了，你的實力我認可了')
        else:
            print('已獲勝勝',win_count,'/5場')
            time.sleep(2)
            if win_count == 1:
                print('利維坦: 你還不錯，不過這只是暖身罷了')
                time.sleep(2)
            elif win_count == 3:
                print('利維坦: 好了，差不多要拿出真實力了')
                time.sleep(2)
            elif win_count == 4:
                computer.item.append('貪婪國王')
                computer.item.append('朦朧國王')
                time.sleep(2)
            
    
    def challenge_mode_reward(self,player_lobby):
        if '扭曲印記' not in player_lobby.unlockable_item:
            player_lobby.unlockable_item.append('扭曲印記')
            time.sleep(2)
            print('利維坦抓住你的手，你感覺皮膚開始灼燒')
            time.sleep(2)
            print('你的前臂被烙上了一隻纏繞的蛇')
            time.sleep(2)
            print('利維坦: 根據契約，現在你也能使用我的一部分能力了')
            time.sleep(2)
            print('利維坦: 不會用的話就去問莉莉斯，她會很樂意教你的')
            time.sleep(2)
            print('說完，利維坦點了根菸，起身走回了她的店內')
            time.sleep(2)
            print('你獲得了扭曲印記')
            time.sleep(2)
            player_lobby.max_item += 2
            print('你的物品持有上限增加2個')
            time.sleep(2)
            lobby_NPC[0].unlock_achievement('扭曲的蛇')

    def unlock_final_challenge(self):
        print('利維坦: 小夥子，野心挺大的嘛')
        time.sleep(3)
        print('利維坦: 你要知道，挑戰惡魔試煉意味著你貪求惡魔的力量')
        time.sleep(3)
        print('利維坦: 真的要打的話，我們是不會放水的，請做好獻出靈魂的心理準備喔')
        time.sleep(3)
        print('利維坦: 如果你做好挑戰的準備，就去找薩邁爾吧，他會為你解釋你將面對什麼樣的地獄')
        time.sleep(3)
        print('利維坦: 祝你好運，小夥子')
        time.sleep(3)
        lobby_NPC[0].unlock_achievement('地獄之門')
    


class host(NPC):
    def __init__(self):
        NPC.__init__(self,'薩邁爾')
        pass

    def challenge_mode_reward(self,player_lobby):
        if '墮天使印記' not in player_lobby.unlockable_item:
            player_lobby.unlockable_item.append('墮天使印記')
            time.sleep(2)
            print('薩邁爾從座位上站起來，向你鞠躬')
            time.sleep(2)
            print('薩邁爾: 你的實力，又或者說是運氣，我認可了')
            time.sleep(2)
            print('薩邁爾: 依照規定，我將賜予你我的羽翼')
            time.sleep(2)
            print('語畢，薩邁爾的身形開始逐漸化為不可名狀之物，惡魔的真身')
            time.sleep(2)
            print('衝擊性的畫面在你的眼中留下了烙印')
            time.sleep(2)
            print('你獲得了墮天使印記')
            time.sleep(2)
            print('薩邁爾: 這是我對你的祝福，亦或者是詛咒。無論如何，通過試煉的你，擁有見公主大人的資格')
            time.sleep(2)
            print('薩邁爾: 準備好之後就來大廳找我吧')
            time.sleep(2)
            lobby_NPC[0].unlock_achievement('墮天使的羽翼')

    def tutorial(self):
        win_count = 0
        print('你走進了吵雜的賭場，一名男子憑空出現在你面前')
        time.sleep(2)
        print('薩邁爾: 你好，我是這裡的負責人，歡迎光臨BuckShot')
        time.sleep(2)
        print('薩邁爾: 需要我為你介紹一下嗎?')
        time.sleep(1)
        action = input('觀看教學? 1.是 2.否')
        if action == '2':
            print('薩邁爾: 原來是熟客了呀，真是失禮了')
            time.sleep(2)
            print('薩邁爾: 如果有任何問題，隨時可以來大廳找我，祝你賭運昌隆')
            time.sleep(2)
            return
        elif action == '1':
            print('薩邁爾: 了解了，那麼請跟我來')
            time.sleep(2)
            print('薩邁爾: BuckShot是一間由惡魔經營的賭場，我們提供巨額獎金，而你則是用靈魂作為賭注')
            time.sleep(4)
            print('薩邁爾帶著你到賭桌前，並交給你一把散彈槍')
            time.sleep(4)
            print('薩邁爾: 每局開始時，這把槍會以隨機順序裝填2~8發實彈或空包彈')
            time.sleep(4)
            print('薩邁爾: 輪到你的回合時，你可以選擇開槍射向自己或射向莊家')
            time.sleep(4)
            print('薩邁爾: 被實彈射中者將會損失1點血量')
            time.sleep(4)
            print('薩邁爾: 當你用空包彈射中自己時，你將獲得一個額外的回合')
            time.sleep(4)
            print('薩邁爾: 雙方輪流開槍直到子彈打空，進入下一局並重新裝填子彈')
            time.sleep(4)
            print('薩邁爾: 先將對方血量歸零者獲勝')
            time.sleep(4)
            print('薩邁爾: 以上便是惡魔輪盤的基礎規則，準備好的話就來練習一場吧?')
            time.sleep(4)
            input('按下Enter開始練習')
            player1 = player(5,[],0)
            computer1 = computer(5,[])
            tutorial_games={}
            tutorial_games[0] = tutorial_game(player1,computer1,2)
            while True:
                if tutorial_games[0].round == 1:
                    live_bullet = 2
                    blank = 1
                else:
                    live_bullet = 2
                    blank = 3
                tutorial_games[0].basic_one_round(live_bullet,blank)
                tutorial_games[0].round += 1
                if player1.hp <= 0:
                    print('你忽然回過神來，發現自己仍坐在賭桌前，彷彿剛才都只是一場夢')
                    time.sleep(3)
                    print('薩邁爾: 賭博這種事，運氣是很重要的。希望你已經掌握基本規則了')
                    break
                elif computer1.hp <= 0:
                    win_count += 1
                    print('薩邁爾: 很好，看來你已經掌握了基本規則')
                    break
            time.sleep(4)
            print('薩邁爾: 那麼，接下來由利維坦為你介紹關於"道具"的規則吧')
            time.sleep(4)
            print('語畢，一名身材高挑，全身刺青的女子不知從何處出現，湊到你的面前')
            time.sleep(4)
            print('利維坦: 新來的小夥子挺標緻嘛，我是這裡的商店老闆，利維坦')
            time.sleep(4)
            print('利維坦: 你不覺得純粹賭運氣的遊戲有點無聊嗎?')
            time.sleep(4)
            print('利維坦: 然而只要加入道具，賭局就會變得更刺激，你說是吧?')
            time.sleep(4)
            print('薩邁爾在一旁瞪了她一眼，利維坦清了清喉嚨，繼續說道')
            time.sleep(4)
            print('利維坦: 接下來我會為你介紹一下道具的使用方法和規則')
            time.sleep(4)
            print('利維坦: 每局開始，也就是重新裝彈的時候，你和莊家都將隨機獲得2~5個道具')
            time.sleep(4)
            print('利維坦: 這些道具可以幫助你或者干擾對手，增加遊戲的變數性')
            time.sleep(4)
            print('利維坦: 你可以在每回合開槍前使用道具，想用幾個道具都可以，次數沒有限制')
            time.sleep(4)
            print('利維坦: 沒用完的道具將會保留，不過請注意每人最多持有8個道具')
            time.sleep(4)
            print('利維坦: 每個道具的效果各不相同，一般道具總共有9種，它們的效果分別是...什麼來著?')
            time.sleep(4)
            print('你聽到身後傳來一聲嘆氣，接著一本圖鑑被放到了賭桌上')
            time.sleep(4)
            print('莉莉斯: 這裡有一般道具的介紹，記下來對你會很有幫助')
            time.sleep(4)
            action = input('查看圖鑑? 1.是 2.否')
            lobby_NPC[0].unlock_normal_item()
            lobby_NPC[0].unlock_special_item()
            if action == '1':
                lobby_NPC[0].show_normal_item()
            time.sleep(2)
            print('莉莉斯: 這些道具是普通道具，當然未來你在賭桌上有機會遇見一些特殊道具')
            time.sleep(4)
            print('莉莉斯: 到時候你可以來我這裡查看圖鑑，我會告訴你如何使用這些道具')
            time.sleep(4)
            print('利維坦: 咳咳...總之，準備好的話就來練習一場吧? 嘿嘿嘿，我會讓你體驗道具真正的力量......')
            time.sleep(4)
            print('薩邁爾一拳打在利維坦頭上，強行把她拖走')
            time.sleep(4)
            print('莉莉斯: 那個笨蛋總是會搞出不必要的混亂。這場就由我來幫你練習吧?')
            time.sleep(4)
            input('按下Enter開始練習')
            player1 = player(5,[],0)
            computer1 = computer(5,[])
            tutorial_games={}
            tutorial_games[1] = tutorial_game(player1,computer1,6)
            while True:
                live_bullet = random.randint(1,4)
                blank = random.randint(1,4)
                item_number = random.randint(2,5)
                tutorial_games[1].item_one_round(live_bullet,blank,item_number)
                tutorial_games[1].round += 1
                if player1.hp <= 0:
                    print('你忽然回過神來，發現自己正趴在賭桌前，莉莉斯剛好為你完成包紮')
                    break
                elif computer1.hp <= 0:
                    win_count += 1
                    print('莉莉斯: 你學得很快呢! 靈活運用道具是致勝的關鍵')
                    break
            time.sleep(4)
            print('莉莉斯: 那麼以上就是關於道具的使用方法和基本規則')
            time.sleep(4)
            print('莉莉斯: 如果有任何規則相關的問題，你可以在大廳找到薩邁爾，他會很樂意為你解答')
            time.sleep(4)
            print('莉莉斯: 遇到新的道具或者想要一些關於賭局的技巧，都可以來找我')
            time.sleep(4)
            print('莉莉斯: 順帶一提，利維坦那笨蛋負責商店，等你有錢後也可以去她那裡光顧一下')
            time.sleep(4)
            print('莉莉斯: 然後這個給你，在你犯錯時可以救你一命，就當作是初次見面的禮物吧')
            time.sleep(4)
            print('你獲得了人工心臟，可以在死亡的復活一次，使用時消耗50%財產作為手術費用')
            main_player.unlockable_item.append('人工心臟')
            time.sleep(4)
            print('莉莉斯: 那麼祝你好運，希望你能在這裡找到你想要的東西')
            time.sleep(4)
            input('按下Enter回到大廳')
            if win_count == 0:
                lobby_NPC[0].unlock_achievement('也許你不適合這裡')
            elif win_count == 2:
                lobby_NPC[0].unlock_achievement('炸魚')
            
         
class collection_manager(NPC):
    def __init__(self):
        NPC.__init__(self,'莉莉斯')
        self.normal_item=[]
        self.special_item=[]
        self.queen_king_item=[]
        self.mark_item=[]
        self.snake_item=[]
        
        self.normal_item.append(all_item('放大鏡','你可以查看現在這發子彈是實彈或空包彈'))
        self.normal_item.append(all_item('香菸','緩解壓力，回復一點血量'))
        self.normal_item.append(all_item('手鋸','鋸下散彈槍前端，下一發子彈傷害加倍'))
        self.normal_item.append(all_item('啤酒','退出並查看當前這發子彈'))
        self.normal_item.append(all_item('手銬','把莊家銬起來，下一回合莊家無法行動'))
        self.normal_item.append(all_item('手機','預知未來某一發子彈是實彈或空包彈'))
        self.normal_item.append(all_item('轉換器','將實彈轉換成空包彈，空包彈轉換成實彈'))
        self.normal_item.append(all_item('過期藥物','50%機率回復2點血量，50%機率損失1點血量'))
        self.normal_item.append(all_item('腎上腺素','竊取莊家一個道具，注意某些道具是無法竊取的'))
        self.special_item.append(all_item('未知藍圖','你可以用來合成一個特殊道具'))
        self.special_item.append(all_item('禁藥','70%機率血量大幅提升，30%機率中毒\n     由3個過期藥物合成'))
        self.special_item.append(all_item('大口徑子彈','當前子彈換成大口徑子彈並直接射出，造成3點傷害，注意這會結束你的回合\n     由2個手鉅和1個放大鏡合成'))  
        self.special_item.append(all_item('榴彈砲','使用榴彈砲攻擊，若為實彈則造成自身當前血量的傷害，注意這會結束你的回合並使你剩下1點血量\n     由1個大口徑子彈、1個腎上腺素和1個轉換器合成'))
        self.special_item.append(all_item('彈藥包','直接射出所有子彈並重新裝填八顆子彈\n     由2個啤酒和1個香菸合成'))
        self.special_item.append(all_item('擴增背包','背包空間+2\n     由滿背包任意的物品合成'))
        self.queen_king_item.append(all_item('琉璃皇后','獲得琉璃的祝福，退出所有子彈並重新裝填一發實彈\n接下來每次換彈都會回復1點血量，並且根據第一發子彈獲得不同增益效果'))
        self.queen_king_item.append(all_item('漆黑皇后','將子彈重新裝填為1發5點傷害的實彈和1發空包彈，同時清空雙方物品欄'))
        self.queen_king_item.append(all_item('神聖皇后','回復2點血量，獲得3個隨機物品，增加2格背包空間'))
        self.queen_king_item.append(all_item('蔚藍皇后','每次輪到莊家的回合時，獲得1個隨機物品'))
        self.queen_king_item.append(all_item('腥紅皇后','每回合獲得手鉅效果並免疫莊家的手鉅雙倍傷害效果，最多觸發5次'))
        self.queen_king_item.append(all_item('朦朧國王','免疫每局第一次傷害'))
        self.queen_king_item.append(all_item('狂暴國王','接下來5次傷害翻倍'))
        self.queen_king_item.append(all_item('狡詐國王','預知前三發子彈'))
        self.queen_king_item.append(all_item('貪婪國王','偷走玩家所有非皇后物品'))
        self.mark_item.append(all_item('嗜血印記','開槍造成1點傷害時，額外吸收莊家的1點血量'))
        self.mark_item.append(all_item('扭曲印記','每局可使用一次，使用後改變道具的本質(詳見下一頁)，直到本局結束'))
        self.mark_item.append(all_item('墮天使印記','未知'))
        self.snake_item.append(all_item('*放大鏡','獲得1格背包空間，額外裝填3發子彈'))
        self.snake_item.append(all_item('*香菸','使當前空包彈變為實彈，若為實彈退彈'))
        self.snake_item.append(all_item('*手鋸','用手鉅攻擊莊家，造成1點傷害，無視朦朧國王效果'))
        self.snake_item.append(all_item('*啤酒','回復1點血量'))
        self.snake_item.append(all_item('*手銬','改造散彈槍，本局雙方都無法再射向自己'))
        self.snake_item.append(all_item('*手機','改變所有剩餘子彈的順序，預知前兩發子彈'))
        self.snake_item.append(all_item('*轉換器','將所有實彈轉換成空包彈，所有空包彈轉換成實彈'))
        self.snake_item.append(all_item('*過期藥物','看破本局莊家的朦朧國王效果'))
        self.snake_item.append(all_item('*腎上腺素','下一次攻擊傷害2倍'))
        self.snake_item.append(all_item('*未知藍圖','獲得3個隨機道具'))
        self.snake_item.append(all_item('*禁藥','吸到high起來，額外獲得一回合'))
        self.snake_item.append(all_item('*大口徑子彈','當所有空包彈換成實彈'))  
        self.snake_item.append(all_item('*榴彈砲','把所有子彈當成實彈射出'))
        self.snake_item.append(all_item('*彈藥包','退到剩一發子彈，每退1發實彈回復1點血量，每退1發空包彈造成1點傷害'))
    
        self.item_list = []
        self.item_list.append(self.normal_item)
        self.item_list.append(self.special_item)
        self.item_list.append(self.queen_king_item)
        self.item_list.append(self.mark_item)
        self.item_list.append(self.snake_item)

        self.achievement_list = []
        self.achievement_list.append(achievement('炸魚','活著通過新手教學','在教學階段表現良好'))
        self.achievement_list.append(achievement('也許你不適合這裡','在新手教學死了兩次','你已經死兩次了'))
        self.achievement_list.append(achievement('惡魔的喜好?','從莉莉斯口中得知惡魔眷屬一事','不小心說溜嘴了!'))
        self.achievement_list.append(achievement('居心叵測','看過莉莉絲的全部對話','tips永遠不嫌多，八卦也是'))
        self.achievement_list.append(achievement('破解','解鎖所有道具','收集道具還得靠運氣'))
        self.achievement_list.append(achievement('誘惑的吻','通關莉莉斯的試煉','你的生命力夠頑強嗎'))
        self.achievement_list.append(achievement('扭曲的蛇','通關利維坦的試煉','這東西不是這樣用的吧喂!'))
        self.achievement_list.append(achievement('墮落的羽翼','通關薩邁爾的試煉','0%戰術，100%運氣'))
        self.achievement_list.append(achievement('地獄之門','解鎖惡魔試煉','你已經準備好了'))
        self.achievement_list.append(achievement('第一桶金','持有10000000元','來吧，開始遊戲吧'))
        self.achievement_list.append(achievement('財富自由','持有500000000元','或許還債有望了?'))
        self.achievement_list.append(achievement('富可敵國','持有999999999999元','兄弟，你是不是該買個島了?'))
        self.achievement_list.append(achievement('見好就收','贏了一場後馬上放棄','Nope'))
        self.achievement_list.append(achievement('恢復呼吸','第一次用人工心臟復活','貪婪的代價'))
        self.achievement_list.append(achievement('風險大師','高風險模式下連續贏了10場','風險管理'))
        self.achievement_list.append(achievement('互相傷害呀','殺手國王模式下連續贏了10場','國王與皇后的對決'))
        self.achievement_list.append(achievement('真實力','幽閉皇后模式下連續贏了10場','靠自己也能贏'))
        self.achievement_list.append(achievement('你才是挑戰者','莊家先手模式下連續贏了10場','想太多，順序根本不重要'))
        self.achievement_list.append(achievement('賭神','下注全部模式下連續贏了10場','你的運氣是怎麼回事?'))
        self.achievement_list.append(achievement('哈哈屁眼','莊家先手模式下第一回合就死了','這我也沒辦法'))
        self.achievement_list.append(achievement('你是笨蛋嗎','使用手鉅對自己造成2點傷害並被嘲笑','你是笨蛋嗎?'))
        self.achievement_list.append(achievement('漆黑子彈','血量低於5的狀態下使用漆黑皇后贏下一局','50%'))
        self.achievement_list.append(achievement('道具永動機','獲得5層以上的蔚藍皇后效果','太...太多了'))
        self.achievement_list.append(achievement('道理我都懂，但是這個背包怎麼這麼大','背包上限突破20','更大的背包'))
        self.achievement_list.append(achievement('巨砲','用榴彈砲造成30以上的傷害','這武器攻擊力無上限對吧?'))
        self.achievement_list.append(achievement('吸毒有礙身心健康，請勿輕易嘗試','吃禁藥死亡','來路不明的藥物別亂嗑'))
        self.achievement_list.append(achievement('琉璃的祝福','獲得琉璃的祝福','這道具也太強了吧'))
        self.achievement_list.append(achievement('就說了不行','嘗試偷走腎上腺素','有些東西是偷不走的'))
        self.achievement_list.append(achievement('滿血','買下所有額外血量','保險起見啦'))
        self.achievement_list.append(achievement('瘋狂的傻子','成為利維坦的眷屬','在利維坦面前耍帥一波'))
        self.achievement_list.append(achievement('慾望的奴隸','成為莉莉斯的眷屬','向莉莉斯展現你的生命力'))
        self.achievement_list.append(achievement('無謂的堅持','成為薩邁爾的眷屬','回應薩邁爾的期待'))

        self.normal_dialogue = []
        #莉莉斯的對話含有重要訊息，所以雖然是隨機但是會循環
        self.dialogue_number = [i for i in range(0,17)]
        
        self.normal_dialogue.extend([f'莉莉斯: {main_player.name}你來啦，隨便坐，我去為你泡杯茶'\
                                    ,'莉莉斯: 利維坦又設計了奇怪的道具...不要增加我的工作量啊!'\
                                    ,'莉莉斯: 轉換器有個很方便的副作用，下次可以試著仔細觀察使用前後剩餘子彈數量'\
                                    ,'莉莉斯: 國王道具無法被竊取，但是皇后可以，所以要小心!'\
                                    ,'莉莉斯: 藍圖的道具合成有優先順序，和圖鑑的排序是一樣的'\
                                    ,'莉莉斯: 手鉅的傷害加成對所有火兵器都有效，包括大口徑子彈、榴彈砲、彈藥包和漆黑皇后'\
                                    ,'莉莉斯: 血量恢復是沒有上限的，我最喜歡生命力旺盛的靈魂了，如果有44點以上的話...啊!沒事!我什麼都沒說!'\
                                    ,'莉莉斯: 手銬不能在一回合連續使用兩次，但可以連續兩回合各自使用一次'\
                                    ,'莉莉斯: 手鉅無法和任何傷害加倍的效果疊加，最多就是兩倍!'\
                                    ,'莉莉斯: 皇后道具是已故賭徒的靈魂殘渣，擁有提升獎金倍率的能力，很奇怪吧?'\
                                    ,'莉莉斯: 榴彈砲殺不死血量比自己高的目標，想扭轉局勢可能得搭配其他道具'\
                                    ,'莉莉斯: 禁藥的回血公式是翻倍再+3。你問我怎麼知道的? 當然是親自實測呀'\
                                    ,'莉莉斯: 國王道具的效果非常誇張，建議隨時注意莊家的物品欄'\
                                    ,'莉莉斯: 利維坦是個不按牌理出牌的傢伙，大家都說只有她才知道道具的真正使用方式'\
                                    ,'莉莉斯: 好想要有更多眷屬啊......別這樣看著我，要想成為眷屬的話，你得先學會看穿惡魔的喜好才行'\
                                    ,'莉莉斯: 說實話，整天收割人類靈魂的生活也是很無聊的，所以公主大人才會突發奇想了這間賭場'\
                                    ,'莉莉斯: 你應該有發覺，薩邁爾其實和利維坦不太合，但礙於實力差距，即使他是這裡的老大也只能嘴上抱怨而已'])


    def unlock_normal_item(self):
        for item in self.normal_item:
            item.unlock_item(show_text=False)
    def unlock_special_item(self):
        for item in self.special_item:
            item.unlock_item(show_text=False)
    def unlock_queen_king_item(self,target):
        for item in self.queen_king_item:
            if item.name_hide == target:
                item.unlock_item(True)
        unlock_all = True
        for cat in self.item_list:
            for item in cat:
                if item.description == '???':
                    unlock_all = False 
        if unlock_all:
            self.unlock_achievement('破解') 
    def unlock_mark_item(self,target):
        for item in self.mark_item:
            if item.name_hide == target:
                item.unlock_item(True)
        unlock_all = True
        for cat in self.item_list:
            for item in cat:
                if item.description == '???':
                    unlock_all = False 
        if unlock_all:
            self.unlock_achievement('破解') 
    def unlock_snake_item(self):
        for item in self.snake_item:
            item.unlock_item(True)
    def show_normal_item(self):
        print('普通道具:')
        #顯示物品名稱和敘述
        for i in range(len(self.normal_item)):
            print(i+1,self.normal_item[i].name)
            print('    ',self.normal_item[i].description)
        input('按下Enter回到上一頁')
    def show_special_item(self):
        print('特殊道具:')
        #顯示物品名稱和敘述
        for i in range(len(self.special_item)):
            print(i+1,self.special_item[i].name)
            print('    ',self.special_item[i].description)
        input('按下Enter回到上一頁')
    def show_queen_king_item(self):
        print('皇后&國王道具:')
        #顯示物品名稱和敘述
        for i in range(len(self.queen_king_item)):
            print(i+1,self.queen_king_item[i].name)
            print('    ',self.queen_king_item[i].description)
        input('按下Enter回到上一頁')
    def show_mark_item(self):
        print('惡魔印記:')
        #顯示物品名稱和敘述
        for i in range(len(self.mark_item)):
            print(i+1,self.mark_item[i].name)
            print('    ',self.mark_item[i].description)
        input('按下Enter回到上一頁')
    def show_snake_item(self):
        print('扭曲印記啟用時的道具:')
        #顯示物品名稱和敘述
        for i in range(len(self.snake_item)):
            print(i+1,self.snake_item[i].name)
            print('    ',self.snake_item[i].description)
        input('按下Enter回到上一頁')
    def show_achievement_1(self):
        print('成就列表:')
        for i in range(len(self.achievement_list)//2):
            print(i+1,self.achievement_list[i].name)
            print('     提示: ' if not self.achievement_list[i].unlock else '    ',self.achievement_list[i].description)
        input('按下Enter查看下一頁')

    def show_achievement_2(self):
        for i in range(len(self.achievement_list)//2,len(self.achievement_list)):
            print(i+1,self.achievement_list[i].name)
            print('     提示: ' if not self.achievement_list[i].unlock else '    ',self.achievement_list[i].description)
        input('按下Enter回到列表')

    def unlock_achievement(self,target):
        for achievement in self.achievement_list:
            if achievement.name_hide == target:
                achievement.unlock_item()

    def show_list(self):
        print ('=================================================================')
        print('圖鑑:')
        print('1.普通道具')
        print('2.特殊道具')
        print('3.皇后&國王道具')
        print('4.惡魔印記')
        if '扭曲印記' in main_player.unlockable_item:
            print('5.扭曲印記啟用時的道具')
            print('6.成就列表')
        else:
            print('5.成就列表')
        print('按下Enter離開')
        while True:
            try:
                choice = input('請選擇:')
            except ValueError:
                print('請重新輸入')
                continue
            break
        if choice == '1':
            self.show_normal_item()
            self.show_list()
        elif choice == '2':
            self.show_special_item()
            self.show_list()
        elif choice == '3':
            self.show_queen_king_item()
            self.show_list()
        elif choice == '4':
            self.show_mark_item()
            self.show_list()
        elif choice == '5' and '扭曲印記' in main_player.unlockable_item:
            self.show_snake_item()
            self.show_list()
        elif choice == '5' and '扭曲印記' not in main_player.unlockable_item:
            self.show_achievement_1()
            self.show_achievement_2()
            self.show_list()
        elif choice == '6':
            self.show_achievement_1()
            self.show_achievement_2()
            self.show_list()
        else:
            return
           
    
    def say_normal_dialogue(self):
        time.sleep(1)
        if len(self.dialogue_number) == 0:
            self.dialogue_number = [i for i in range(0,17)]

        if 0 in self.dialogue_number:
            number = self.dialogue_number.pop(0)
        else:
            number = self.dialogue_number.pop(random.randint(0,len(self.dialogue_number)-1))
        
        print(self.normal_dialogue[number])
        if number == 14:
            self.unlock_achievement('惡魔的喜好?')
        if self.dialogue_number == []:
            self.unlock_achievement('居心叵測')
        time.sleep(2)

    def challenge_mode_dialogue(self,win_count,computer):
        #每場結束時說的話
        if win_count == 5:
            print('莉莉斯: 看來是我輸了呢......')
        else:
            time.sleep(2)
            if win_count == 1:
                print('莉莉斯: 好久沒嘗到靈魂的滋味了，你可要活久一點喔?')
            elif win_count == 3:
                print('莉莉斯: 不屈不撓的靈魂，我很喜歡')
            elif win_count == 4:
                computer.item.append('禁藥')
                computer.item.append('禁藥')
    def challenge_mode_reward(self,player_lobby):
        if '扭曲印記' not in player_lobby.unlockable_item:
            player_lobby.unlockable_item.append('嗜血印記')
            time.sleep(2)
            print('莉莉斯起身向前，給了你一個深深的吻')
            time.sleep(2)
            print('酥麻感流遍全身，你的靈魂深處感到一股強烈的...對鮮血的渴望')
            time.sleep(2)
            print('莉莉斯: 你的靈魂非常甜美，多謝款待')
            time.sleep(2)
            print('回過神來，莉莉斯已經離開了')
            time.sleep(2)
            print('你獲得了嗜血印記')
            time.sleep(2)
            player_lobby.extra_hp += 2
            print('你的額外生命增加了2點')
            time.sleep(1)
            lobby_NPC[0].unlock_achievement('誘惑的吻')

class player_in_lobby(NPC):
    def __init__(self,name,money):
        NPC.__init__(self,name)
        self.die_state = False
        self.money = money
        #保存下來的物品欄(商店升級)
        self.item = []
        self.max_item = 0
        self.extra_hp = 0
        #商店物品
        self.unlockable_item = []
    def earn_money(self,amount):
        self.money += amount
    def show_money(self):
        print('你的金錢:',self.money)
    def buy_item(self,item,price):
        self.money -= price
        self.unlockable_item.append(item)
    def save_item(self,input_item):
        self.item = []
        for i in range(self.max_item):
            if len(input_item) == 0:
                break 
            self.item.append(input_item.pop(0))
        self.item.sort(key = ['琉璃皇后','漆黑皇后','神聖皇后','蔚藍皇后','腥紅皇后','未知藍圖','禁藥','大口徑子彈','榴彈砲','彈藥包','放大鏡','香菸','手鋸','啤酒','手銬','手機','轉換器','過期藥物','腎上腺素'].index)
    def show_item(self):
        print('你的物品欄:',self.item)
    def show_unlockable_item(self):
        print('已解鎖的商店物品:',self.unlockable_item)
    def revive(self):
        self.money -= int(self.money*0.5)
        self.item = []
    def die(self):
        self.die_state = True

#遊戲內部物件
class participant:
    def __init__(self, controlable, hp, item):
        self.controlable = controlable
        self.hp = hp
        self.item = item
        self.item_queen = 0
        self.blood_queen = 0

class computer(participant):
    def __init__(self, hp, item):
        participant.__init__(self, False, hp, item)
        self.handcuff = False
        self.bullet_pattern = []
        self.known_live = 0
        self.known_blank = 0
        self.max_item = 8
        self.rage_king = 0
        self.fog_king = 0
        self.fog = 0
        self.trick_king = 0
    def dohandcuff(self):
        self.handcuff = True
    def unhandcuff(self):
        self.handcuff = False
    def reset_bullet_pattern(self,number):
        self.bullet_pattern = []
        for i in range(number):
            self.bullet_pattern.append('unknown')
        self.known_live = 0
        self.known_blank = 0
    def set_bullet_pattern(self,poition,value):
        self.bullet_pattern[poition] = value
        if value == 'live':
            self.known_live = self.bullet_pattern.count('live')
        else:
            self.known_blank = self.bullet_pattern.count('blank')
    def pop_bullet_pattern(self):
        if self.bullet_pattern.pop(0) == 'live':
            self.known_live = self.bullet_pattern.count('live')
        else:
            self.known_blank = self.bullet_pattern.count('blank')

class player(participant):
    def __init__(self, hp, item, money = 0):
        participant.__init__(self, True, hp, item)
        self.handcuff = False
        self.money = money
        self.max_item = 8
        self.queen_used = []
        self.blood_queen = 0
        self.blessing = 0
        self.snake_mark_activate = False
        self.have_snake_mark = False
        self.have_blood_mark = False
        self.have_death_mark = False
    def dohandcuff(self):
        self.handcuff = True
    def unhandcuff(self):
        self.handcuff = False
    def enable_mark(self,blood,snake,death):
        self.have_blood_mark = blood
        self.have_snake_mark = snake
        self.have_death_mark = death
    def use_snake_mark(self):
        self.have_snake_mark = False
        self.snake_mark_activate = True
        print('你使用了扭曲印記，本局道具的用途被改變了')
        time.sleep(1)
    def end_snake_mark(self):
        if self.snake_mark_activate:
            print('扭曲印記效果結束')
            self.snake_mark_activate = False
            self.have_snake_mark = True
        

class game:
    def __init__(self, player, computer, hp, risk):
        self.player = player
        self.computer = computer
        self.player.hp = hp
        self.computer.hp = hp
        self.round = 1
        self.first_move = '玩家'
        self.item_list = ['放大鏡','香菸','手鋸','啤酒','手銬','手機','轉換器','過期藥物','腎上腺素']
        self.special_item = ['未知藍圖','禁藥','大口徑子彈','榴彈砲','彈藥包']
        self.queen = ['漆黑皇后','神聖皇后','蔚藍皇后','腥紅皇后','琉璃皇后'] 
        self.king = ['朦朧國王','狂暴國王','狡詐國王','貪婪國王']
        if risk % 2 == 0:
            self.item_list = ['放大鏡','香菸','手鋸','啤酒','手銬','手機','轉換器','過期藥物','腎上腺素','禁藥','大口徑子彈','榴彈砲','彈藥包']
            if random.randint(0,1):
                print('高風險模式，血量大幅提升')
                health = random.randint(3,10)
                self.player.hp += health
                self.computer.hp += health
        print('遊戲開始,每人有',self.player.hp,'點血量')

    def set_first_move(self,first_move):
        self.first_move = first_move

    def give_participant_item(self,number,participant):
        #神聖皇后和蔚藍皇后的給道具效果
        for i in range(number):
            if len(participant.item) < participant.max_item:
                time.sleep(1)
                self.item_list.append('未知藍圖')
                item=self.item_list[random.randint(0,len(self.item_list)-1)]
                self.item_list.remove('未知藍圖')
                print('你' if participant.controlable else '莊家','獲得了',item)
                participant.item.append(item)
                
            else:
                print('物品欄已滿')
        #照著['琉璃皇后','漆黑皇后','神聖皇后','蔚藍皇后','腥紅皇后','未知藍圖','禁藥','大口徑子彈','榴彈砲','彈藥包','放大鏡','香菸','手鋸','啤酒','手銬','手機','轉換器','過期藥物','腎上腺素']的順序排序玩家和電腦的物品欄
        participant.item.sort(key = ['朦朧國王','狂暴國王','狡詐國王','貪婪國王','琉璃皇后','漆黑皇后','神聖皇后','蔚藍皇后','腥紅皇后','未知藍圖','禁藥','大口徑子彈','榴彈砲','彈藥包','放大鏡','香菸','手鋸','啤酒','手銬','手機','轉換器','過期藥物','腎上腺素'].index)
    def give_item(self,number):
        for i in range(number):
            if len(self.player.item) < self.player.max_item:
                chance = random.randint(1,100)
                if (chance <= 20) and (self.player.item.count('未知藍圖') == 0):
                    item='未知藍圖'
                    if (random.randint(1,4) == 4) and (risk % 2 == 0) and (risk % 5 != 0):  
                        item=self.queen[random.randint(0,len(self.queen)-1)]
                        print('***你獲得了 ',item,' ***')
                    else:
                        print('你獲得了',item)
                    self.player.item.append(item)
                elif (chance > 95) and (risk % 5 != 0):   
                    if main_player.unlockable_item.count('琉璃皇后') == 0:
                        chance = random.randint(1,100)
                        if chance <= 20:
                            item='神聖皇后'
                            print('***你獲得了 神聖皇后 ***')
                            self.player.item.append(item)    
                        elif chance <= 40:
                            item='蔚藍皇后'
                            print('***你獲得了 蔚藍皇后 ***')
                            self.player.item.append(item)
                        elif chance <= 70:
                            item='腥紅皇后'
                            print('***你獲得了 腥紅皇后 ***')
                            self.player.item.append(item)
                        else:
                            item='漆黑皇后'
                            print('***你獲得了 漆黑皇后 ***')
                            self.player.item.append(item)
                    else:
                        chance = random.randint(1,110)
                        if chance <= 10:
                            item='琉璃皇后'
                            print('★★★你獲得了 琉璃皇后 ★★★')
                            self.player.item.append(item)
                        if chance <= 30:
                            item='神聖皇后'
                            print('***你獲得了 神聖皇后 ***')
                            self.player.item.append(item)    
                        elif chance <= 50:
                            item='蔚藍皇后'
                            print('***你獲得了 蔚藍皇后 ***')
                            self.player.item.append(item)
                        elif chance <= 80:
                            item='腥紅皇后'
                            print('***你獲得了 腥紅皇后 ***')
                            self.player.item.append(item)
                        else:
                            item='漆黑皇后'
                            print('***你獲得了 漆黑皇后 ***')
                            self.player.item.append(item)

                else:
                    item=self.item_list[random.randint(0,len(self.item_list)-1)]
                    print('你獲得了',item)
                    self.player.item.append(item)
            else:
                print('你的物品欄已滿')
            if len(self.computer.item) < self.computer.max_item:
                chance = random.randint(1,20)
                if chance == 20:
                    item='未知藍圖'
                    self.computer.item.append(item)
                elif (chance == 19) and (risk % 2 == 0):
                    item='未知藍圖'
                    self.computer.item.append(item)
                elif (chance == 18) and (risk % 3 == 0):
                    while True:
                        chance = random.randint(1,4)
                        if chance == 1:
                            self.computer.item.append('朦朧國王')
                        elif chance == 2:
                            self.computer.item.append('狂暴國王')
                        elif chance == 3:
                            self.computer.item.append('狡詐國王')
                        elif chance == 4:
                            self.computer.item.append('貪婪國王')
                        break
                else:
                    self.computer.item.append(self.item_list[random.randint(0,len(self.item_list)-1)])
        self.player.item.sort(key = ['琉璃皇后','漆黑皇后','神聖皇后','蔚藍皇后','腥紅皇后','未知藍圖','禁藥','大口徑子彈','榴彈砲','彈藥包','放大鏡','香菸','手鋸','啤酒','手銬','手機','轉換器','過期藥物','腎上腺素'].index)
        self.computer.item.sort(key = ['朦朧國王','狂暴國王','狡詐國王','貪婪國王','未知藍圖','禁藥','大口徑子彈','榴彈砲','彈藥包','放大鏡','香菸','手鋸','啤酒','手銬','手機','轉換器','過期藥物','腎上腺素'].index)
    
    def computer_bonus(self,bonus_number):
        self.computer.item.append(self.item_list[random.randint(0,len(self.item_list)-1)])
        if (bonus_number+1) % 2 == 0:
            self.computer.hp += 1
            print('莊家的血量增加了一點')
        if (bonus_number+1) % 10 == 0:
            self.computer.item.pop(0)
            self.computer.item.append('未知藍圖')

    def player_bonus(self,win_count):
        if win_count ==0:
            for i in main_player.unlockable_item:
                if i =='永久藍圖':
                    self.player.item.append('未知藍圖')
                elif i == '隨機皇后':
                    if '琉璃皇后' in main_player.unlockable_item:
                        self.player.item.append(self.queen[random.randint(0,4)])
                    else:
                        self.player.item.append(self.queen[random.randint(0,3)])
        for i in range(main_player.extra_hp):
            self.player.hp += 1
            
    def blessing(self,remain_bullet,turn,handsaw):
        print('★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★')
        print('琉璃祝福治癒了你的傷口')
        self.player.hp += self.player.blessing
        if remain_bullet[0] & (turn == '玩家'):
            print('你感覺到第一發子彈是實彈，這發子彈將造成兩倍傷害')
            print('★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★')
            time.sleep(2)
            return True
        elif remain_bullet[0] & (turn == '莊家'):   
            print('你感覺到第一發子彈是實彈，你將額外回復2點血量')
            self.player.hp += 2
        elif random.randint(0,1) and len(self.computer.item) > 0:
            print('你感覺到第一發子彈是空包彈，莊家的',self.computer.item[0],'將被摧毀')
            self.computer.item.pop(0)
        else:
            print('你感覺到第一發子彈是空包彈，你將額外獲得一個物品')
            self.give_participant_item(1,self.player)
        print('★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★')
        time.sleep(2)
        return handsaw

    def one_round(self,live_bullet,blank,item_number):
        time.sleep(3)
        print('第',self.round,'局開始')
        #朦朧國王效果
        self.computer.fog = self.computer.fog_king

        if self.player.handcuff:
            self.player.unhandcuff()
            print('你的手銬解除,可以自由行動了')
        if self.computer.handcuff:
            self.computer.unhandcuff()
            print('莊家的手銬解除,可以自由行動了')
        handsaw = False
        skip = False    
        killer_queen = False
        self.give_item(item_number)
        remain_bullet = []
        self.computer.reset_bullet_pattern(live_bullet+blank)
        print('這局有',live_bullet,'發實彈',blank,'發空包彈')
        for i in range(live_bullet):
            remain_bullet.append(True)
        for i in range(blank):
            remain_bullet.append(False)
        random.shuffle(remain_bullet)
        #狡詐國王效果
        for i in range(self.computer.trick_king):
            if i > len(remain_bullet)-1:
                break
            elif remain_bullet[i]:
                self.computer.set_bullet_pattern(i,'live')
            else:
                self.computer.set_bullet_pattern(i,'blank')
        #琉璃祝福效果
        if self.player.blessing > 0:
            handsaw = self.blessing(remain_bullet,self.first_move,handsaw)

        time.sleep(2)        

        while len(remain_bullet) > 0:
            skip = False
            try_count = 0
            not_blue_print = True
            gun_lock = False
            temp_break = False

            if self.player.hp <= 0:
                time.sleep(2)
                print('**************************************')
                print('你死了')
                time.sleep(2)
                return
            
            time.sleep(1)
            if self.first_move == '玩家':
                print('==========================================')
                print('你的回合')
                print('你的物品欄:',self.player.item)
                print('玩家血量:',self.player.hp,'莊家血量:',self.computer.hp)  
                print('剩餘',live_bullet,'發實彈',blank,'發空包彈')
                print('請選擇要做的事')
                if self.player.have_snake_mark:
                    print('1.射向莊家, 2.射向自己, 3.使用物品, 4.顯示莊家物品欄, 5.使用扭曲印記')
                else:
                    print('1.射向莊家, 2.射向自己, 3.使用物品, 4.顯示莊家物品欄')
                if len(self.computer.bullet_pattern) != len(remain_bullet):
                    raise Exception('子彈數量不符')
                if self.player.blood_queen > 0 and (handsaw==False):
                    print('腥紅皇后使你獲得手鋸效果')
                    time.sleep(1)
                    handsaw = True
                    self.player.blood_queen -= 1
                if self.player.max_item >= 20:
                    lobby_NPC[0].unlock_achievement('道理我都懂，但是這個背包怎麼這麼大')
                    time.sleep(1)
                while True:
                    try:
                        action = int(input())
                    except ValueError:
                        print('請輸入正確的數字')
                        continue
                    if type(action) != int:
                        print('請輸入正確的數字')
                        continue
                    if action == 5 and self.player.have_snake_mark:
                        self.player.use_snake_mark()
                        temp_break == True
                    elif action < 1 or action > 4:
                        print('請輸入正確的數字')
                        continue
                    break
                if temp_break:
                    temp_break = False
                    continue
            else:
                action = 0
                self.first_move = '玩家'
            
            if action==1:
                if remain_bullet[0] and (self.computer.fog > 0):
                    print('朦朧國王使你射偏了')
                    self.computer.pop_bullet_pattern()
                    self.computer.fog -= 1
                    handsaw = False
                    killer_queen = False
                    live_bullet -= 1
                elif remain_bullet[0] and handsaw and killer_queen:
                    self.computer.hp -= 10
                    print('你使用漆黑皇后射中了莊家,造成十點傷害')
                    if self.computer.blood_queen > 0:
                        print('腥紅皇后使莊家免疫額外傷害')
                        self.computer.hp += 5
                        self.computer.blood_queen -= 1
                    handsaw = False
                    killer_queen = False
                    self.computer.pop_bullet_pattern()
                    live_bullet -= 1
                    if (self.player.hp <= 5) and (self.computer.hp <= 0):
                        time.sleep(2)
                        lobby_NPC[0].unlock_achievement('漆黑子彈')
                elif remain_bullet[0]&killer_queen:
                    self.computer.hp -= 5
                    print('你使用漆黑皇后射中了莊家,造成五點傷害')
                    self.computer.pop_bullet_pattern()
                    live_bullet -= 1
                    killer_queen = False
                    if (self.player.hp <= 5) and (self.computer.hp <= 0):
                        time.sleep(2)
                        lobby_NPC[0].unlock_achievement('漆黑子彈')
                elif remain_bullet[0]&handsaw:
                    self.computer.hp -= 2
                    print('你射中了莊家,造成兩點傷害')
                    if self.computer.blood_queen > 0:
                        print('腥紅皇后使莊家免疫額外傷害')
                        self.computer.hp += 1
                        self.computer.blood_queen -= 1
                    handsaw = False
                    self.computer.pop_bullet_pattern()
                    live_bullet -= 1
                elif remain_bullet[0]:
                    self.computer.hp -= 1
                    print('你射中了莊家,造成一點傷害')
                    if self.player.have_blood_mark:
                        time.sleep(1)
                        print('嗜血印記使你吸收一點血量')
                        self.player.hp += 1
                        self.computer.hp -= 1
                        time.sleep(1)
                    self.computer.pop_bullet_pattern()
                    live_bullet -= 1
                else:
                    print('你的子彈打空了')
                    self.computer.pop_bullet_pattern()
                    blank -= 1
                    handsaw = False
                remain_bullet.pop(0)
                handsaw = False
            elif action==2 and gun_lock :
                print('槍經過改造，這局無法再射向自己了')
                time.sleep(1)
                continue
            elif action==2:
                if remain_bullet[0]&handsaw&killer_queen:
                    self.player.hp -= 10
                    print('你用漆黑皇后射中了自己,造成十點傷害')
                    if self.player.blood_queen > 0:
                        print('腥紅皇后使你免疫額外傷害')
                        self.player.hp += 5
                        self.player.blood_queen -= 1
                    else:
                        print('節哀順變')
                    handsaw = False
                    killer_queen = False
                    self.computer.pop_bullet_pattern()
                    live_bullet -= 1
                elif remain_bullet[0]&killer_queen:
                    self.player.hp -= 5
                    print('你用漆黑皇后射中了自己,造成五點傷害')
                    print('節哀順變')
                    killer_queen = False
                    self.computer.pop_bullet_pattern()
                    live_bullet -= 1
                elif remain_bullet[0]&handsaw:
                    self.player.hp -= 2
                    print('你射中了自己,造成兩點傷害')
                    if self.player.blood_queen > 0:
                        print('腥紅皇后使你免疫額外傷害')
                        self.player.hp += 1
                        self.player.blood_queen -= 1
                    else:
                        print('你是笨蛋嗎?')
                        lobby_NPC[0].unlock_achievement('你是笨蛋嗎')
                    handsaw = False
                    self.computer.pop_bullet_pattern()
                    live_bullet -= 1
                elif remain_bullet[0]:
                    self.player.hp -= 1
                    print('你射中了自己,造成一點傷害')
                    self.computer.pop_bullet_pattern()
                    live_bullet -= 1
                    handsaw = False
                else:
                    print('你的子彈打空了,額外獲得一回合')
                    remain_bullet.pop(0)
                    self.computer.pop_bullet_pattern()
                    blank -= 1
                    handsaw = False
                    continue
                remain_bullet.pop(0)
                handsaw = False

            elif action==3 and self.player.snake_mark_activate: 
                print('請選擇要使用的物品')
                for i in range(len(self.player.item)):
                    print(i+1,'.',self.player.item[i])
                try:
                    item = int(input())
                except ValueError:
                    print('請輸入正確的數字')
                    continue
                if item > len(self.player.item):    
                    print('請輸入正確的數字')
                    continue

                if self.player.item[item-1] == '手鋸':
                    print('你拿手鋸砍向莊家,造成了一點傷害')
                    time.sleep(1)
                    self.computer.hp -= 1
                elif self.player.item[item-1] == '啤酒':
                    self.player.hp += 1
                    print('你使用了啤酒,回復了一點血量')
                elif self.player.item[item-1] == '手機':
                    print('你使用了手機，改變了未來')
                    random.shuffle(remain_bullet)
                    self.computer.reset_bullet_pattern(live_bullet+blank)
                    print('第一發是', '實彈' if remain_bullet[0] else '空包彈')
                    print('第二發是', '實彈' if remain_bullet[1] else '空包彈')
                elif self.player.item[item-1] == '轉換器':
                    print('你使用了轉換器,反轉了所有子彈')
                    for i in range(len(remain_bullet)):
                        remain_bullet[i] = not remain_bullet[i] 
                        if remain_bullet[i]:
                            live_bullet += 1
                            blank -= 1
                        else:
                            live_bullet -= 1
                            blank += 1
                elif self.player.item[item-1] == '過期藥物':
                    print('你吸了一些過期藥物，high了起來')
                    self.computer.fog == 0
                    print('你看破了莊家的朦朧國王效果')
                elif self.player.item[item-1] == '放大鏡':
                    print('你使用了放大鏡,身前的空間被扭曲了')
                    self.player.max_item += 1
                    for i in range(3):
                        if random.randint(0,1):
                            remain_bullet.append(True)
                            live_bullet += 1
                        else:
                            remain_bullet.append(False)
                            blank += 1
                    self.computer.bullet_pattern.append('unknown')
                    self.computer.bullet_pattern.append('unknown')
                    self.computer.bullet_pattern.append('unknown')
                elif self.player.item[item-1] == '香菸':
                    if remain_bullet[0]:
                        print('你抽了根菸,退掉一發實彈')
                        live_bullet -= 1
                        remain_bullet.pop(0)
                        self.computer.pop_bullet_pattern()
                    else:
                        print('你把香菸塞進槍裡,空包彈被換成了實彈')
                        remain_bullet[0] = True
                        live_bullet += 1
                        blank -= 1
                    if len(remain_bullet) == 0:
                        print('子彈打完了')
                        print('進入下一局')
                        return
                elif self.player.item[item-1] == '手銬':
                    if gun_lock:
                        print('槍已經被改造過了')
                        continue
                    print('你用手銬改造了槍,這局無法再射向自己')
                    gun_lock = True
                elif self.player.item[item-1] == '未知藍圖':
                    print('你撕碎未知藍圖，憑空變出了三樣物品')
                    self.give_participant_item(3,self.player)
                    
                elif self.player.item[item-1] == '禁藥':
                    print('你嗑了禁藥，身手變的快速，摸頭還要哭!')
                    self.computer.dohandcuff()
                    handsaw = True
                    
                elif self.player.item[item-1] == '大口徑子彈':
                    print('你使用了大口徑子彈,所有空包彈被換成了實彈')
                    for i in range(len(remain_bullet)):
                        if remain_bullet[i] == False:
                            remain_bullet[i] = True
                            live_bullet += 1
                            blank -= 1
                elif self.player.item[item-1] == '榴彈砲':
                    print('你使用榴彈砲強制射出所有子彈,造成了',live_bullet+blank,'點傷害')
                    self.computer.hp -= live_bullet+blank
                    time.sleep(1)
                    print('子彈打完了')
                    print('進入下一局')
                    return
                elif self.player.item[item-1] == '彈藥包':
                    damage = 0
                    for i in range(len(remain_bullet)-1):
                        if remain_bullet.pop(0):
                            live_bullet -= 1
                            self.player.hp += 1
                            self.computer.pop_bullet_pattern()
                        else:
                            damage += 1
                            self.computer.pop_bullet_pattern()
                            blank -= 1
                    if handsaw:
                        damage *= 2
                        handsaw = False 
                    self.computer.hp -= damage
                    print('你用彈藥包清空大部分子彈，回復',live_bullet,'點血量，並對你造成',damage,'點傷害')
                    
                elif self.player.item[item-1] == '腎上腺素':    
                    print('你使用了腎上腺素，眼神變得狂暴')
                    handsaw = True
                self.player.item.pop(item-1)
                continue
            elif action==3:
                print('請選擇要使用的物品')
                for i in range(len(self.player.item)):
                    print(i+1,'.',self.player.item[i])
                try:
                    item = int(input())
                except ValueError:
                    print('請輸入正確的數字')
                    continue

                if item > len(self.player.item):    
                    print('請輸入正確的數字')
                    continue
                if self.player.item[item-1] == '手鋸':
                    if handsaw:
                        print('手鉅效果已經存在了')
                        continue
                    handsaw = True
                    print('你使用了手鋸,下一發子彈造成兩倍傷害')
                elif self.player.item[item-1] == '啤酒':
                    if remain_bullet.pop(0):
                        print('你使用了啤酒,退掉一發實彈')
                        live_bullet -= 1
                    else:
                        print('你使用了啤酒,退掉一發空包彈')
                        blank -= 1
                    self.computer.pop_bullet_pattern()
                    if len(remain_bullet) == 0:
                            print('子彈打完了')
                            print('進入下一局')
                            return
                elif self.player.item[item-1] == '手機':
                    print('你使用了手機')
                    if len(remain_bullet) == 1:
                        n = 0
                    else:
                        n=random.randint(1,len(remain_bullet)-1)
                    if remain_bullet[n]:
                        print('第',n+1,'發是實彈')
                    else:
                        print('第',n+1,'發是空包彈')
                elif self.player.item[item-1] == '轉換器':
                    print('你使用了轉換器,現在這發子彈將反轉')
                    remain_bullet[0] = not remain_bullet[0]
                    if remain_bullet[0]:
                        live_bullet += 1
                        blank -= 1
                    else:
                        live_bullet -= 1
                        blank += 1
                elif self.player.item[item-1] == '過期藥物':
                    print('你使用了過期藥物')
                    if random.randint(0,1):
                        self.player.hp += 2
                        print('你回復了兩點血量')
                    else:
                        self.player.hp -= 1
                        print('你失去了一點血量')
                        if self.player.hp <= 0:
                            time.sleep(2)
                            print('**************************************')
                            print('你死了')
                            time.sleep(2)
                            return
                elif self.player.item[item-1] == '放大鏡':
                    print('你使用了放大鏡看到 ','實彈' if remain_bullet[0] else '空包彈')
                elif self.player.item[item-1] == '香菸':
                    print('你使用了香菸,回復一點血量')
                    self.player.hp += 1
                elif self.player.item[item-1] == '手銬':
                    if self.computer.handcuff:
                        print('莊家已經被銬住了')
                        continue
                    print('你使用了手銬,莊家下回合無法行動')
                    self.computer.dohandcuff()
                elif self.player.item[item-1] == '未知藍圖':
                    if self.player.item.count('過期藥物') >= 3:
                        print('你獲得了禁藥')
                        self.player.item.append('禁藥')
                        for i in range(3):
                            self.player.item.remove('過期藥物')
                        self.player.item.remove('未知藍圖')
                    elif (self.player.item.count('手鋸') >= 2) and  (self.player.item.count('放大鏡') >= 1):
                        print('你獲得了大口徑子彈')
                        self.player.item.append('大口徑子彈')
                        for i in range(2):
                            self.player.item.remove('手鋸')
                        self.player.item.remove('放大鏡')
                        self.player.item.remove('未知藍圖')
                    elif (self.player.item.count('大口徑子彈') >= 1) and (self.player.item.count('腎上腺素') >= 1) and (self.player.item.count('轉換器') >= 1):
                        print('你獲得了榴彈砲')
                        self.player.item.append('榴彈砲')
                        self.player.item.remove('腎上腺素')
                        self.player.item.remove('大口徑子彈')
                        self.player.item.remove('轉換器')
                        self.player.item.remove('未知藍圖')
                    elif (self.player.item.count('啤酒') >= 2) and (self.player.item.count('香菸') >= 1) and ((live_bullet+blank) >= 3):
                        print('你獲得了彈藥包')
                        self.player.item.remove('啤酒')
                        self.player.item.remove('啤酒')
                        self.player.item.remove('香菸')
                        self.player.item.append('彈藥包')
                        self.player.item.remove('未知藍圖')
                    elif len(self.player.item) == self.player.max_item:
                        print('你獲得了擴增背包,物品欄增加2格')
                        self.player.item = []
                        self.player.max_item += 2
                    else:
                        print('你的物品不足以合成')
                        continue
                    not_blue_print = False
                elif self.player.item[item-1] == '禁藥':
                    #70%機率血量翻倍並+3，30%血量降低到1點，若血量為1則死亡
                    print('你使用了禁藥')
                    if random.randint(1,10) <= 7:
                        self.player.hp *= 2
                        self.player.hp += 3
                        print('你的血量大幅提升,現在血量為',self.player.hp)
                    else:
                        if self.player.hp == 1:
                            print('你死了')
                            self.player.hp = 0  
                            time.sleep(2)
                            lobby_NPC[0].unlock_achievement('吸毒有礙身心健康，請勿隨意嘗試')
                            time.sleep(2)      
                            return
                        self.player.hp = 1
                        print('你中毒了，血量降為1')
                elif self.player.item[item-1] == '大口徑子彈':
                    #將目前這發直接子彈替換成大口徑子彈並直接發射，造成3點傷害，如果有使用手鋸則造成6點傷害
                    if self.computer.fog > 0:
                        print('朦朧國王使你射偏了')
                        self.computer.fog -= 1
                        handsaw = False
                    elif handsaw:
                        self.computer.hp -= 6
                        print('你發射了大口徑子彈,造成6點傷害')
                    else:
                        self.computer.hp -= 3
                        print('你發射了大口徑子彈,造成3點傷害')
                    if remain_bullet.pop(0):
                        live_bullet -= 1
                    else:
                        blank -= 1
                    self.computer.pop_bullet_pattern()
                    self.player.item.pop(item-1)
                    skip = True
                    handsaw = False
                elif self.player.item[item-1] == '榴彈砲':
                    #將自身血量降低至1點，並發射現在這發子彈，若為實彈則造成(降低的血量+1)點傷害，使用手鋸則造成兩倍傷害，若為空包彈則不造成傷害，使用後輪到莊家的回合
                    damage = self.player.hp
                    self.player.hp = 1
                    if remain_bullet.pop(0):
                        if self.computer.fog > 0:
                            print('朦朧國王使你射偏了')
                            self.computer.fog -= 1
                            handsaw = False
                        elif handsaw:
                            self.computer.hp -= 2*damage
                            print('你發射了榴彈砲,造成',2*damage,'點傷害')
                            handsaw = False
                        else:
                            self.computer.hp -= damage
                            print('你發射了榴彈砲,造成',damage,'點傷害')
                        live_bullet -= 1
                    else:
                        print('你發射了榴彈砲,但是子彈打空了')
                        blank -= 1
                    self.computer.pop_bullet_pattern()
                    self.player.item.pop(item-1)
                    skip = True
                elif self.player.item[item-1] == '彈藥包':
                    #對莊家造成剩餘實彈數量的傷害，之後用實彈和空包彈隨機將彈藥填滿至8發
                    damage = live_bullet
                    if self.computer.fog > 0:
                        if damage > self.computer.fog:
                            damage -= self.computer.fog
                            self.computer.fog = 0
                            if handsaw:
                                damage *= 2
                            self.computer.hp -= damage
                            print('你使用了彈藥包')
                            print('朦朧國王使你射偏了部分子彈,對莊家造成',damage,'點傷害')
                        else:
                            print('你使用了彈藥包，但是朦朧國王使你射偏了所有子彈') 
                            self.computer.fog -= damage
                    else:
                        if handsaw:
                            damage *= 2
                        print('你使用了彈藥包,對莊家造成',damage,'點傷害')
                        self.computer.hp -= damage
                    handsaw = False
                    remain_bullet = []
                    live_bullet = 0
                    blank = 0
                    for i in range(8-len(remain_bullet)):
                        if random.randint(0,1):
                            remain_bullet.append(True)
                            live_bullet += 1
                        else:
                            remain_bullet.append(False)
                            blank += 1
                    random.shuffle(remain_bullet)
                    print('彈藥已重新裝填')
                    self.computer.reset_bullet_pattern(live_bullet+blank)
                    if self.player.blessing > 0:
                        handsaw = self.blessing(remain_bullet,'玩家',handsaw)
                elif self.player.item[item-1] == '漆黑皇后':
                    #移除雙方所有道具，將彈夾裝填為一發空包彈一發實彈，這發實彈將造成5點傷害
                    print('你使用了漆黑皇后，彈藥裝填為一發空包彈一發5點傷害實彈，祈禱吧!')
                    self.player.item = []
                    self.computer.item = []
                    remain_bullet = [True,False]
                    live_bullet = 1
                    blank = 1
                    self.computer.reset_bullet_pattern(live_bullet+blank)
                    random.shuffle(remain_bullet)
                    killer_queen = True
                    not_blue_print = False
                    self.player.queen_used.append('漆黑皇后')
                    if self.player.blessing > 0:
                        handsaw = self.blessing(remain_bullet,'玩家',handsaw)
                elif self.player.item[item-1] == '神聖皇后':
                    #回3點血量，背包上限+2，獲得3個隨機物品
                    print('你使用了神聖皇后，回復3點血量，背包上限+2，獲得3個隨機物品')
                    self.player.hp += 3
                    self.player.max_item += 3
                    self.give_participant_item(3,self.player)
                    self.player.max_item -= 1
                    self.player.queen_used.append('神聖皇后')
                elif self.player.item[item-1] == '蔚藍皇后':
                    #玩家的回合結束時，獲得一個隨機物品
                    print('你使用了蔚藍皇后，輪到莊家的回合時你將獲得一個隨機物品')
                    self.player.item_queen += 1   
                    self.player.queen_used.append('蔚藍皇后')
                    if self.player.item_queen >= 5 :
                        time.sleep(1)
                        lobby_NPC[0].unlock_achievement('道具永動機')
                        time.sleep(1)
                elif self.player.item[item-1] == '腥紅皇后':
                    #玩家的回合開始時，附加手鉅效果
                    print('你使用了腥紅皇后，每回合獲得手鋸效果並免疫手鉅的額外傷害，可以觸發五次')
                    self.player.blood_queen += 5       
                    self.player.queen_used.append('腥紅皇后') 
                elif self.player.item[item-1] == '琉璃皇后':
                    #每次重新裝彈(回合開始、彈藥包、漆黑皇后)時通靈第一顆子彈，若為實彈則附加手鉅效果
                    #若為空包彈則回復一點血量並消除莊家一個道具或獲得一個隨機道具
                    #使用當下清空莊家的道具、清空彈夾並裝上一顆實彈
                    print('你獲得了琉璃的祝福，莊家的道具被清空，彈夾重新裝填了')
                    time.sleep(2)
                    lobby_NPC[0].unlock_achievement('琉璃的祝福')
                    self.computer.item = [] 
                    self.computer.reset_bullet_pattern(1)
                    remain_bullet = [True]
                    if not handsaw:
                        handsaw = True
                        print('你獲得了手鋸效果')
                    time.sleep(1)
                    live_bullet = 1
                    blank = 0
                    self.player.blessing += 1
                    self.player.queen_used.append('琉璃皇后')                          
                elif self.player.item[item-1] == '腎上腺素':
                    print('你使用了腎上腺素,可以偷取莊家的物品')
                    if len(self.computer.item) == 0:
                        print('莊家沒有物品可以偷取')
                        continue
                    print('請選擇要偷取的物品:')
                    for i in range(len(self.computer.item)):
                        print(i+1,'.',self.computer.item[i])
                    try:
                        steal = int(input())
                    except ValueError:
                        print('請輸入正確的數字')
                        time.sleep(1)
                        continue  
                    if steal > len(self.computer.item):
                        print('請輸入正確的數字')
                        continue
                    elif steal <= 0:
                        print('請輸入正確的數字')
                        continue
                    #馬上使用選擇的物品 
                    if self.computer.item[steal-1] == '手鋸':
                        if handsaw:
                            print('手鉅效果已經存在了')
                            continue
                        handsaw = True
                        print('你使用了手鋸,下一發子彈造成兩倍傷害')
                    elif self.computer.item[steal-1] == '啤酒':
                        if remain_bullet.pop(0):
                            print('你使用了啤酒,退掉一發實彈')
                            live_bullet -= 1
                        else:
                            print('你使用了啤酒,退掉一發空包彈')
                            blank -= 1
                        self.computer.pop_bullet_pattern()
                        if len(remain_bullet) == 0:
                            print('子彈打完了')
                            print('進入下一局')
                            return
                    elif self.computer.item[steal-1] == '手機':
                        print('你使用了手機')
                        if len(remain_bullet) == 1:
                            n = 0
                        else:
                            n=random.randint(1,len(remain_bullet)-1)
                        if remain_bullet[n]:
                            print('第',n+1,'發是實彈')
                        else:
                            print('第',n+1,'發是空包彈')
                    elif self.computer.item[steal-1] == '轉換器':
                        print('你使用了轉換器,現在這發子彈將反轉')
                        remain_bullet[0] = not remain_bullet[0]
                        if remain_bullet[0]:
                            live_bullet += 1
                            blank -= 1
                        else:
                            live_bullet -= 1
                            blank += 1
                    elif self.computer.item[steal-1] == '過期藥物':
                        print('你使用了過期藥物')
                        if random.randint(0,1):
                            self.player.hp += 2
                            print('你回復了兩點血量')
                        else:
                            self.player.hp -= 1
                            print('你失去了一點血量')
                            if self.player.hp <= 0:
                                time.sleep(2)
                                print('**************************************')
                                print('你死了')
                                time.sleep(2)
                                return
                    elif self.computer.item[steal-1] == '放大鏡':
                        print('你使用了放大鏡看到 ','實彈' if remain_bullet[0] else '空包彈')
                    elif self.computer.item[steal-1] == '香菸':
                        print('你使用了香菸,回復一點血量')
                        self.player.hp += 1
                    elif self.computer.item[steal-1] == '手銬':
                        if self.computer.handcuff:
                            print('莊家已經被銬住了')
                            continue
                        print('你使用了手銬,莊家下回合無法行動')
                        self.computer.dohandcuff()
                    elif self.computer.item[steal-1] == '未知藍圖':
                        self.player.item.append('未知藍圖')
                        print('你獲得了未知藍圖')
                    elif self.computer.item[steal-1] == '禁藥':
                        print('你使用了禁藥')
                        if random.randint(1,10) <= 7:
                            self.player.hp *= 2
                            self.player.hp += 3
                            print('你的血量大幅提升,現在血量為',self.player.hp)
                        else:
                            if self.player.hp == 1:
                                print('你死了')
                                self.player.hp = 0  
                                time.sleep(2)
                                lobby_NPC[0].unlock_achievement('吸毒有礙身心健康，請勿隨意嘗試')
                                time.sleep(2)    
                                return
                            self.player.hp = 1
                            print('你中毒了，血量降為1')
                    elif self.computer.item[steal-1] == '大口徑子彈':
                        if self.computer.fog > 0:
                            print('朦朧國王使你射偏了')
                            self.computer.fog -= 1
                            handsaw = False
                        elif handsaw:
                            self.computer.hp -= 6
                            print('你使用了大口徑子彈,造成6點傷害')
                        else:
                            self.computer.hp -= 3
                            print('你使用了大口徑子彈,造成3點傷害')
                        if remain_bullet.pop(0):
                            live_bullet -= 1
                        else:
                            blank -= 1
                        self.computer.pop_bullet_pattern()
                        handsaw = False
                    elif self.computer.item[steal-1] == '榴彈砲':
                        damage = self.player.hp 
                        self.player.hp = 1
                        if remain_bullet.pop(0):
                            if self.computer.fog > 0:
                                print('朦朧國王使你射偏了')
                                self.computer.fog -= 1
                                handsaw = False
                            elif handsaw:
                                self.computer.hp -= 2*damage
                                print('你使用了榴彈砲,造成',2*damage,'點傷害')
                                handsaw = False
                                if damage >= 15:
                                    lobby_NPC[0].unlock_achievement('巨砲')
                            else:
                                self.computer.hp -= damage
                                print('你使用了榴彈砲,造成',damage,'點傷害')
                                if damage >= 30:
                                    lobby_NPC[0].unlock_achievement('巨砲')
                            live_bullet -= 1
                        else:
                            print('你使用了榴彈砲,但是子彈打空了')
                            blank -= 1
                            handsaw = False
                        self.computer.pop_bullet_pattern()
                    elif self.computer.item[steal-1] == '彈藥包':
                        damage = live_bullet
                        if self.computer.fog > 0:
                            if damage > self.computer.fog:
                                damage -= self.computer.fog
                                self.computer.fog = 0
                                if handsaw:
                                    damage *= 2
                                self.computer.hp -= damage
                                print('你使用了彈藥包')
                                print('朦朧國王使你射偏了部分子彈,對莊家造成',damage,'點傷害')
                            else:
                                print('你使用了彈藥包，但是朦朧國王使你射偏了所有子彈') 
                                self.computer.fog -= damage
                        else:
                            if handsaw:
                                damage *= 2
                            print('你使用了彈藥包,對莊家造成',damage,'點傷害')
                            self.computer.hp -= damage
                        handsaw = False
                        remain_bullet = []
                        live_bullet = 0
                        blank = 0
                        for i in range(8-len(remain_bullet)):
                            if random.randint(0,1):
                                remain_bullet.append(True)
                                live_bullet += 1
                            else:
                                remain_bullet.append(False)
                                blank += 1
                        random.shuffle(remain_bullet)
                        print('彈藥已重新裝填')
                        self.computer.reset_bullet_pattern(live_bullet+blank)
                        if self.player.blessing > 0:
                            handsaw = self.blessing(remain_bullet,'玩家',handsaw)
                        
                    elif self.computer.item[steal-1] == '腎上腺素':
                        print('你不能偷取腎上腺素')
                        time.sleep(2)
                        lobby_NPC[0].unlock_achievement('就說了不行')
                        continue
                    else:
                        print('你不能偷取國王道具')
                        continue
                    self.computer.item.pop(steal-1)

                if not_blue_print and not skip: 
                    self.player.item.pop(item-1)
                time.sleep(2)
                if self.computer.hp <= 0:
                    time.sleep(2)
                    print('**************************************')
                    print('你贏了')
                    time.sleep(2)
                    return
                if not skip:
                    continue
            elif action==4:
                print('莊家的物品欄:',self.computer.item)
                time.sleep(4)
                continue
            if self.computer.hp <= 0:
                time.sleep(2)
                print('**************************************')
                print('你贏了')
                time.sleep(2)
                return
            if self.player.hp <= 0:
                time.sleep(2)
                print('**************************************')
                print('你死了')
                time.sleep(2)
                return
            if len(remain_bullet) == 0:
                print('子彈打完了')
                print('進入下一局')
                return
            if self.player.item_queen > 0:
                print('蔚藍皇后使你獲得隨機物品')
                time.sleep(1)
            for i in range(self.player.item_queen):
                self.give_participant_item(1,self.player)
            print('==========================================')
            print('莊家的回合')
            print('==========================================')
            time.sleep(1)
            try_count = 0
            not_blue_print = True

            if self.computer.handcuff:
                print('莊家被手銬銬住了,無法行動')
                self.computer.unhandcuff()
                continue

            skip = False
            not_blue_print = True
            if action == 0:
                achievement_first_dead = True
            else:
                achievement_first_dead = False

            while True:
                #莊家進行剩餘子彈分析
                if (live_bullet-self.computer.known_live) <= 0:
                    for i in range(len(self.computer.bullet_pattern)):
                        if self.computer.bullet_pattern[i] == 'unknown':
                            self.computer.set_bullet_pattern(i,'blank')
                elif (blank-self.computer.known_blank) <= 0:
                    for i in range(len(self.computer.bullet_pattern)):
                        if self.computer.bullet_pattern[i] == 'unknown':
                            self.computer.set_bullet_pattern(i,'live')
                if self.player.hp <= 0:
                    time.sleep(2)
                    print('**************************************')
                    print('你死了')
                    time.sleep(2)
                    if achievement_first_dead:
                        lobby_NPC[0].unlock_achievement('哈哈屁眼')
                    return
                time.sleep(2)
                if len(remain_bullet) == 0:
                    print('子彈打完了')
                    print('進入下一局')
                    return
                if (self.computer.rage_king > 0) and (handsaw == False):
                    print('狂暴國王給予莊家手鉅效果')
                    time.sleep(1)
                    handsaw = True
                    self.computer.rage_king -= 1
                if self.computer.item.count('腥紅皇后') > 0 & (not handsaw):
                    print('腥紅皇后使莊家獲得手鋸效果')
                    time.sleep(1)
                    handsaw = True
                    self.computer.blood_queen -= 1
                #莊家的行動判斷
                if len(self.computer.bullet_pattern) != len(remain_bullet):
                    raise Exception('子彈數量不符')
                if len(self.computer.item) > 2 :
                    if try_count >= 3:
                        action = random.randint(1,2)
                        if self.computer.bullet_pattern[0] == 'live':
                            action = 1
                        elif self.computer.bullet_pattern[0] == 'blank':
                            action = 2
                    elif random.randint(1,4) == 4:
                        action = random.randint(1,2)
                    else:
                        action = 3
                elif ('朦朧國王' in self.computer.item or '狂暴國王' in self.computer.item or '狡詐國王' in self.computer.item or '貪婪國王' in self.computer.item):
                    action = 3
                elif self.computer.bullet_pattern[0] == 'live':
                    action = 1
                elif self.computer.bullet_pattern[0] == 'blank':
                    action = 2
                elif len(self.computer.item) == 0:
                    action = random.randint(1,2)
                else:
                    action = random.randint(1,3)
                if (live_bullet > blank) & (action == 2):
                    action = 1
                if (self.computer.bullet_pattern[0] == 'live') and (action == 2):
                    action = 1
                elif (self.computer.bullet_pattern[0] == 'blank') and (action == 1):
                    action = 2
                
                if (self.computer.bullet_pattern[0] == 'blank') & ('轉換器' in self.computer.item):
                    print('莊家使用了轉換器,現在這發子彈將反轉')
                    remain_bullet[0] = True
                    live_bullet += 1
                    blank -= 1
                    self.computer.bullet_pattern[0] = 'live'
                    self.computer.item.remove('轉換器')
                    time.sleep(2)
                    continue
                if (self.computer.bullet_pattern[0] == 'live') & ('手鋸' in self.computer.item) and not handsaw:  
                    handsaw = True
                    print('莊家使用了手鋸,下一發子彈造成兩倍傷害')
                    time.sleep(2)
                    self.computer.item.remove('手鋸')
                    action = 1
                if '未知藍圖' in self.computer.item:
                    #馬上使用未知藍圖
                    print('莊家使用了未知藍圖')
                    time.sleep(2)
                    temp = random.randint(1,5)
                    if temp == 1:
                        print('莊家獲得了禁藥')
                        
                        self.computer.item.append('禁藥')
                    elif temp == 2:
                        print('莊家獲得了大口徑子彈')
                        
                        self.computer.item.append('大口徑子彈')
                    elif temp == 3:
                        print('莊家獲得了榴彈砲')
                        
                        self.computer.item.append('榴彈砲')
                    elif temp == 4:
                        print('莊家獲得了彈藥包')
                        
                        self.computer.item.append('彈藥包')
                    elif temp == 5:
                        print('莊家獲得了擴增背包')
                        
                        self.computer.max_item += 1
                    self.computer.item.remove('未知藍圖')
                    time.sleep(2)
                    continue
                if gun_lock and action == 2:
                    action = 1
                #莊家的行動選項和玩家相同
                if action==1:
                    try_count = 0
                    if remain_bullet[0]&handsaw&killer_queen:
                        self.player.hp -= 10
                        print('莊家使用漆黑皇后射中了你,造成十點傷害')
                        if self.player.blood_queen > 0:
                            print('腥紅皇后使你免疫額外傷害')
                            self.player.hp += 5
                            self.player.blood_queen -= 1
                        handsaw = False
                        killer_queen = False
                        live_bullet -= 1
                        self.computer.pop_bullet_pattern()
                    elif remain_bullet[0]&killer_queen:
                        self.player.hp -= 5
                        print('莊家使用漆黑皇后射中了你,造成五點傷害')
                        live_bullet -= 1
                        self.computer.pop_bullet_pattern()
                        killer_queen = False
                    elif remain_bullet[0]&handsaw:
                        self.player.hp -= 2
                        print('莊家射中了你,造成兩點傷害')
                        if self.player.blood_queen > 0:
                            print('腥紅皇后使你免疫額外傷害')
                            self.player.hp += 1
                            self.player.blood_queen -= 1
                        handsaw = False
                        live_bullet -= 1
                        self.computer.pop_bullet_pattern()
                    elif remain_bullet[0]:
                        self.player.hp -= 1
                        print('莊家射中了你,造成一點傷害')
                        live_bullet -= 1
                        self.computer.pop_bullet_pattern()
                    else:
                        print('莊家的子彈打空了')
                        blank -= 1
                        self.computer.pop_bullet_pattern()
                        handsaw = False
                    remain_bullet.pop(0)
                    handsaw = False
                elif action==2:
                    try_count = 0
                    if remain_bullet[0] and (self.computer.fog > 0):
                        print('朦朧國王使莊家射偏了')
                        self.computer.fog -= 1
                        handsaw = False
                        killer_queen = False
                        live_bullet -= 1
                        self.computer.pop_bullet_pattern()
                    elif remain_bullet[0]&handsaw&killer_queen:
                        self.computer.hp -= 10
                        print('莊家使用漆黑皇后射中了自己,造成十點傷害')
                        if self.computer.blood_queen > 0:
                            print('腥紅皇后使你免疫額外傷害')
                            self.computer.hp += 5
                            self.computer.blood_queen -= 1
                        else:
                            print('你逃過了一截')
                        handsaw = False
                        killer_queen = False
                        live_bullet -= 1
                        self.computer.pop_bullet_pattern()
                    elif remain_bullet[0]&killer_queen:
                        self.computer.hp -= 5
                        print('莊家使用漆黑皇后射中了自己,造成五點傷害')
                        print('你逃過了一截')
                        live_bullet -= 1
                        self.computer.pop_bullet_pattern()
                        killer_queen = False
                    elif remain_bullet[0]&handsaw:
                        self.computer.hp -= 2
                        print('莊家射中了自己,造成兩點傷害')
                        if self.computer.blood_queen > 0:
                            print('腥紅皇后使莊家免疫額外傷害')
                            self.computer.hp += 1
                            self.computer.blood_queen -= 1
                        handsaw = False
                        live_bullet -= 1
                        self.computer.pop_bullet_pattern()
                    elif remain_bullet[0]:
                        self.computer.hp -= 1
                        print('莊家射中了自己,造成一點傷害')
                        live_bullet -= 1
                        self.computer.pop_bullet_pattern()
                        handsaw = False
                    else:
                        print('莊家射向自己，子彈打空了,額外獲得一回合')
                        remain_bullet.pop(0)
                        self.computer.pop_bullet_pattern()
                        blank -= 1
                        handsaw = False
                        continue
                    remain_bullet.pop(0)
                    handsaw = False
                elif action==3:
                    item = random.randint(0,len(self.computer.item)-1)
                    if (self.computer.item[item] == '啤酒') & (self.computer.bullet_pattern[0]=='live'):
                        try_count +=1
                        continue
                    if (self.computer.item[item] == '手銬') & self.player.handcuff:
                        try_count +=1
                        continue
                    if (self.computer.item[item] == '過期藥物') & (self.computer.hp == 1):
                        try_count +=1
                        continue
                    if (self.computer.item[item] == '手機') & (len(remain_bullet) <= 2):
                        try_count +=1
                        continue
                    if (self.computer.item[item] == '手鋸') & handsaw:
                        try_count +=1
                        continue
                    if (self.computer.item[item] == '手鋸') & (self.computer.bullet_pattern[0] == 'blank'):
                        try_count +=1
                        continue
                    if (self.computer.item[item] == '榴彈砲') & (self.computer.bullet_pattern[0] == 'blank'):
                        try_count +=1
                        continue
                    if (self.computer.item[item] == '放大鏡') & (self.computer.bullet_pattern[0] == 'blank'):
                        try_count +=1
                        continue
                    if (self.computer.item[item] == '放大鏡') & (self.computer.bullet_pattern[0] == 'live'):
                        try_count +=1
                        continue
                    if (self.computer.item[item] == '手機') & ('unknown' not in self.computer.bullet_pattern):
                        try_count +=1
                        continue
                    if (self.computer.item[item] == '腎上腺素') & (len(self.player.item) == 0):
                        try_count +=1
                        continue     
                    try_count = 0
                    if self.computer.item[item] == '手鋸':
                        handsaw = True
                        print('莊家使用了手鋸,下一發子彈造成兩倍傷害')
                    elif self.computer.item[item] == '啤酒':
                        if remain_bullet.pop(0):
                            print('莊家使用了啤酒,退掉一發實彈')
                            live_bullet -= 1
                            self.computer.pop_bullet_pattern()
                        else:
                            print('莊家使用了啤酒,退掉一發空包彈')
                            blank -= 1
                            self.computer.pop_bullet_pattern()
                        if len(remain_bullet) == 0:
                            print('子彈打完了')
                            print('進入下一局')
                            return
                    elif self.computer.item[item] == '手機':
                        print('莊家使用了手機')
                        if len(remain_bullet) == 1:
                            n = 0
                        else:
                            n=random.randint(1,len(remain_bullet)-1)
                        if remain_bullet[n]:
                            self.computer.set_bullet_pattern(n,'live')
                        else:
                            self.computer.set_bullet_pattern(n,'blank')
                    elif self.computer.item[item] == '轉換器':
                        print('莊家使用了轉換器,現在這發子彈將反轉')
                        remain_bullet[0] = not remain_bullet[0]
                        if remain_bullet[0]:
                            live_bullet += 1
                            blank -= 1
                        else:
                            live_bullet -= 1
                            blank += 1
                        if self.computer.bullet_pattern[0] == 'live':
                            self.computer.set_bullet_pattern(0,'blank')
                        elif self.computer.bullet_pattern[0] == 'blank':
                            self.computer.set_bullet_pattern(0,'live')
                    elif self.computer.item[item] == '過期藥物':
                        print('莊家使用了過期藥物')
                        if random.randint(0,1):
                            self.computer.hp += 2
                            print('莊家回復了兩點血量')
                        else:
                            self.computer.hp -= 1
                            print('莊家失去了一點血量')
                            if self.computer.hp <= 0:
                                time.sleep(2)
                                print('**************************************')
                                print('你贏了')
                                time.sleep(2)
                                return
                    elif self.computer.item[item] == '放大鏡':
                        print('莊家使用了放大鏡')
                        self.computer.set_bullet_pattern(0,'live' if remain_bullet[0] else 'blank')
                    elif self.computer.item[item] == '香菸':
                        print('莊家使用了香菸,回復一點血量')
                        self.computer.hp += 1
                    elif self.computer.item[item] == '手銬':
                        print('莊家使用了手銬,你下回合無法行動')
                        self.player.dohandcuff()
                    elif self.computer.item[item] == '朦朧國王':
                        self.player.queen_used.append('朦朧國王')
                        print('莊家使用了***朦朧國王***，每回合額外免疫一次傷害')
                        #fog_king為上限，fog為當前免疫次數
                        self.computer.fog_king += 1
                        self.computer.fog += 1
                    elif self.computer.item[item] == '狂暴國王':
                        self.player.queen_used.append('狂暴國王')   
                        print('莊家使用了***狂暴國王***，下5發子彈造成兩倍傷害')
                        self.computer.rage_king += 5
                    elif self.computer.item[item] == '狡詐國王':
                        self.player.queen_used.append('狡詐國王')
                        print('莊家使用了***狡詐國王***，能夠預知部分未來')
                        self.computer.trick_king += 3
                    elif self.computer.item[item] == '貪婪國王':
                        print('莊家使用了***貪婪國王***，偷走你的道具')
                        self.player.queen_used.append('貪婪國王')
                        #偷走玩家所有非皇后道具，留下皇后道具
                        temp_item = []
                        for i in range(len(self.player.item)):
                            if self.player.item[i] != '漆黑皇后' and self.player.item[i] != '神聖皇后' and self.player.item[i] != '蔚藍皇后' and self.player.item[i] != '腥紅皇后':
                                self.computer.item.append(self.player.item[i])
                            else:
                                temp_item.append(self.player.item[i])
                        self.player.item = temp_item                         
                        self.computer.item.remove('貪婪國王')
                        skip = True
                    elif self.computer.item[item] == '未知藍圖':
                        print('莊家使用了未知藍圖')
                        time.sleep(2)
                        temp = random.randint(1,5)
                        if temp == 1:
                            print('莊家獲得了禁藥')
                            self.computer.item.pop(item)
                            self.computer.item.append('禁藥')
                        elif temp == 2:
                            print('莊家獲得了大口徑子彈')
                            self.computer.item.pop(item)
                            self.computer.item.append('大口徑子彈')
                        elif temp == 3:
                            print('莊家獲得了榴彈砲')
                            self.computer.item.pop(item)
                            self.computer.item.append('榴彈砲')
                        elif temp == 4:
                            print('莊家獲得了彈藥包')
                            self.computer.item.pop(item)
                            self.computer.item.append('彈藥包')
                        elif temp == 5:
                            print('莊家獲得了擴增背包')
                            self.computer.item.pop(item)
                            self.computer.max_item += 1
                    elif self.computer.item[item] == '禁藥':
                        print('莊家使用了禁藥')
                        if random.randint(1,10) <= 7:
                            self.computer.hp *= 2
                            self.computer.hp += 3
                            print('莊家的血量大幅提升,現在血量為',self.computer.hp)
                        else:
                            if self.computer.hp == 1:
                                print('莊家中毒身亡，你贏了')
                                self.computer.hp = 0
                                time.sleep(2)
                                return
                            self.computer.hp = 1
                            print('莊家中毒了，血量降為1')    
                    elif self.computer.item[item] == '大口徑子彈':
                        self.computer.item.pop(item)
                        if handsaw:
                            self.player.hp -= 6
                            print('莊家使用了大口徑子彈,造成6點傷害')
                        else:
                            self.player.hp -= 3
                            print('莊家使用了大口徑子彈,造成3點傷害')
                        if remain_bullet.pop(0):
                            live_bullet -= 1
                        else:
                            blank -= 1
                        self.computer.pop_bullet_pattern()
                        skip = True
                        handsaw = False
                    elif self.computer.item[item] == '榴彈砲':
                        self.computer.item.pop(item)
                        damage = self.computer.hp 
                        self.computer.hp = 1
                        if remain_bullet.pop(0):
                            if handsaw:
                                self.player.hp -= 2*damage
                                print('莊家使用了榴彈砲,造成',2*damage,'點傷害')
                                handsaw = False
                            else:
                                self.player.hp -= damage
                                print('莊家使用了榴彈砲,造成',damage,'點傷害')
                            live_bullet -= 1
                        else:
                            print('莊家使用了榴彈砲,但是子彈打空了')
                            blank -= 1
                            handsaw = False

                        self.computer.pop_bullet_pattern()
                        skip = True
                    elif self.computer.item[item] == '彈藥包':
                        damage = live_bullet
                        if handsaw:
                            damage *= 2
                            handsaw = False 
                        self.player.hp -= damage
                        print('莊家使用了彈藥包,對你造成',damage,'點傷害')
                        remain_bullet = []
                        live_bullet = 0
                        blank = 0
                        for i in range(8-len(remain_bullet)):
                            if random.randint(0,1):
                                remain_bullet.append(True)
                                live_bullet += 1
                            else:
                                remain_bullet.append(False)
                                blank += 1
                        random.shuffle(remain_bullet)
                        print('彈藥已重新裝填')
                        if self.player.blessing > 0:
                            handsaw = self.blessing(remain_bullet,'莊家',handsaw)
                        self.computer.reset_bullet_pattern(live_bullet+blank)

                    elif self.computer.item[item] == '腎上腺素':    
                        print('莊家使用了腎上腺素,可以偷取你的物品')
                        if len(self.player.item) == 0:
                            print('你沒有物品可以偷取')
                            continue
                        #隨機偷取玩家的一件物品，馬上使用偷取的物品
                        target = random.randint(0,len(self.player.item)-1)
                        steal = self.player.item.pop(target)
                        if steal == '手鋸':
                            handsaw = True
                            print('莊家偷走了手鋸,下一發子彈造成兩倍傷害')
                        elif steal == '啤酒':
                            if remain_bullet.pop(0):
                                print('莊家偷走了啤酒,退掉一發實彈')
                                live_bullet -= 1
                                self.computer.pop_bullet_pattern()
                            else:
                                print('莊家偷走了啤酒,退掉一發空包彈')
                                blank -= 1
                                self.computer.pop_bullet_pattern()
                            if len(remain_bullet) == 0:
                                print('子彈打完了')
                                print('進入下一局')
                                return
                        elif steal == '手機':
                            print('莊家偷走了手機')
                            if len(remain_bullet) == 1:
                                n = 0
                            else:
                                n=random.randint(1,len(remain_bullet)-1)
                            if remain_bullet[n]:
                                self.computer.set_bullet_pattern(n,'live')
                            else:
                                self.computer.set_bullet_pattern(n,'blank')
                        elif steal == '轉換器':
                            print('莊家偷走了轉換器,現在這發子彈將反轉')
                            remain_bullet[0] = not remain_bullet[0]
                            if remain_bullet[0]:
                                live_bullet += 1
                                blank -= 1
                            else:
                                live_bullet -= 1
                                blank += 1
                            if self.computer.bullet_pattern[0] == 'live':
                                self.computer.set_bullet_pattern(0,'blank')
                            elif self.computer.bullet_pattern[0] == 'blank':
                                self.computer.set_bullet_pattern(0,'live')
                        elif steal == '過期藥物':
                            print('莊家偷走了過期藥物')
                            if random.randint(0,1):
                                self.computer.hp += 2
                                print('莊家回復了兩點血量')
                            else:
                                self.computer.hp -= 1
                                print('莊家失去了一點血量')
                                if self.computer.hp <= 0:
                                    time.sleep(2)
                                    print('**************************************')
                                    print('你贏了')
                                    time.sleep(2)
                                    return
                        elif steal == '放大鏡':
                            print('莊家偷走了放大鏡')
                            self.computer.set_bullet_pattern(0,'live' if remain_bullet[0] else 'blank')
                        elif steal == '香菸':
                            print('莊家偷走了香菸,回復一點血量')
                            self.computer.hp += 1
                        elif steal == '手銬':
                            print('莊家偷走了手銬,你下回合無法行動')
                            self.player.dohandcuff()
                        elif steal == '漆黑皇后':
                            #效果和玩家使用漆黑皇后相同
                            print('莊家偷走了漆黑皇后，彈藥裝填為一發空包彈一發5點傷害實彈，祈禱吧!')
                            self.computer.item = []
                            self.player.item = []
                            remain_bullet = [True,False]
                            live_bullet = 1
                            blank = 1
                            self.computer.reset_bullet_pattern(live_bullet+blank)
                            random.shuffle(remain_bullet)
                            killer_queen = True
                            not_blue_print = False
                            if self.player.blessing > 0:
                                self.blessing(remain_bullet,'莊家',handsaw)
                        elif steal == '神聖皇后':
                            #效果和玩家使用神聖皇后相同
                            print('莊家偷走了神聖皇后，回復3點血量，背包上限+2，獲得3個隨機物品')
                            self.computer.hp += 3
                            self.computer.max_item += 2
                            self.give_participant_item(3,self.computer)
                        elif steal == '蔚藍皇后':
                            #效果和玩家使用蔚藍皇后相同
                            print('莊家偷走了蔚藍皇后，你獲得回合時莊家將獲得隨機物品')
                            self.computer.item_queen += 1
                        elif steal == '腥紅皇后':
                            #效果和玩家使用腥紅皇后相同
                            print('莊家偷走了腥紅皇后，你獲得回合時莊家將獲得手鋸效果')
                            self.computer.blood_queen += 1
                            
                        elif steal == '未知藍圖':
                            temp = random.randint(1,5)
                            if temp == 1:
                                print('莊家獲得了禁藥')
                                self.computer.item.append('禁藥')
                            elif temp == 2:
                                print('莊家獲得了大口徑子彈')
                                self.computer.item.append('大口徑子彈')
                            elif temp == 3:
                                print('莊家獲得了榴彈砲')
                                self.computer.item.append('榴彈砲')
                            elif temp == 4:
                                print('莊家獲得了彈藥包')
                                self.computer.item.append('彈藥包')
                            elif temp == 5:
                                print('莊家獲得了擴增背包')
                                self.computer.max_item += 1
                        elif steal == '禁藥':
                            print('莊家偷走了禁藥')
                            if random.randint(1,10) <= 7:
                                self.computer.hp *= 2
                                self.computer.hp += 3
                                print('莊家的血量大幅提升,現在血量為',self.computer.hp)
                            else:
                                if self.computer.hp == 1:
                                    print('莊家中毒身亡，你贏了')
                                    time.sleep(2)
                                    return
                                self.computer.hp = 1
                                print('莊家中毒了，血量降為1')
                        elif steal == '大口徑子彈':
                            if handsaw:
                                self.player.hp -= 6
                                print('莊家偷走了大口徑子彈,造成6點傷害')
                            else:
                                self.player.hp -= 3
                                print('莊家偷走了大口徑子彈,造成3點傷害')
                            if remain_bullet.pop(0):
                                live_bullet -= 1
                            else:
                                blank -= 1
                            handsaw = False
                            self.computer.pop_bullet_pattern()
                            if self.player.handcuff:
                                print('你被手銬銬住了,無法行動')
                                self.player.unhandcuff()
                                try_count = 0
                                continue
                            else:
                                break
                        elif steal == '榴彈砲':
                            damage = self.computer.hp 
                            self.computer.hp = 1
                            if remain_bullet.pop(0):
                                if handsaw:
                                    self.player.hp -= 2*damage
                                    print('莊家偷走了榴彈砲,造成',2*damage,'點傷害')
                                    handsaw = False
                                else:
                                    self.player.hp -= damage
                                    print('莊家偷走了榴彈砲,造成',damage,'點傷害')
                                live_bullet -= 1
                            else:
                                print('莊家偷走了榴彈砲,但是子彈打空了')
                                blank -= 1
                                handsaw = False
                            self.computer.pop_bullet_pattern()
                            if self.player.handcuff:
                                print('你被手銬銬住了,無法行動')
                                self.player.unhandcuff()
                                try_count = 0
                                continue
                            else:
                                break
                        elif steal == '彈藥包':
                            damage = live_bullet
                            if handsaw:
                                self.player.hp -= 2*damage
                                handsaw = False
                            self.player.hp -= damage
                            print('莊家偷走了彈藥包,對你造成',damage,'點傷害')
                            remain_bullet = []
                            live_bullet = 0
                            blank = 0
                            for i in range(8-len(remain_bullet)):
                                if random.randint(0,1):
                                    remain_bullet.append(True)
                                    live_bullet += 1
                                else:
                                    remain_bullet.append(False)
                                    blank += 1
                            random.shuffle(remain_bullet)
                            print('彈藥已重新裝填')
                            if self.player.blessing > 0:
                                handsaw = self.blessing(remain_bullet,'莊家',handsaw)
                            self.computer.reset_bullet_pattern(live_bullet+blank)
                        elif steal == '腎上腺素':
                            print('莊家試著偷取腎上腺素但失敗了')
                            self.player.item.append('腎上腺素')
                        elif steal == '琉璃皇后':
                            print('莊家試著偷取琉璃皇后但失敗了')
                            self.player.item.append('琉璃皇后')
                    if skip and not self.player.handcuff:
                        break
                    elif skip and self.player.handcuff:
                        print('你被手銬銬住了,無法行動')
                        self.player.unhandcuff()
                        try_count = 0
                        continue
                    if not_blue_print:
                        self.computer.item.pop(item)
                    continue
                if self.player.hp <= 0:
                    time.sleep(2)
                    print('**************************************')
                    print('你死了')
                    time.sleep(2)
                    if achievement_first_dead:
                        lobby_NPC[0].unlock_achievement('哈哈屁眼')
                    return
                if self.computer.hp <= 0:
                    time.sleep(2)
                    print('**************************************')
                    print('你贏了')
                    time.sleep(2)
                    return
                if self.player.handcuff:
                    print('你被手銬銬住了,無法行動')
                    self.player.unhandcuff()
                    try_count = 0
                    continue
                if len(remain_bullet) == 0:
                    print('子彈打完了')
                    print('進入下一局')
                    return
                if self.computer.item_queen > 0:
                    print('蔚藍皇后使莊家獲得隨機物品')
                    time.sleep(1)
                for i in range(self.computer.item_queen):
                    self.give_participant_item(1,self.computer)
                break

#試煉模式
class challenge_mode(game):
    def __init__(self, player, computer, hp, risk, challenger):
        if challenger == '薩邁爾':
            hp = 6
        elif challenger == '利維坦':
            hp = random.randint(4,6)
        elif challenger == '莉莉斯':
            pass
        self.player = player
        self.computer = computer
        self.player.hp = hp
        self.computer.hp = hp
        self.round = 1
        self.first_move = '玩家'
        self.item_list = ['放大鏡','香菸','手鋸','啤酒','手銬','手機','轉換器','過期藥物','腎上腺素']
        self.special_item = ['未知藍圖','禁藥','大口徑子彈','榴彈砲','彈藥包']
        self.queen = ['漆黑皇后','神聖皇后','蔚藍皇后','腥紅皇后','琉璃皇后'] 
        self.king = ['朦朧國王','狂暴國王','狡詐國王','貪婪國王']
        if risk % 2 == 0:
            self.item_list = ['放大鏡','香菸','手鋸','啤酒','手銬','手機','轉換器','過期藥物','腎上腺素','禁藥','大口徑子彈','榴彈砲','彈藥包']
            print('高風險模式，血量大幅提升')
            health = random.randint(3,10)
            self.player.hp += health
            self.computer.hp += health
        print('遊戲開始,每人有',self.player.hp,'點血量')
        self.challenger = challenger
        self.devil_princess_item_list = ['朦朧國王','狂暴國王','狡詐國王','貪婪國王','琉璃皇后','漆黑皇后','神聖皇后','蔚藍皇后','腥紅皇后','未知藍圖','禁藥','大口徑子彈','榴彈砲','彈藥包','放大鏡','香菸','手鋸','啤酒','手銬','手機','轉換器','過期藥物','腎上腺素']

    def give_item(self,number):
        if self.challenger != '惡魔公主':
            super().give_item(number)
        else:
            for i in range(number):
                if len(self.player.item) < self.player.max_item:
                    item=self.item_list[random.randint(0,len(self.item_list)-1)]
                    print('你獲得了',item)
                    self.player.item.append(item)
                else:
                    print('你的物品欄已滿')
                if len(self.computer.item) < self.computer.max_item:
                    self.computer.item.append(self.devil_princess_item_list[random.randint(0,len(self.devil_princess_item_list)-1)])
        
            self.player.item.sort(key = ['琉璃皇后','漆黑皇后','神聖皇后','蔚藍皇后','腥紅皇后','未知藍圖','禁藥','大口徑子彈','榴彈砲','彈藥包','放大鏡','香菸','手鋸','啤酒','手銬','手機','轉換器','過期藥物','腎上腺素'].index)
            self.computer.item.sort(key = ['朦朧國王','狂暴國王','狡詐國王','貪婪國王','琉璃皇后','漆黑皇后','神聖皇后','蔚藍皇后','腥紅皇后','未知藍圖','禁藥','大口徑子彈','榴彈砲','彈藥包','放大鏡','香菸','手鋸','啤酒','手銬','手機','轉換器','過期藥物','腎上腺素'].index)

    def give_Leviathan_item(self,number,participant):
        for i in range(number):
            if len(participant.item) < participant.max_item:
                time.sleep(1)
                self.item_list.extend(['禁藥','大口徑子彈','榴彈砲','彈藥包'])
                item=self.item_list[random.randint(0,len(self.item_list)-1)]
                for i in ['禁藥','大口徑子彈','榴彈砲','彈藥包']:
                    self.item_list.remove(i)
                print(' 利維坦獲得了',item)
                participant.item.append(item)
                
            else:
                print('物品欄已滿')
    
    def Lilit_life_steal(self):
        time.sleep(1.5)
        drain = ((self.round-1)//2) + 1
        print('莉莉斯使用了吸血鬼之吻')
        self.player.hp -= drain
        self.computer.hp += drain
        print('你的生命被莉莉斯吸取了',drain,'點')
        time.sleep(2)
            

    def player_bonus(self,win_count):
        if win_count == 0:
            for i in main_player.unlockable_item:
                if i =='永久藍圖':
                    self.player.item.append('未知藍圖')
                elif i == '隨機皇后':
                    if ('琉璃皇后' in main_player.unlockable_item) and (main_player.unlockable_item.count('隨機皇后') == 3) and '琉璃皇后' not in self.player.item:
                        self.player.item.append('琉璃皇后')
                    elif ('琉璃皇后' in main_player.unlockable_item) and '琉璃皇后' not in self.player.item:
                        self.player.item.append(self.queen[random.randint(0,4)])
                    else:
                        self.player.item.append(self.queen[random.randint(0,3)])
        for i in range(main_player.extra_hp):
            self.player.hp += 1
            
    def blessing(self,remain_bullet,turn,handsaw):
        print('★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★')
        print('琉璃祝福治癒了你的傷口')
        self.player.hp += self.player.blessing
        if remain_bullet[0] & (turn == '玩家'):
            print('你感覺到第一發子彈是實彈，這發子彈將造成兩倍傷害')
            print('★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★')
            time.sleep(2)
            return True
        elif remain_bullet[0] & (turn == '莊家'):   
            print('你感覺到第一發子彈是實彈，你將額外回復2點血量')
            self.player.hp += 2
        elif random.randint(0,1) and len(self.computer.item) > 0:
            print('你感覺到第一發子彈是空包彈，莊家的',self.computer.item[0],'將被摧毀')
            self.computer.item.pop(0)
        else:
            print('你感覺到第一發子彈是空包彈，你將額外獲得一個物品')
            self.give_participant_item(1,self.player)
        print('★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★')
        time.sleep(2)
        return handsaw

    def one_round_Leviathan(self,live_bullet,blank,item_number):
        time.sleep(3)
        print('第',self.round,'局開始')
        #朦朧國王效果
        self.computer.fog = self.computer.fog_king

        if self.player.handcuff:
            self.player.unhandcuff()
            print('你的手銬解除,可以自由行動了')
        if self.computer.handcuff:
            self.computer.unhandcuff()
            print('利維坦的手銬解除,可以自由行動了')
        handsaw = False
        skip = False
        killer_queen = False
        gun_lock = False
        self.give_item(item_number)
        remain_bullet = []
        self.computer.reset_bullet_pattern(live_bullet+blank)
        print('這局有',live_bullet,'發實彈',blank,'發空包彈')
        for i in range(live_bullet):
            remain_bullet.append(True)
        for i in range(blank):
            remain_bullet.append(False)
        random.shuffle(remain_bullet)
        #狡詐國王效果
        for i in range(self.computer.trick_king):
            if i > len(remain_bullet)-1:
                break
            elif remain_bullet[i]:
                self.computer.set_bullet_pattern(i,'live')
            else:
                self.computer.set_bullet_pattern(i,'blank')
        #琉璃祝福效果
        if self.player.blessing > 0:
            handsaw = self.blessing(remain_bullet,self.first_move,handsaw)

        time.sleep(2)        

        while len(remain_bullet) > 0:
            skip = False
            try_count = 0
            not_blue_print = True

            if self.player.hp <= 0:
                time.sleep(2)
                print('**************************************')
                print('你死了')
                time.sleep(2)
                return
            
            time.sleep(1)
            if self.first_move == '玩家':
                print('==========================================')
                print('你的回合')
                print('你的物品欄:',self.player.item)
                print('玩家血量:',self.player.hp,'利維坦血量:',self.computer.hp)  
                print('剩餘',live_bullet,'發實彈',blank,'發空包彈')
                print('請選擇要做的事')
                print('1.射向利維坦, 2.射向自己, 3.使用物品, 4.顯示利維坦的物品欄')
                if len(self.computer.bullet_pattern) != len(remain_bullet):
                    raise Exception('子彈數量不符')
                if self.player.blood_queen > 0 and (handsaw==False):
                    print('腥紅皇后使你獲得手鋸效果')
                    time.sleep(1)
                    handsaw = True
                    self.player.blood_queen -= 1
                if self.player.max_item >= 20:
                    lobby_NPC[0].unlock_achievement('道理我都懂，但是這個背包怎麼這麼大')
                    time.sleep(1)
                while True:
                    try:
                        action = int(input())
                    except ValueError:
                        print('請輸入正確的數字')
                        continue
                    if type(action) != int:
                        print('請輸入正確的數字')
                        continue
                    if action < 1 or action > 4:
                        print('請輸入正確的數字')
                        continue
                    break
            else:
                action = 0
                self.first_move = '玩家'
            
            if action==1:
                if remain_bullet[0] and (self.computer.fog > 0):
                    print('朦朧國王使你射偏了')
                    self.computer.pop_bullet_pattern()
                    self.computer.fog -= 1
                    handsaw = False
                    killer_queen = False
                    live_bullet -= 1
                elif remain_bullet[0] and handsaw and killer_queen:
                    self.computer.hp -= 10
                    print('你使用漆黑皇后射中了利維坦,造成十點傷害')
                    if self.computer.blood_queen > 0:
                        print('腥紅皇后使利維坦免疫額外傷害')
                        self.computer.hp += 5
                        self.computer.blood_queen -= 1
                    handsaw = False
                    killer_queen = False
                    self.computer.pop_bullet_pattern()
                    live_bullet -= 1
                    if (self.player.hp <= 5) and (self.computer.hp <= 0):
                        time.sleep(2)
                        lobby_NPC[0].unlock_achievement('漆黑子彈')
                elif remain_bullet[0]&killer_queen:
                    self.computer.hp -= 5
                    print('你使用漆黑皇后射中了利維坦,造成五點傷害')
                    self.computer.pop_bullet_pattern()
                    live_bullet -= 1
                    killer_queen = False
                    if (self.player.hp <= 5) and (self.computer.hp <= 0):
                        time.sleep(2)
                        lobby_NPC[0].unlock_achievement('漆黑子彈')
                elif remain_bullet[0]&handsaw:
                    self.computer.hp -= 2
                    print('你射中了利維坦,造成兩點傷害')
                    if self.computer.blood_queen > 0:
                        print('腥紅皇后使利維坦免疫額外傷害')
                        self.computer.hp += 1
                        self.computer.blood_queen -= 1
                    handsaw = False
                    self.computer.pop_bullet_pattern()
                    live_bullet -= 1
                elif remain_bullet[0]:
                    self.computer.hp -= 1
                    print('你射中了利維坦,造成一點傷害')
                    self.computer.pop_bullet_pattern()
                    live_bullet -= 1
                else:
                    print('你的子彈打空了')
                    self.computer.pop_bullet_pattern()
                    blank -= 1
                    handsaw = False
                remain_bullet.pop(0)
                handsaw = False
            elif action==2 and gun_lock :
                print('槍經過改造，這局無法再射向自己了')
                time.sleep(1)
                continue
            elif action==2:
                if remain_bullet[0]&handsaw&killer_queen:
                    self.player.hp -= 10
                    print('你用漆黑皇后射中了自己,造成十點傷害')
                    if self.player.blood_queen > 0:
                        print('腥紅皇后使你免疫額外傷害')
                        self.player.hp += 5
                        self.player.blood_queen -= 1
                    else:
                        print('節哀順變')
                    handsaw = False
                    killer_queen = False
                    self.computer.pop_bullet_pattern()
                    live_bullet -= 1
                elif remain_bullet[0]&killer_queen:
                    self.player.hp -= 5
                    print('你用漆黑皇后射中了自己,造成五點傷害')
                    print('節哀順變')
                    killer_queen = False
                    self.computer.pop_bullet_pattern()
                    live_bullet -= 1
                elif remain_bullet[0]&handsaw:
                    self.player.hp -= 2
                    print('你射中了自己,造成兩點傷害')
                    if self.player.blood_queen > 0:
                        print('腥紅皇后使你免疫額外傷害')
                        self.player.hp += 1
                        self.player.blood_queen -= 1
                    else:
                        print('你是笨蛋嗎?')
                        lobby_NPC[0].unlock_achievement('你是笨蛋嗎')
                    handsaw = False
                    self.computer.pop_bullet_pattern()
                    live_bullet -= 1
                elif remain_bullet[0]:
                    self.player.hp -= 1
                    print('你射中了自己,造成一點傷害')
                    self.computer.pop_bullet_pattern()
                    live_bullet -= 1
                    handsaw = False
                else:
                    print('你的子彈打空了,額外獲得一回合')
                    remain_bullet.pop(0)
                    self.computer.pop_bullet_pattern()
                    blank -= 1
                    handsaw = False
                    continue
                remain_bullet.pop(0)
                handsaw = False
            elif action==3:
                print('請選擇要使用的物品')
                for i in range(len(self.player.item)):
                    print(i+1,'.',self.player.item[i])
                try:
                    item = int(input())
                except ValueError:
                    print('請輸入正確的數字')
                    continue

                if item > len(self.player.item):    
                    print('請輸入正確的數字')
                    continue
                if self.player.item[item-1] == '手鋸':
                    if handsaw:
                        print('手鉅效果已經存在了')
                        continue
                    handsaw = True
                    print('你使用了手鋸,下一發子彈造成兩倍傷害')
                elif self.player.item[item-1] == '啤酒':
                    if remain_bullet.pop(0):
                        print('你使用了啤酒,退掉一發實彈')
                        live_bullet -= 1
                    else:
                        print('你使用了啤酒,退掉一發空包彈')
                        blank -= 1
                    self.computer.pop_bullet_pattern()
                    if len(remain_bullet) == 0:
                            print('子彈打完了')
                            print('進入下一局')
                            return
                elif self.player.item[item-1] == '手機':
                    print('你使用了手機')
                    if len(remain_bullet) == 1:
                        n = 0
                    else:
                        n=random.randint(1,len(remain_bullet)-1)
                    if remain_bullet[n]:
                        print('第',n+1,'發是實彈')
                    else:
                        print('第',n+1,'發是空包彈')
                elif self.player.item[item-1] == '轉換器':
                    print('你使用了轉換器,現在這發子彈將反轉')
                    remain_bullet[0] = not remain_bullet[0]
                    if remain_bullet[0]:
                        live_bullet += 1
                        blank -= 1
                    else:
                        live_bullet -= 1
                        blank += 1
                elif self.player.item[item-1] == '過期藥物':
                    print('你使用了過期藥物')
                    if random.randint(0,1):
                        self.player.hp += 2
                        print('你回復了兩點血量')
                    else:
                        self.player.hp -= 1
                        print('你失去了一點血量')
                        if self.player.hp <= 0:
                            time.sleep(2)
                            print('**************************************')
                            print('你死了')
                            time.sleep(2)
                            return
                elif self.player.item[item-1] == '放大鏡':
                    print('你使用了放大鏡看到 ','實彈' if remain_bullet[0] else '空包彈')
                elif self.player.item[item-1] == '香菸':
                    print('你使用了香菸,回復一點血量')
                    self.player.hp += 1
                elif self.player.item[item-1] == '手銬':
                    if self.computer.handcuff:
                        print('利維坦已經被銬住了')
                        continue
                    print('你使用了手銬,利維坦下回合無法行動')
                    self.computer.dohandcuff()
                elif self.player.item[item-1] == '未知藍圖':
                    if self.player.item.count('過期藥物') >= 3:
                        print('你獲得了禁藥')
                        self.player.item.append('禁藥')
                        for i in range(3):
                            self.player.item.remove('過期藥物')
                        self.player.item.remove('未知藍圖')
                    elif (self.player.item.count('手鋸') >= 2) and  (self.player.item.count('放大鏡') >= 1):
                        print('你獲得了大口徑子彈')
                        self.player.item.append('大口徑子彈')
                        for i in range(2):
                            self.player.item.remove('手鋸')
                        self.player.item.remove('放大鏡')
                        self.player.item.remove('未知藍圖')
                    elif (self.player.item.count('大口徑子彈') >= 1) and (self.player.item.count('腎上腺素') >= 1) and (self.player.item.count('轉換器') >= 1):
                        print('你獲得了榴彈砲')
                        self.player.item.append('榴彈砲')
                        self.player.item.remove('腎上腺素')
                        self.player.item.remove('大口徑子彈')
                        self.player.item.remove('轉換器')
                        self.player.item.remove('未知藍圖')
                    elif (self.player.item.count('啤酒') >= 2) and (self.player.item.count('香菸') >= 1) and ((live_bullet+blank) >= 3):
                        print('你獲得了彈藥包')
                        self.player.item.remove('啤酒')
                        self.player.item.remove('啤酒')
                        self.player.item.remove('香菸')
                        self.player.item.append('彈藥包')
                        self.player.item.remove('未知藍圖')
                    elif len(self.player.item) == self.player.max_item:
                        print('你獲得了擴增背包,物品欄增加2格')
                        self.player.item = []
                        self.player.max_item += 2
                    else:
                        print('你的物品不足以合成')
                        continue
                    not_blue_print = False
                elif self.player.item[item-1] == '禁藥':
                    #70%機率血量翻倍並+3，30%血量降低到1點，若血量為1則死亡
                    print('你使用了禁藥')
                    if random.randint(1,10) <= 7:
                        self.player.hp *= 2
                        self.player.hp += 3
                        print('你的血量大幅提升,現在血量為',self.player.hp)
                    else:
                        if self.player.hp == 1:
                            self.player.hp = 0
                            print('你死了')
                            time.sleep(2)
                            lobby_NPC[0].unlock_achievement('吸毒有礙身心健康，請勿隨意嘗試')
                            time.sleep(2)    
                            return
                        self.player.hp = 1
                        print('你中毒了，血量降為1')
                elif self.player.item[item-1] == '大口徑子彈':
                    #將目前這發直接子彈替換成大口徑子彈並直接發射，造成3點傷害，如果有使用手鋸則造成6點傷害
                    if self.computer.fog > 0:
                        print('朦朧國王使你射偏了')
                        self.computer.fog -= 1
                        handsaw = False
                    elif handsaw:
                        self.computer.hp -= 6
                        print('你發射了大口徑子彈,造成6點傷害')
                    else:
                        self.computer.hp -= 3
                        print('你發射了大口徑子彈,造成3點傷害')
                    if remain_bullet.pop(0):
                        live_bullet -= 1
                    else:
                        blank -= 1
                    self.computer.pop_bullet_pattern()
                    self.player.item.pop(item-1)
                    skip = True
                    handsaw = False
                elif self.player.item[item-1] == '榴彈砲':
                    #將自身血量降低至1點，並發射現在這發子彈，若為實彈則造成(降低的血量+1)點傷害，使用手鋸則造成兩倍傷害，若為空包彈則不造成傷害，使用後輪到利維坦的回合
                    damage = self.player.hp
                    self.player.hp = 1
                    if remain_bullet.pop(0):
                        if self.computer.fog > 0:
                            print('朦朧國王使你射偏了')
                            self.computer.fog -= 1
                            handsaw = False
                        elif handsaw:
                            self.computer.hp -= 2*damage
                            print('你發射了榴彈砲,造成',2*damage,'點傷害')
                            handsaw = False
                        else:
                            self.computer.hp -= damage
                            print('你發射了榴彈砲,造成',damage,'點傷害')
                        live_bullet -= 1
                    else:
                        print('你發射了榴彈砲,但是子彈打空了')
                        blank -= 1
                    self.computer.pop_bullet_pattern()
                    self.player.item.pop(item-1)
                    skip = True
                elif self.player.item[item-1] == '彈藥包':
                    #對利維坦造成剩餘實彈數量的傷害，之後用實彈和空包彈隨機將彈藥填滿至8發
                    damage = live_bullet
                    if self.computer.fog > 0:
                        if damage > self.computer.fog:
                            damage -= self.computer.fog
                            self.computer.fog = 0
                            if handsaw:
                                damage *= 2
                            self.computer.hp -= damage
                            print('你使用了彈藥包')
                            print('朦朧國王使你射偏了部分子彈,對利維坦造成',damage,'點傷害')
                        else:
                            print('你使用了彈藥包，但是朦朧國王使你射偏了所有子彈') 
                            self.computer.fog -= damage
                    else:
                        if handsaw:
                            damage *= 2
                        print('你使用了彈藥包,對利維坦造成',damage,'點傷害')
                        self.computer.hp -= damage
                    handsaw = False
                    remain_bullet = []
                    live_bullet = 0
                    blank = 0
                    for i in range(8-len(remain_bullet)):
                        if random.randint(0,1):
                            remain_bullet.append(True)
                            live_bullet += 1
                        else:
                            remain_bullet.append(False)
                            blank += 1
                    random.shuffle(remain_bullet)
                    print('彈藥已重新裝填')
                    self.computer.reset_bullet_pattern(live_bullet+blank)
                    if self.player.blessing > 0:
                        handsaw = self.blessing(remain_bullet,'玩家',handsaw)
                elif self.player.item[item-1] == '漆黑皇后':
                    #移除雙方所有道具，將彈夾裝填為一發空包彈一發實彈，這發實彈將造成5點傷害
                    print('你使用了漆黑皇后，彈藥裝填為一發空包彈一發5點傷害實彈，祈禱吧!')
                    self.player.item = []
                    self.computer.item = []
                    remain_bullet = [True,False]
                    live_bullet = 1
                    blank = 1
                    self.computer.reset_bullet_pattern(live_bullet+blank)
                    random.shuffle(remain_bullet)
                    killer_queen = True
                    not_blue_print = False
                    self.player.queen_used.append('漆黑皇后')
                    if self.player.blessing > 0:
                        handsaw = self.blessing(remain_bullet,'玩家',handsaw)
                elif self.player.item[item-1] == '神聖皇后':
                    #回3點血量，背包上限+2，獲得3個隨機物品
                    print('你使用了神聖皇后，回復3點血量，背包上限+2，獲得3個隨機物品')
                    self.player.hp += 3
                    self.player.max_item += 3
                    self.give_participant_item(3,self.player)
                    self.player.max_item -= 1
                    self.player.queen_used.append('神聖皇后')
                elif self.player.item[item-1] == '蔚藍皇后':
                    #玩家的回合結束時，獲得一個隨機物品
                    print('你使用了蔚藍皇后，輪到利維坦的回合時你將獲得一個隨機物品')
                    self.player.item_queen += 1   
                    self.player.queen_used.append('蔚藍皇后')
                    if self.player.item_queen >= 5 :
                        time.sleep(1)
                        lobby_NPC[0].unlock_achievement('道具永動機')
                        time.sleep(1)
                elif self.player.item[item-1] == '腥紅皇后':
                    #玩家的回合開始時，附加手鉅效果
                    print('你使用了腥紅皇后，每回合獲得手鋸效果並免疫手鉅的額外傷害，可以觸發五次')
                    self.player.blood_queen += 5       
                    self.player.queen_used.append('腥紅皇后') 
                elif self.player.item[item-1] == '琉璃皇后':
                    #每次重新裝彈(回合開始、彈藥包、漆黑皇后)時通靈第一顆子彈，若為實彈則附加手鉅效果
                    #若為空包彈則回復一點血量並消除利維坦一個道具或獲得一個隨機道具
                    #使用當下清空利維坦的道具、清空彈夾並裝上一顆實彈
                    print('你獲得了琉璃的祝福，利維坦的道具被清空，彈夾重新裝填了')
                    time.sleep(2)
                    lobby_NPC[0].unlock_achievement('琉璃的祝福')
                    self.computer.item = [] 
                    self.computer.reset_bullet_pattern(1)
                    remain_bullet = [True]
                    if not handsaw:
                        handsaw = True
                        print('你獲得了手鋸效果')
                    time.sleep(1)
                    live_bullet = 1
                    blank = 0
                    self.player.blessing += 1
                    self.player.queen_used.append('琉璃皇后')                          
                elif self.player.item[item-1] == '腎上腺素':
                    print('你使用了腎上腺素,可以偷取利維坦的物品')
                    if len(self.computer.item) == 0:
                        print('利維坦沒有物品可以偷取')
                        continue
                    print('請選擇要偷取的物品:')
                    for i in range(len(self.computer.item)):
                        print(i+1,'.',self.computer.item[i])
                    try:
                        steal = int(input())
                    except ValueError:
                        print('請輸入正確的數字')
                        time.sleep(1)
                        continue  
                    if steal > len(self.computer.item):
                        print('請輸入正確的數字')
                        continue
                    elif steal <= 0:
                        print('請輸入正確的數字')
                        continue
                    #馬上使用選擇的物品 
                    if self.computer.item[steal-1] == '手鋸':
                        if handsaw:
                            print('手鉅效果已經存在了')
                            continue
                        handsaw = True
                        print('你使用了手鋸,下一發子彈造成兩倍傷害')
                    elif self.computer.item[steal-1] == '啤酒':
                        if remain_bullet.pop(0):
                            print('你使用了啤酒,退掉一發實彈')
                            live_bullet -= 1
                        else:
                            print('你使用了啤酒,退掉一發空包彈')
                            blank -= 1
                        self.computer.pop_bullet_pattern()
                        if len(remain_bullet) == 0:
                            print('子彈打完了')
                            print('進入下一局')
                            return
                    elif self.computer.item[steal-1] == '手機':
                        print('你使用了手機')
                        if len(remain_bullet) == 1:
                            n = 0
                        else:
                            n=random.randint(1,len(remain_bullet)-1)
                        if remain_bullet[n]:
                            print('第',n+1,'發是實彈')
                        else:
                            print('第',n+1,'發是空包彈')
                    elif self.computer.item[steal-1] == '轉換器':
                        print('你使用了轉換器,現在這發子彈將反轉')
                        remain_bullet[0] = not remain_bullet[0]
                        if remain_bullet[0]:
                            live_bullet += 1
                            blank -= 1
                        else:
                            live_bullet -= 1
                            blank += 1
                    elif self.computer.item[steal-1] == '過期藥物':
                        print('你使用了過期藥物')
                        if random.randint(0,1):
                            self.player.hp += 2
                            print('你回復了兩點血量')
                        else:
                            self.player.hp -= 1
                            print('你失去了一點血量')
                            if self.player.hp <= 0:
                                time.sleep(2)
                                print('**************************************')
                                print('你死了')
                                time.sleep(2)
                                return
                    elif self.computer.item[steal-1] == '放大鏡':
                        print('你使用了放大鏡看到 ','實彈' if remain_bullet[0] else '空包彈')
                    elif self.computer.item[steal-1] == '香菸':
                        print('你使用了香菸,回復一點血量')
                        self.player.hp += 1
                    elif self.computer.item[steal-1] == '手銬':
                        if self.computer.handcuff:
                            print('利維坦已經被銬住了')
                            continue
                        print('你使用了手銬,利維坦下回合無法行動')
                        self.computer.dohandcuff()
                    elif self.computer.item[steal-1] == '未知藍圖':
                        self.player.item.append('未知藍圖')
                        print('你獲得了未知藍圖')
                    elif self.computer.item[steal-1] == '禁藥':
                        print('你使用了禁藥')
                        if random.randint(1,10) <= 7:
                            self.player.hp *= 2
                            self.player.hp += 3
                            print('你的血量大幅提升,現在血量為',self.player.hp)
                        else:
                            if self.player.hp == 1:
                                print('你死了')
                                self.player.hp = 0
                                time.sleep(2)
                                lobby_NPC[0].unlock_achievement('吸毒有礙身心健康，請勿隨意嘗試')
                                time.sleep(2)    
                                return
                            self.player.hp = 1
                            print('你中毒了，血量降為1')
                    elif self.computer.item[steal-1] == '大口徑子彈':
                        if self.computer.fog > 0:
                            print('朦朧國王使你射偏了')
                            self.computer.fog -= 1
                            handsaw = False
                        elif handsaw:
                            self.computer.hp -= 6
                            print('你使用了大口徑子彈,造成6點傷害')
                        else:
                            self.computer.hp -= 3
                            print('你使用了大口徑子彈,造成3點傷害')
                        if remain_bullet.pop(0):
                            live_bullet -= 1
                        else:
                            blank -= 1
                        self.computer.pop_bullet_pattern()
                        handsaw = False
                    elif self.computer.item[steal-1] == '榴彈砲':
                        damage = self.player.hp 
                        self.player.hp = 1
                        if remain_bullet.pop(0):
                            if self.computer.fog > 0:
                                print('朦朧國王使你射偏了')
                                self.computer.fog -= 1
                                handsaw = False
                            elif handsaw:
                                self.computer.hp -= 2*damage
                                print('你使用了榴彈砲,造成',2*damage,'點傷害')
                                handsaw = False
                                if damage >= 15:
                                    lobby_NPC[0].unlock_achievement('巨砲')
                            else:
                                self.computer.hp -= damage
                                print('你使用了榴彈砲,造成',damage,'點傷害')
                                if damage >= 30:
                                    lobby_NPC[0].unlock_achievement('巨砲')
                            live_bullet -= 1
                        else:
                            print('你使用了榴彈砲,但是子彈打空了')
                            blank -= 1
                            handsaw = False
                        self.computer.pop_bullet_pattern()
                    elif self.computer.item[steal-1] == '彈藥包':
                        damage = live_bullet
                        if self.computer.fog > 0:
                            if damage > self.computer.fog:
                                damage -= self.computer.fog
                                self.computer.fog = 0
                                if handsaw:
                                    damage *= 2
                                self.computer.hp -= damage
                                print('你使用了彈藥包')
                                print('朦朧國王使你射偏了部分子彈,對利維坦造成',damage,'點傷害')
                            else:
                                print('你使用了彈藥包，但是朦朧國王使你射偏了所有子彈') 
                                self.computer.fog -= damage
                        else:
                            if handsaw:
                                damage *= 2
                            print('你使用了彈藥包,對利維坦造成',damage,'點傷害')
                            self.computer.hp -= damage
                        handsaw = False
                        remain_bullet = []
                        live_bullet = 0
                        blank = 0
                        for i in range(8-len(remain_bullet)):
                            if random.randint(0,1):
                                remain_bullet.append(True)
                                live_bullet += 1
                            else:
                                remain_bullet.append(False)
                                blank += 1
                        random.shuffle(remain_bullet)
                        print('彈藥已重新裝填')
                        self.computer.reset_bullet_pattern(live_bullet+blank)
                        if self.player.blessing > 0:
                            handsaw = self.blessing(remain_bullet,'玩家',handsaw)
                        
                    elif self.computer.item[steal-1] == '腎上腺素':
                        print('你不能偷取腎上腺素')
                        time.sleep(2)
                        lobby_NPC[0].unlock_achievement('就說了不行')
                        continue
                    else:
                        print('你不能偷取國王道具')
                        continue
                    self.computer.item.pop(steal-1)

                if not_blue_print and not skip: 
                    self.player.item.pop(item-1)
                time.sleep(2)
                if self.computer.hp <= 0:
                    time.sleep(2)
                    print('**************************************')
                    print('你贏了')
                    time.sleep(2)
                    return
                if not skip:
                    continue
            elif action==4:
                print('利維坦的物品欄:',self.computer.item)
                time.sleep(4)
                continue
            if self.computer.hp <= 0:
                time.sleep(2)
                print('**************************************')
                print('你贏了')
                time.sleep(2)
                return
            if self.player.hp <= 0:
                time.sleep(2)
                print('**************************************')
                print('你死了')
                time.sleep(2)
                return
            if len(remain_bullet) == 0:
                print('子彈打完了')
                print('進入下一局')
                return
            if self.player.item_queen > 0:
                print('蔚藍皇后使你獲得隨機物品')
                time.sleep(1)
            for i in range(self.player.item_queen):
                self.give_participant_item(1,self.player)
            print('==========================================')
            print('利維坦的回合')
            print('==========================================')
            time.sleep(1)
            try_count = 0
            not_blue_print = True
            if action == 0:
                achivement_first_dead = True
            else:
                achivement_first_dead = False
            '''
            利維坦道具說明:
            國王和皇后效果不變
            1.未知藍圖
                讓利維坦獲得3個隨機物品
            2.手鉅
                直接對玩家造成1點傷害
            3.香菸
                將這發空包彈變成實彈，若是實彈則退彈
            4.啤酒
                回復一點血量
            5.手機
                改變剩餘所有子彈的順序，偷看兩發子彈
            6.轉換器
                轉換所有子彈
            7.過期藥物
                (用吸的(X
                獲得一層朦朧國王效果
            8.放大鏡
                增加一格背包空間，裝填3發隨機子彈
            9.腎上腺素
                獲得手鉅效果
            10.手銬
                打完剩餘子彈前兩人皆無法再射向自己
            11.禁藥
                獲得額外回合(就是手銬效果)，獲得手鉅效果
            12.大口徑子彈
                把所有空包彈變成實彈
            13.榴彈砲
                造成剩餘子彈數量的傷害
            14.彈藥包
                退到剩下一發子彈，每退一發實彈回一點血，每退一發空包彈造成一點傷害

            '''

            if self.computer.handcuff:
                print('利維坦被手銬銬住了,無法行動')
                self.computer.unhandcuff()
                continue

            skip = False
            not_blue_print = True

            while True:
                #利維坦進行剩餘子彈分析
                if (live_bullet-self.computer.known_live) <= 0:
                    for i in range(len(self.computer.bullet_pattern)):
                        if self.computer.bullet_pattern[i] == 'unknown':
                            self.computer.set_bullet_pattern(i,'blank')
                elif (blank-self.computer.known_blank) <= 0:
                    for i in range(len(self.computer.bullet_pattern)):
                        if self.computer.bullet_pattern[i] == 'unknown':
                            self.computer.set_bullet_pattern(i,'live')
                if self.player.hp <= 0:
                    time.sleep(2)
                    print('**************************************')
                    print('你死了')
                    time.sleep(2)
                    return
                time.sleep(2)
                if len(remain_bullet) == 0:
                    print('子彈打完了')
                    print('進入下一局')
                    return
                if (self.computer.rage_king > 0) and (handsaw == False):
                    print('狂暴國王給予利維坦手鉅效果')
                    time.sleep(1)
                    handsaw = True
                    self.computer.rage_king -= 1
                if self.computer.item.count('腥紅皇后') > 0 & (not handsaw):
                    print('腥紅皇后使利維坦獲得手鋸效果')
                    time.sleep(1)
                    handsaw = True
                    self.computer.blood_queen -= 1
                #利維坦的行動判斷
                if len(self.computer.bullet_pattern) != len(remain_bullet):
                    raise Exception('子彈數量不符')
                if len(self.computer.item) > 3 :
                    if try_count >= 5:
                        action = random.randint(1,2)
                        if self.computer.bullet_pattern[0] == 'live':
                            action = 1
                        elif self.computer.bullet_pattern[0] == 'blank':
                            action = 2
                    else:
                        action = 3
                elif ('朦朧國王' in self.computer.item or '狂暴國王' in self.computer.item or '狡詐國王' in self.computer.item or '貪婪國王' in self.computer.item):
                    action = 3
                elif self.computer.bullet_pattern[0] == 'live':
                    action = 1
                elif self.computer.bullet_pattern[0] == 'blank':
                    action = 2
                elif len(self.computer.item) == 0:
                    action = random.randint(1,2)
                else:
                    action = random.randint(1,3)
                if (self.computer.bullet_pattern[0] == 'live') and (action == 2):
                    action = 1
                elif (self.computer.bullet_pattern[0] == 'blank') and (action == 1):
                    action = 2
                if (live_bullet > blank) & (action == 2):
                    action = 1
                if handsaw & (action == 2):
                    action = 1
                #利維坦手銬效果
                if gun_lock and (action == 2):
                    action = 1
                
                if (self.computer.bullet_pattern[0] == 'live') & ('腎上腺素' in self.computer.item) and not handsaw:  
                    print('利維坦使用了腎上腺素，眼神變得狂暴')
                    self.computer.item.remove('腎上腺素')
                    handsaw = True
                    continue
                if '未知藍圖' in self.computer.item:
                    #使用未知藍圖得到3個物品
                    print('利維坦撕碎未知藍圖，接著憑空變出了三樣物品')
                    self.give_Leviathan_item(3,self.computer)
                    self.computer.item.remove('未知藍圖')
                    continue
                    
                #利維坦的行動選項和玩家相同
                if action==1:
                    try_count = 0
                    if remain_bullet[0]&handsaw&killer_queen:
                        self.player.hp -= 10
                        print('利維坦使用漆黑皇后射中了你,造成十點傷害')
                        if self.player.blood_queen > 0:
                            print('腥紅皇后使你免疫額外傷害')
                            self.player.hp += 5
                            self.player.blood_queen -= 1
                        handsaw = False
                        killer_queen = False
                        live_bullet -= 1
                        self.computer.pop_bullet_pattern()
                    elif remain_bullet[0]&killer_queen:
                        self.player.hp -= 5
                        print('利維坦使用漆黑皇后射中了你,造成五點傷害')
                        live_bullet -= 1
                        self.computer.pop_bullet_pattern()
                        killer_queen = False
                    elif remain_bullet[0]&handsaw:
                        self.player.hp -= 2
                        print('利維坦射中了你,造成兩點傷害')
                        if self.player.blood_queen > 0:
                            print('腥紅皇后使你免疫額外傷害')
                            self.player.hp += 1
                            self.player.blood_queen -= 1
                        handsaw = False
                        live_bullet -= 1
                        self.computer.pop_bullet_pattern()
                    elif remain_bullet[0]:
                        self.player.hp -= 1
                        print('利維坦射中了你,造成一點傷害')
                        live_bullet -= 1
                        self.computer.pop_bullet_pattern()
                    else:
                        print('利維坦的子彈打空了')
                        blank -= 1
                        self.computer.pop_bullet_pattern()
                        handsaw = False
                    remain_bullet.pop(0)
                    handsaw = False
                elif action==2:
                    try_count = 0
                    if remain_bullet[0] and (self.computer.fog > 0):
                        print('朦朧國王使利維坦射偏了')
                        self.computer.fog -= 1
                        handsaw = False
                        killer_queen = False
                        live_bullet -= 1
                        self.computer.pop_bullet_pattern()
                    elif remain_bullet[0]&handsaw&killer_queen:
                        self.computer.hp -= 10
                        print('利維坦使用漆黑皇后射中了自己,造成十點傷害')
                        if self.computer.blood_queen > 0:
                            print('腥紅皇后使你免疫額外傷害')
                            self.computer.hp += 5
                            self.computer.blood_queen -= 1
                        else:
                            print('你逃過了一截')
                        handsaw = False
                        killer_queen = False
                        live_bullet -= 1
                        self.computer.pop_bullet_pattern()
                    elif remain_bullet[0]&killer_queen:
                        self.computer.hp -= 5
                        print('利維坦使用漆黑皇后射中了自己,造成五點傷害')
                        print('你逃過了一截')
                        live_bullet -= 1
                        self.computer.pop_bullet_pattern()
                        killer_queen = False
                    elif remain_bullet[0]&handsaw:
                        self.computer.hp -= 2
                        print('利維坦射中了自己,造成兩點傷害')
                        if self.computer.blood_queen > 0:
                            print('腥紅皇后使利維坦免疫額外傷害')
                            self.computer.hp += 1
                            self.computer.blood_queen -= 1
                        handsaw = False
                        live_bullet -= 1
                        self.computer.pop_bullet_pattern()
                    elif remain_bullet[0]:
                        self.computer.hp -= 1
                        print('利維坦射中了自己,造成一點傷害')
                        live_bullet -= 1
                        self.computer.pop_bullet_pattern()
                        handsaw = False
                    else:
                        print('利維坦射向自己，子彈打空了,額外獲得一回合')
                        remain_bullet.pop(0)
                        self.computer.pop_bullet_pattern()
                        blank -= 1
                        handsaw = False
                        continue
                    remain_bullet.pop(0)
                    handsaw = False
                elif action==3:
                    item = random.randint(0,len(self.computer.item)-1)
                    if  ((not any(remain_bullet)) or all(remain_bullet)) and (self.computer.item[item] == '手機'):
                        try_count +=1
                        continue 
                    if handsaw and (self.computer.item[item] == '腎上腺素'):
                        try_count +=1
                        continue
                    if blank == 0 and (self.computer.item[item] == '大口徑子彈'):
                        try_count +=1
                        continue
                    if (self.player.hp >= 5) and (len(remain_bullet) <= 2) and (self.computer.item[item] == '榴彈砲'):
                        try_count +=1
                        continue
                    if (len(remain_bullet) == 1) and (self.computer.item[item] == '彈藥包'):
                        try_count +=1
                        continue
                    if (self.computer.bullet_pattern[0] == 'live') and (self.computer.item[item] == '香菸'):
                        try_count +=1
                        continue
                    if gun_lock and (self.computer.item[item] == '轉換器') and (self.computer.bullet_pattern[0] == 'live'):
                        try_count +=1
                        continue
                    if (self.computer.bullet_pattern[0] == 'live') and (self.computer.item[item] == '香菸'):
                        try_count +=1
                        continue
                    if gun_lock and (self.computer.item[item] == '手銬'):
                        try_count +=1
                        continue
                    try_count = 0
                    if self.computer.item[item] == '手鋸':
                        print('利維坦拿手鋸砍向你,造成了一點傷害')
                        time.sleep(1)
                        self.player.hp -= 1
                        print('利維坦:鋸子這種東西，拿來砍人不是挺好嗎?')
                    elif self.computer.item[item] == '啤酒':
                        self.computer.hp += 1
                        print('利維坦使用了啤酒,回復了一點血量')
                        time.sleep(1)
                        if random.randint(0,1):
                            print('利維坦: 嗝~')
                        else:
                            print('利維坦: 其實我不太喜歡喝酒就是了')
                    elif self.computer.item[item] == '手機':
                        print('利維坦使用了手機，改變了未來')
                        random.shuffle(remain_bullet)
                        self.computer.reset_bullet_pattern(live_bullet+blank)
                        self.computer.set_bullet_pattern(0,'live' if remain_bullet[0] else 'blank')
                        self.computer.set_bullet_pattern(1,'live' if remain_bullet[1] else 'blank')
                    elif self.computer.item[item] == '轉換器':
                        print('利維坦使用了轉換器,反轉了所有子彈')
                        for i in range(len(remain_bullet)):
                            remain_bullet[i] = not remain_bullet[i] 
                            if remain_bullet[i]:
                                live_bullet += 1
                                blank -= 1
                            else:
                                live_bullet -= 1
                                blank += 1
                            if self.computer.bullet_pattern[i] == 'live':
                                self.computer.set_bullet_pattern(i,'blank')
                            elif self.computer.bullet_pattern[i] == 'blank':
                                self.computer.set_bullet_pattern(i,'live')
                    elif self.computer.item[item] == '過期藥物':
                        print('利維坦吸了一些過期藥物，high了起來')
                        self.computer.fog += 1
                        time.sleep(1)
                        print('利維坦:這才是這貨真正的用法')
                    elif self.computer.item[item] == '放大鏡':
                        print('利維坦使用了放大鏡,身前的空間被扭曲了')
                        self.computer.max_item += 1
                        for i in range(3):
                            if random.randint(0,1):
                                remain_bullet.append(True)
                                live_bullet += 1
                            else:
                                remain_bullet.append(False)
                                blank += 1
                        self.computer.bullet_pattern.append('unknown')
                        self.computer.bullet_pattern.append('unknown')
                        self.computer.bullet_pattern.append('unknown')
                    elif self.computer.item[item] == '香菸':
                        if remain_bullet[0]:
                            print('利維坦抽了根菸,退掉一發實彈')
                            live_bullet -= 1
                            remain_bullet.pop(0)
                            self.computer.pop_bullet_pattern()
                        else:
                            print('利維坦把香菸塞進槍裡,空包彈被換成了實彈')
                            remain_bullet[0] = True
                            live_bullet += 1
                            blank -= 1
                        if len(remain_bullet) == 0:
                            print('子彈打完了')
                            print('進入下一局')
                            return
                    elif self.computer.item[item] == '手銬':
                        print('利維坦用手銬改造了槍,這局無法再射向自己')
                        gun_lock = True
                    elif self.computer.item[item] == '朦朧國王':
                        print('利維坦使用了***朦朧國王***，每回合額外免疫一次傷害')
                        self.player.queen_used.append('朦朧國王')
                        #fog_king為上限，fog為當前免疫次數
                        self.computer.fog_king += 1
                        self.computer.fog += 1
                    elif self.computer.item[item] == '狂暴國王':
                        print('利維坦使用了***狂暴國王***，下5發子彈造成兩倍傷害')
                        self.player.queen_used.append('狂暴國王')   
                        self.computer.rage_king += 5
                    elif self.computer.item[item] == '狡詐國王':
                        print('利維坦使用了***狡詐國王***，能夠預知部分未來')
                        self.player.queen_used.append('狡詐國王')
                        self.computer.trick_king += 3
                    elif self.computer.item[item] == '貪婪國王':
                        print('利維坦使用了***貪婪國王***，偷走你的道具')
                        self.player.queen_used.append('貪婪國王')
                        #偷走玩家所有非皇后道具，留下皇后道具
                        temp_item = []
                        for i in range(len(self.player.item)):
                            if self.player.item[i] != '漆黑皇后' and self.player.item[i] != '神聖皇后' and self.player.item[i] != '蔚藍皇后' and self.player.item[i] != '腥紅皇后':
                                self.computer.item.append(self.player.item[i])
                            else:
                                temp_item.append(self.player.item[i])
                        self.player.item = temp_item                         
                        self.computer.item.remove('貪婪國王')
                        continue
                    elif self.computer.item[item] == '未知藍圖':
                        print('利維坦撕碎未知藍圖，接著憑空變出了三樣物品')
                        self.give_Leviathan_item(3,self.computer)
                        
                    elif self.computer.item[item] == '禁藥':
                        print('利維坦嗑了禁藥，身影變得模糊')
                        self.player.dohandcuff()
                        handsaw = True
                        
                    elif self.computer.item[item] == '大口徑子彈':
                        print('利維坦使用了大口徑子彈,所有空包彈被換成了實彈')
                        for i in range(len(remain_bullet)):
                            if remain_bullet[i] == False:
                                remain_bullet[i] = True
                                live_bullet += 1
                                blank -= 1
                    elif self.computer.item[item] == '榴彈砲':
                        print('利維坦使用榴彈砲強制射出所有子彈,造成了',live_bullet+blank,'點傷害')
                        self.player.hp -= live_bullet+blank
                        time.sleep(1)
                        print('利維坦:呼呼呼，管你實彈空包彈，射出去之後都是好子彈')
                        time.sleep(1)
                        print('子彈打完了')
                        print('進入下一局')
                        return
                    elif self.computer.item[item] == '彈藥包':
                        damage = 0
                        for i in range(len(remain_bullet)-1):
                            if remain_bullet.pop(0):
                                live_bullet -= 1
                                self.computer.hp += 1
                                self.computer.pop_bullet_pattern()
                            else:
                                damage += 1
                                self.computer.pop_bullet_pattern()
                                blank -= 1
                        if handsaw:
                            damage *= 2
                            handsaw = False 
                        self.player.hp -= damage
                        print('利維坦用彈藥包清空大部分子彈，回復',live_bullet,'點血量，並對你造成',damage,'點傷害')
                        
                    elif self.computer.item[item] == '腎上腺素':    
                        print('利維坦使用了腎上腺素，眼神變得狂暴')
                        handsaw = True
                    self.computer.item.pop(item)
                    continue
                if self.player.hp <= 0:
                    time.sleep(2)
                    print('**************************************')
                    print('你死了')
                    time.sleep(2)
                    if achievement_first_dead:
                        lobby_NPC[0].unlock_achievement('哈哈屁眼')
                    return
                if self.computer.hp <= 0:
                    time.sleep(2)
                    print('**************************************')
                    print('你贏了')
                    time.sleep(2)
                    return
                if self.player.handcuff:
                    print('利維坦的速度太快了，你無法行動')
                    self.player.unhandcuff()
                    try_count = 0
                    continue
                if len(remain_bullet) == 0:
                    print('子彈打完了')
                    print('進入下一局')
                    return
                if self.computer.item_queen > 0:
                    print('蔚藍皇后使利維坦獲得隨機物品')
                    time.sleep(1)
                for i in range(self.computer.item_queen):
                    self.give_participant_item(1,self.computer)
                break
            
    def one_round_Samael(self,live_bullet,blank,foresee):
        self.player.blessing = 0
        self.player.item = []
        self.computer.item = []
        time.sleep(3)
        print('第',self.round,'局開始')
        remain_bullet = []
        self.computer.reset_bullet_pattern(live_bullet+blank)
        print('這局有',live_bullet,'發實彈',blank,'發空包彈')
        for i in range(live_bullet):
            remain_bullet.append(True)
        for i in range(blank):
            remain_bullet.append(False)
        random.shuffle(remain_bullet)
        time.sleep(2)        
        #薩邁爾預知效果
        if foresee == 2:
            self.computer.set_bullet_pattern(0,'live' if remain_bullet[0] else 'blank')
            self.computer.set_bullet_pattern(1,'live' if remain_bullet[1] else 'blank')
        elif foresee == 4:
            while True:
                rand = random.randint(0,7)
                if self.computer.bullet_pattern[rand] == 'unknown':
                    self.computer.set_bullet_pattern(rand,'live' if remain_bullet[rand] else 'blank')
                    foresee -= 1
                if foresee == 0:
                    break
        
        while len(remain_bullet) > 0:
            if self.player.hp <= 0:
                time.sleep(2)
                print('**************************************')
                print('你死了')
                time.sleep(2)
                return
            
            time.sleep(1)
            if self.first_move == '玩家':
                print('==========================================')
                print('你的回合')
                print('玩家血量:',self.player.hp,'薩邁爾血量:',self.computer.hp)  
                print('剩餘',live_bullet,'發實彈',blank,'發空包彈')
                print('請選擇要做的事')
                print('1.射向薩邁爾, 2.射向自己')
                if len(self.computer.bullet_pattern) != len(remain_bullet):
                    raise Exception('子彈數量不符')
                while True:
                    try:
                        action = int(input())
                    except ValueError:
                        print('請輸入正確的數字')
                        continue
                    if type(action) != int:
                        print('請輸入正確的數字')
                        continue
                    if action < 1 or action > 2:
                        print('請輸入正確的數字')
                        continue
                    break
            else:
                action = 0
                self.first_move = '玩家'
            
            if action==1:
                if remain_bullet[0]:
                    self.computer.hp -= 1
                    print('你射中了薩邁爾,造成一點傷害')
                    self.computer.pop_bullet_pattern()
                    live_bullet -= 1
                else:
                    print('你的子彈打空了')
                    self.computer.pop_bullet_pattern()
                    blank -= 1
                remain_bullet.pop(0)
            elif action==2:
                if remain_bullet[0]:
                    self.player.hp -= 1
                    print('你射中了自己,造成一點傷害')
                    self.computer.pop_bullet_pattern()
                    live_bullet -= 1
                else:
                    print('你的子彈打空了,額外獲得一回合')
                    remain_bullet.pop(0)
                    self.computer.pop_bullet_pattern()
                    blank -= 1
                    continue
                remain_bullet.pop(0)
                if self.computer.hp <= 0:
                    time.sleep(2)
                    print('**************************************')
                    print('你贏了')
                    time.sleep(2)
                    return
            if self.computer.hp <= 0:
                time.sleep(2)
                print('**************************************')
                print('你贏了')
                time.sleep(2)
                return
            if self.player.hp <= 0:
                time.sleep(2)
                print('**************************************')
                print('你死了')
                time.sleep(2)
                return
            if len(remain_bullet) == 0:
                print('子彈打完了')
                print('進入下一局')
                return
            print('==========================================')
            print('薩邁爾的回合')
            print('==========================================')
            time.sleep(1)
            while True:
                #薩邁爾進行剩餘子彈分析
                if (live_bullet-self.computer.known_live) <= 0:
                    for i in range(len(self.computer.bullet_pattern)):
                        if self.computer.bullet_pattern[i] == 'unknown':
                            self.computer.set_bullet_pattern(i,'blank')
                elif (blank-self.computer.known_blank) <= 0:
                    for i in range(len(self.computer.bullet_pattern)):
                        if self.computer.bullet_pattern[i] == 'unknown':
                            self.computer.set_bullet_pattern(i,'live')
                if self.player.hp <= 0:
                    time.sleep(2)
                    print('**************************************')
                    print('你死了')
                    time.sleep(2)
                    return
                time.sleep(2)
                if len(remain_bullet) == 0:
                    print('子彈打完了')
                    print('進入下一局')
                    return
                #薩邁爾的行動判斷
                if self.computer.bullet_pattern[0] == 'live':
                    action = 1
                elif self.computer.bullet_pattern[0] == 'blank':
                    action = 2
                else:
                    remain_live = live_bullet - self.computer.known_live
                    remain_blank = blank - self.computer.known_blank
                    rand = random.randint(1,remain_live+remain_blank)
                    if rand <= remain_live:
                        action = 2
                    else:
                        action = 1
                    
                #薩邁爾的行動選項和玩家相同
                if action==1:
                    if remain_bullet[0]:
                        self.player.hp -= 1
                        print('薩邁爾射中了你,造成一點傷害')
                        live_bullet -= 1
                        self.computer.pop_bullet_pattern()
                    else:
                        print('薩邁爾的子彈打空了')
                        blank -= 1
                        self.computer.pop_bullet_pattern()
                    remain_bullet.pop(0)
                elif action==2:
                    if remain_bullet[0]:
                        self.computer.hp -= 1
                        print('薩邁爾射中了自己,造成一點傷害')
                        live_bullet -= 1
                        self.computer.pop_bullet_pattern()
                    else:
                        print('薩邁爾射向自己，子彈打空了,額外獲得一回合')
                        remain_bullet.pop(0)
                        self.computer.pop_bullet_pattern()
                        blank -= 1
                        continue
                    remain_bullet.pop(0)
                
                if self.player.hp <= 0:
                    time.sleep(2)
                    print('**************************************')
                    print('你死了')
                    time.sleep(2)
                    return
                if self.computer.hp <= 0:
                    time.sleep(2)
                    print('**************************************')
                    print('你贏了')
                    time.sleep(2)
                    return
                if len(remain_bullet) == 0:
                    print('子彈打完了')
                    print('進入下一局')
                    return
                break
            
    def one_round_Lilit(self,live_bullet,blank,item_number):
        time.sleep(3)
        print('第',self.round,'局開始')
        #朦朧國王效果
        self.computer.fog = self.computer.fog_king

        if self.player.handcuff:
            self.player.unhandcuff()
            print('你的手銬解除,可以自由行動了')
        if self.computer.handcuff:
            self.computer.unhandcuff()
            print('莉莉斯的手銬解除,可以自由行動了')
        handsaw = False
        skip = False    
        killer_queen = False
        self.give_item(item_number)
        remain_bullet = []
        self.computer.reset_bullet_pattern(live_bullet+blank)
        print('這局有',live_bullet,'發實彈',blank,'發空包彈')
        for i in range(live_bullet):
            remain_bullet.append(True)
        for i in range(blank):
            remain_bullet.append(False)
        random.shuffle(remain_bullet)
        #狡詐國王效果
        for i in range(self.computer.trick_king):
            if i > len(remain_bullet)-1:
                break
            elif remain_bullet[i]:
                self.computer.set_bullet_pattern(i,'live')
            else:
                self.computer.set_bullet_pattern(i,'blank')
        #琉璃祝福效果
        if self.player.blessing > 0:
            handsaw = self.blessing(remain_bullet,self.first_move,handsaw)

        time.sleep(2)        

        while len(remain_bullet) > 0:
            skip = False
            try_count = 0
            not_blue_print = True
            gun_lock = False
            temp_break = False

            if self.player.hp <= 0:
                time.sleep(2)
                print('**************************************')
                print('你死了')
                time.sleep(2)
                return
            
            time.sleep(1)
            if self.first_move == '玩家':
                print('==========================================')
                print('你的回合')
                print('你的物品欄:',self.player.item)
                print('玩家血量:',self.player.hp,'莉莉斯血量:',self.computer.hp)  
                print('剩餘',live_bullet,'發實彈',blank,'發空包彈')
                print('請選擇要做的事')
                print('1.射向莉莉斯, 2.射向自己, 3.使用物品, 4.顯示莉莉斯的物品欄')
                if self.player.blood_queen > 0 and (handsaw==False):
                    print('腥紅皇后使你獲得手鋸效果')
                    time.sleep(1)
                    handsaw = True
                    self.player.blood_queen -= 1
                if self.player.max_item >= 20:
                    lobby_NPC[0].unlock_achievement('道理我都懂，但是這個背包怎麼這麼大')
                    time.sleep(1)
                while True:
                    try:
                        action = int(input())
                    except ValueError:
                        print('請輸入正確的數字')
                        continue
                    if type(action) != int:
                        print('請輸入正確的數字')
                        continue
                    if action < 1 or action > 4:
                        print('請輸入正確的數字')
                        continue
                    break
            else:
                action = 0
                self.first_move = '玩家'
            
            if action==1:
                if remain_bullet[0] and (self.computer.fog > 0):
                    print('朦朧國王使你射偏了')
                    self.computer.pop_bullet_pattern()
                    self.computer.fog -= 1
                    handsaw = False
                    killer_queen = False
                    live_bullet -= 1
                elif remain_bullet[0] and handsaw and killer_queen:
                    self.computer.hp -= 10
                    print('你使用漆黑皇后射中了莉莉斯,造成十點傷害')
                    if self.computer.blood_queen > 0:
                        print('腥紅皇后使莉莉斯免疫額外傷害')
                        self.computer.hp += 5
                        self.computer.blood_queen -= 1
                    handsaw = False
                    killer_queen = False
                    self.computer.pop_bullet_pattern()
                    live_bullet -= 1
                    if (self.player.hp <= 5) and (self.computer.hp <= 0):
                        time.sleep(2)
                        lobby_NPC[0].unlock_achievement('漆黑子彈')
                elif remain_bullet[0]&killer_queen:
                    self.computer.hp -= 5
                    print('你使用漆黑皇后射中了莉莉斯,造成五點傷害')
                    self.computer.pop_bullet_pattern()
                    live_bullet -= 1
                    killer_queen = False
                    if (self.player.hp <= 5) and (self.computer.hp <= 0):
                        time.sleep(2)
                        lobby_NPC[0].unlock_achievement('漆黑子彈')
                elif remain_bullet[0]&handsaw:
                    self.computer.hp -= 2
                    print('你射中了莉莉斯,造成兩點傷害')
                    if self.computer.blood_queen > 0:
                        print('腥紅皇后使莉莉斯免疫額外傷害')
                        self.computer.hp += 1
                        self.computer.blood_queen -= 1
                    handsaw = False
                    self.computer.pop_bullet_pattern()
                    live_bullet -= 1
                elif remain_bullet[0]:
                    self.computer.hp -= 1
                    print('你射中了莉莉斯,造成一點傷害')
                    self.computer.pop_bullet_pattern()
                    live_bullet -= 1
                else:
                    print('你的子彈打空了')
                    self.computer.pop_bullet_pattern()
                    blank -= 1
                    handsaw = False
                remain_bullet.pop(0)
                handsaw = False
            elif action==2:
                if remain_bullet[0]&handsaw&killer_queen:
                    self.player.hp -= 10
                    print('你用漆黑皇后射中了自己,造成十點傷害')
                    if self.player.blood_queen > 0:
                        print('腥紅皇后使你免疫額外傷害')
                        self.player.hp += 5
                        self.player.blood_queen -= 1
                    else:
                        print('節哀順變')
                    handsaw = False
                    killer_queen = False
                    self.computer.pop_bullet_pattern()
                    live_bullet -= 1
                elif remain_bullet[0]&killer_queen:
                    self.player.hp -= 5
                    print('你用漆黑皇后射中了自己,造成五點傷害')
                    print('節哀順變')
                    killer_queen = False
                    self.computer.pop_bullet_pattern()
                    live_bullet -= 1
                elif remain_bullet[0]&handsaw:
                    self.player.hp -= 2
                    print('你射中了自己,造成兩點傷害')
                    if self.player.blood_queen > 0:
                        print('腥紅皇后使你免疫額外傷害')
                        self.player.hp += 1
                        self.player.blood_queen -= 1
                    else:
                        print('你是笨蛋嗎?')
                        lobby_NPC[0].unlock_achievement('你是笨蛋嗎')
                    handsaw = False
                    self.computer.pop_bullet_pattern()
                    live_bullet -= 1
                elif remain_bullet[0]:
                    self.player.hp -= 1
                    print('你射中了自己,造成一點傷害')
                    self.computer.pop_bullet_pattern()
                    live_bullet -= 1
                    handsaw = False
                else:
                    print('你的子彈打空了,額外獲得一回合')
                    remain_bullet.pop(0)
                    self.computer.pop_bullet_pattern()
                    blank -= 1
                    handsaw = False
                    continue
                remain_bullet.pop(0)
                handsaw = False
            elif action==3:
                print('請選擇要使用的物品')
                for i in range(len(self.player.item)):
                    print(i+1,'.',self.player.item[i])
                try:
                    item = int(input())
                except ValueError:
                    print('請輸入正確的數字')
                    continue

                if item > len(self.player.item):    
                    print('請輸入正確的數字')
                    continue
                if self.player.item[item-1] == '手鋸':
                    if handsaw:
                        print('手鉅效果已經存在了')
                        continue
                    handsaw = True
                    print('你使用了手鋸,下一發子彈造成兩倍傷害')
                elif self.player.item[item-1] == '啤酒':
                    if remain_bullet.pop(0):
                        print('你使用了啤酒,退掉一發實彈')
                        live_bullet -= 1
                    else:
                        print('你使用了啤酒,退掉一發空包彈')
                        blank -= 1
                    self.computer.pop_bullet_pattern()
                    if len(remain_bullet) == 0:
                            print('子彈打完了')
                            print('進入下一局')
                            return
                elif self.player.item[item-1] == '手機':
                    print('你使用了手機')
                    if len(remain_bullet) == 1:
                        n = 0
                    else:
                        n=random.randint(1,len(remain_bullet)-1)
                    if remain_bullet[n]:
                        print('第',n+1,'發是實彈')
                    else:
                        print('第',n+1,'發是空包彈')
                elif self.player.item[item-1] == '轉換器':
                    print('你使用了轉換器,現在這發子彈將反轉')
                    remain_bullet[0] = not remain_bullet[0]
                    if remain_bullet[0]:
                        live_bullet += 1
                        blank -= 1
                    else:
                        live_bullet -= 1
                        blank += 1
                elif self.player.item[item-1] == '過期藥物':
                    print('你使用了過期藥物')
                    if random.randint(0,1):
                        self.player.hp += 2
                        print('你回復了兩點血量')
                    else:
                        self.player.hp -= 1
                        print('你失去了一點血量')
                        if self.player.hp <= 0:
                            time.sleep(2)
                            print('**************************************')
                            print('你死了')
                            time.sleep(2)
                            return
                elif self.player.item[item-1] == '放大鏡':
                    print('你使用了放大鏡看到 ','實彈' if remain_bullet[0] else '空包彈')
                elif self.player.item[item-1] == '香菸':
                    print('你使用了香菸,回復一點血量')
                    self.player.hp += 1
                elif self.player.item[item-1] == '手銬':
                    if self.computer.handcuff:
                        print('莉莉斯已經被銬住了')
                        continue
                    print('你使用了手銬,莉莉斯下回合無法行動')
                    self.computer.dohandcuff()
                elif self.player.item[item-1] == '未知藍圖':
                    if self.player.item.count('過期藥物') >= 3:
                        print('你獲得了禁藥')
                        self.player.item.append('禁藥')
                        for i in range(3):
                            self.player.item.remove('過期藥物')
                        self.player.item.remove('未知藍圖')
                    elif (self.player.item.count('手鋸') >= 2) and  (self.player.item.count('放大鏡') >= 1):
                        print('你獲得了大口徑子彈')
                        self.player.item.append('大口徑子彈')
                        for i in range(2):
                            self.player.item.remove('手鋸')
                        self.player.item.remove('放大鏡')
                        self.player.item.remove('未知藍圖')
                    elif (self.player.item.count('大口徑子彈') >= 1) and (self.player.item.count('腎上腺素') >= 1) and (self.player.item.count('轉換器') >= 1):
                        print('你獲得了榴彈砲')
                        self.player.item.append('榴彈砲')
                        self.player.item.remove('腎上腺素')
                        self.player.item.remove('大口徑子彈')
                        self.player.item.remove('轉換器')
                        self.player.item.remove('未知藍圖')
                    elif (self.player.item.count('啤酒') >= 2) and (self.player.item.count('香菸') >= 1) and ((live_bullet+blank) >= 3):
                        print('你獲得了彈藥包')
                        self.player.item.remove('啤酒')
                        self.player.item.remove('啤酒')
                        self.player.item.remove('香菸')
                        self.player.item.append('彈藥包')
                        self.player.item.remove('未知藍圖')
                    elif len(self.player.item) == self.player.max_item:
                        print('你獲得了擴增背包,物品欄增加2格')
                        self.player.item = []
                        self.player.max_item += 2
                    else:
                        print('你的物品不足以合成')
                        continue
                    not_blue_print = False
                elif self.player.item[item-1] == '禁藥':
                    #70%機率血量翻倍並+3，30%血量降低到1點，若血量為1則死亡
                    print('你使用了禁藥')
                    if random.randint(1,10) <= 7:
                        self.player.hp *= 2
                        self.player.hp += 3
                        print('你的血量大幅提升,現在血量為',self.player.hp)
                    else:
                        if self.player.hp == 1:
                            print('你死了')
                            self.player.hp = 0
                            time.sleep(2)
                            lobby_NPC[0].unlock_achievement('吸毒有礙身心健康，請勿隨意嘗試')
                            time.sleep(2)    
                            return
                        self.player.hp = 1
                        print('你中毒了，血量降為1')
                elif self.player.item[item-1] == '大口徑子彈':
                    #將目前這發直接子彈替換成大口徑子彈並直接發射，造成3點傷害，如果有使用手鋸則造成6點傷害
                    if self.computer.fog > 0:
                        print('朦朧國王使你射偏了')
                        self.computer.fog -= 1
                        handsaw = False
                    elif handsaw:
                        self.computer.hp -= 6
                        print('你發射了大口徑子彈,造成6點傷害')
                    else:
                        self.computer.hp -= 3
                        print('你發射了大口徑子彈,造成3點傷害')
                    if remain_bullet.pop(0):
                        live_bullet -= 1
                    else:
                        blank -= 1
                    self.computer.pop_bullet_pattern()
                    self.player.item.pop(item-1)
                    skip = True
                    handsaw = False
                elif self.player.item[item-1] == '榴彈砲':
                    #將自身血量降低至1點，並發射現在這發子彈，若為實彈則造成(降低的血量+1)點傷害，使用手鋸則造成兩倍傷害，若為空包彈則不造成傷害，使用後輪到莉莉斯的回合
                    damage = self.player.hp
                    self.player.hp = 1
                    if remain_bullet.pop(0):
                        if self.computer.fog > 0:
                            print('朦朧國王使你射偏了')
                            self.computer.fog -= 1
                            handsaw = False
                        elif handsaw:
                            self.computer.hp -= 2*damage
                            print('你發射了榴彈砲,造成',2*damage,'點傷害')
                            handsaw = False
                        else:
                            self.computer.hp -= damage
                            print('你發射了榴彈砲,造成',damage,'點傷害')
                        live_bullet -= 1
                    else:
                        print('你發射了榴彈砲,但是子彈打空了')
                        blank -= 1
                    self.computer.pop_bullet_pattern()
                    self.player.item.pop(item-1)
                    skip = True
                elif self.player.item[item-1] == '彈藥包':
                    #對莉莉斯造成剩餘實彈數量的傷害，之後用實彈和空包彈隨機將彈藥填滿至8發
                    damage = live_bullet
                    if self.computer.fog > 0:
                        if damage > self.computer.fog:
                            damage -= self.computer.fog
                            self.computer.fog = 0
                            if handsaw:
                                damage *= 2
                            self.computer.hp -= damage
                            print('你使用了彈藥包')
                            print('朦朧國王使你射偏了部分子彈,對莉莉斯造成',damage,'點傷害')
                        else:
                            print('你使用了彈藥包，但是朦朧國王使你射偏了所有子彈') 
                            self.computer.fog -= damage
                    else:
                        if handsaw:
                            damage *= 2
                        print('你使用了彈藥包,對莉莉斯造成',damage,'點傷害')
                        self.computer.hp -= damage
                    handsaw = False
                    remain_bullet = []
                    live_bullet = 0
                    blank = 0
                    for i in range(8-len(remain_bullet)):
                        if random.randint(0,1):
                            remain_bullet.append(True)
                            live_bullet += 1
                        else:
                            remain_bullet.append(False)
                            blank += 1
                    random.shuffle(remain_bullet)
                    print('彈藥已重新裝填')
                    self.computer.reset_bullet_pattern(live_bullet+blank)
                    if self.player.blessing > 0:
                        handsaw = self.blessing(remain_bullet,'玩家',handsaw)
                elif self.player.item[item-1] == '漆黑皇后':
                    #移除雙方所有道具，將彈夾裝填為一發空包彈一發實彈，這發實彈將造成5點傷害
                    print('你使用了漆黑皇后，彈藥裝填為一發空包彈一發5點傷害實彈，祈禱吧!')
                    self.player.item = []
                    self.computer.item = []
                    remain_bullet = [True,False]
                    live_bullet = 1
                    blank = 1
                    self.computer.reset_bullet_pattern(live_bullet+blank)
                    random.shuffle(remain_bullet)
                    killer_queen = True
                    not_blue_print = False
                    self.player.queen_used.append('漆黑皇后')
                    if self.player.blessing > 0:
                        handsaw = self.blessing(remain_bullet,'玩家',handsaw)
                elif self.player.item[item-1] == '神聖皇后':
                    #回3點血量，背包上限+2，獲得3個隨機物品
                    print('你使用了神聖皇后，回復3點血量，背包上限+2，獲得3個隨機物品')
                    self.player.hp += 3
                    self.player.max_item += 3
                    self.give_participant_item(3,self.player)
                    self.player.max_item -= 1
                    self.player.queen_used.append('神聖皇后')
                elif self.player.item[item-1] == '蔚藍皇后':
                    #玩家的回合結束時，獲得一個隨機物品
                    print('你使用了蔚藍皇后，輪到莉莉斯的回合時你將獲得一個隨機物品')
                    self.player.item_queen += 1   
                    self.player.queen_used.append('蔚藍皇后')
                    if self.player.item_queen >= 5 :
                        time.sleep(1)
                        lobby_NPC[0].unlock_achievement('道具永動機')
                        time.sleep(1)
                elif self.player.item[item-1] == '腥紅皇后':
                    #玩家的回合開始時，附加手鉅效果
                    print('你使用了腥紅皇后，每回合獲得手鋸效果並免疫手鉅的額外傷害，可以觸發五次')
                    self.player.blood_queen += 5       
                    self.player.queen_used.append('腥紅皇后') 
                elif self.player.item[item-1] == '琉璃皇后':
                    #每次重新裝彈(回合開始、彈藥包、漆黑皇后)時通靈第一顆子彈，若為實彈則附加手鉅效果
                    #若為空包彈則回復一點血量並消除莉莉斯一個道具或獲得一個隨機道具
                    #使用當下清空莉莉斯的道具、清空彈夾並裝上一顆實彈
                    print('你獲得了琉璃的祝福，莉莉斯的道具被清空，彈夾重新裝填了')
                    time.sleep(2)
                    lobby_NPC[0].unlock_achievement('琉璃的祝福')
                    self.computer.item = [] 
                    self.computer.reset_bullet_pattern(1)
                    remain_bullet = [True]
                    if not handsaw:
                        handsaw = True
                        print('你獲得了手鋸效果')
                    time.sleep(1)
                    live_bullet = 1
                    blank = 0
                    self.player.blessing += 1
                    self.player.queen_used.append('琉璃皇后')                          
                elif self.player.item[item-1] == '腎上腺素':
                    print('你使用了腎上腺素,可以偷取莉莉斯的物品')
                    if len(self.computer.item) == 0:
                        print('莉莉斯沒有物品可以偷取')
                        continue
                    print('請選擇要偷取的物品:')
                    for i in range(len(self.computer.item)):
                        print(i+1,'.',self.computer.item[i])
                    try:
                        steal = int(input())
                    except ValueError:
                        print('請輸入正確的數字')
                        time.sleep(1)
                        continue  
                    if steal > len(self.computer.item):
                        print('請輸入正確的數字')
                        continue
                    elif steal <= 0:
                        print('請輸入正確的數字')
                        continue
                    #馬上使用選擇的物品 
                    if self.computer.item[steal-1] == '手鋸':
                        if handsaw:
                            print('手鉅效果已經存在了')
                            continue
                        handsaw = True
                        print('你使用了手鋸,下一發子彈造成兩倍傷害')
                    elif self.computer.item[steal-1] == '啤酒':
                        if remain_bullet.pop(0):
                            print('你使用了啤酒,退掉一發實彈')
                            live_bullet -= 1
                        else:
                            print('你使用了啤酒,退掉一發空包彈')
                            blank -= 1
                        self.computer.pop_bullet_pattern()
                        if len(remain_bullet) == 0:
                            print('子彈打完了')
                            print('進入下一局')
                            return
                    elif self.computer.item[steal-1] == '手機':
                        print('你使用了手機')
                        if len(remain_bullet) == 1:
                            n = 0
                        else:
                            n=random.randint(1,len(remain_bullet)-1)
                        if remain_bullet[n]:
                            print('第',n+1,'發是實彈')
                        else:
                            print('第',n+1,'發是空包彈')
                    elif self.computer.item[steal-1] == '轉換器':
                        print('你使用了轉換器,現在這發子彈將反轉')
                        remain_bullet[0] = not remain_bullet[0]
                        if remain_bullet[0]:
                            live_bullet += 1
                            blank -= 1
                        else:
                            live_bullet -= 1
                            blank += 1
                    elif self.computer.item[steal-1] == '過期藥物':
                        print('你使用了過期藥物')
                        if random.randint(0,1):
                            self.player.hp += 2
                            print('你回復了兩點血量')
                        else:
                            self.player.hp -= 1
                            print('你失去了一點血量')
                            if self.player.hp <= 0:
                                time.sleep(2)
                                print('**************************************')
                                print('你死了')
                                time.sleep(2)
                                return
                    elif self.computer.item[steal-1] == '放大鏡':
                        print('你使用了放大鏡看到 ','實彈' if remain_bullet[0] else '空包彈')
                    elif self.computer.item[steal-1] == '香菸':
                        print('你使用了香菸,回復一點血量')
                        self.player.hp += 1
                    elif self.computer.item[steal-1] == '手銬':
                        if self.computer.handcuff:
                            print('莉莉斯已經被銬住了')
                            continue
                        print('你使用了手銬,莉莉斯下回合無法行動')
                        self.computer.dohandcuff()
                    elif self.computer.item[steal-1] == '未知藍圖':
                        self.player.item.append('未知藍圖')
                        print('你獲得了未知藍圖')
                    elif self.computer.item[steal-1] == '禁藥':
                        print('你使用了禁藥')
                        if random.randint(1,10) <= 7:
                            self.player.hp *= 2
                            self.player.hp += 3
                            print('你的血量大幅提升,現在血量為',self.player.hp)
                        else:
                            if self.player.hp == 1:
                                print('你死了')
                                time.sleep(2)
                                self.player.hp = 0
                                lobby_NPC[0].unlock_achievement('吸毒有礙身心健康，請勿隨意嘗試')
                                time.sleep(2)    
                                return
                            self.player.hp = 1
                            print('你中毒了，血量降為1')
                    elif self.computer.item[steal-1] == '大口徑子彈':
                        if self.computer.fog > 0:
                            print('朦朧國王使你射偏了')
                            self.computer.fog -= 1
                            handsaw = False
                        elif handsaw:
                            self.computer.hp -= 6
                            print('你使用了大口徑子彈,造成6點傷害')
                        else:
                            self.computer.hp -= 3
                            print('你使用了大口徑子彈,造成3點傷害')
                        if remain_bullet.pop(0):
                            live_bullet -= 1
                        else:
                            blank -= 1
                        self.computer.pop_bullet_pattern()
                        handsaw = False
                    elif self.computer.item[steal-1] == '榴彈砲':
                        damage = self.player.hp 
                        self.player.hp = 1
                        if remain_bullet.pop(0):
                            if self.computer.fog > 0:
                                print('朦朧國王使你射偏了')
                                self.computer.fog -= 1
                                handsaw = False
                            elif handsaw:
                                self.computer.hp -= 2*damage
                                print('你使用了榴彈砲,造成',2*damage,'點傷害')
                                handsaw = False
                                if damage >= 15:
                                    lobby_NPC[0].unlock_achievement('巨砲')
                            else:
                                self.computer.hp -= damage
                                print('你使用了榴彈砲,造成',damage,'點傷害')
                                if damage >= 30:
                                    lobby_NPC[0].unlock_achievement('巨砲')
                            live_bullet -= 1
                        else:
                            print('你使用了榴彈砲,但是子彈打空了')
                            blank -= 1
                            handsaw = False
                        self.computer.pop_bullet_pattern()
                    elif self.computer.item[steal-1] == '彈藥包':
                        damage = live_bullet
                        if self.computer.fog > 0:
                            if damage > self.computer.fog:
                                damage -= self.computer.fog
                                self.computer.fog = 0
                                if handsaw:
                                    damage *= 2
                                self.computer.hp -= damage
                                print('你使用了彈藥包')
                                print('朦朧國王使你射偏了部分子彈,對莉莉斯造成',damage,'點傷害')
                            else:
                                print('你使用了彈藥包，但是朦朧國王使你射偏了所有子彈') 
                                self.computer.fog -= damage
                        else:
                            if handsaw:
                                damage *= 2
                            print('你使用了彈藥包,對莉莉斯造成',damage,'點傷害')
                            self.computer.hp -= damage
                        handsaw = False
                        remain_bullet = []
                        live_bullet = 0
                        blank = 0
                        for i in range(8-len(remain_bullet)):
                            if random.randint(0,1):
                                remain_bullet.append(True)
                                live_bullet += 1
                            else:
                                remain_bullet.append(False)
                                blank += 1
                        random.shuffle(remain_bullet)
                        print('彈藥已重新裝填')
                        self.computer.reset_bullet_pattern(live_bullet+blank)
                        if self.player.blessing > 0:
                            handsaw = self.blessing(remain_bullet,'玩家',handsaw)
                        
                    elif self.computer.item[steal-1] == '腎上腺素':
                        print('你不能偷取腎上腺素')
                        time.sleep(2)
                        lobby_NPC[0].unlock_achievement('就說了不行')
                        continue
                    else:
                        print('你不能偷取國王道具')
                        continue
                    self.computer.item.pop(steal-1)

                if not_blue_print and not skip: 
                    self.player.item.pop(item-1)
                time.sleep(2)
                if self.computer.hp <= 0:
                    time.sleep(2)
                    print('**************************************')
                    print('你贏了')
                    time.sleep(2)
                    return
                if not skip:
                    continue
            elif action==4:
                print('莉莉斯的物品欄:',self.computer.item)
                time.sleep(4)
                continue
            if self.computer.hp <= 0:
                time.sleep(2)
                print('**************************************')
                print('你贏了')
                time.sleep(2)
                return
            if self.player.hp <= 0:
                time.sleep(2)
                print('**************************************')
                print('你死了')
                time.sleep(2)
                return
            if len(remain_bullet) == 0:
                print('子彈打完了')
                print('進入下一局')
                return
            if self.player.item_queen > 0:
                print('蔚藍皇后使你獲得隨機物品')
                time.sleep(1)
            for i in range(self.player.item_queen):
                self.give_participant_item(1,self.player)
            print('==========================================')
            print('莉莉斯的回合')
            print('==========================================')
            time.sleep(1)
            try_count = 0
            not_blue_print = True

            if self.computer.handcuff:
                print('莉莉斯被手銬銬住了,無法行動')
                self.computer.unhandcuff()
                continue

            skip = False
            not_blue_print = True

            while True:
                #莉莉斯進行剩餘子彈分析
                if (live_bullet-self.computer.known_live) <= 0:
                    for i in range(len(self.computer.bullet_pattern)):
                        if self.computer.bullet_pattern[i] == 'unknown':
                            self.computer.set_bullet_pattern(i,'blank')
                elif (blank-self.computer.known_blank) <= 0:
                    for i in range(len(self.computer.bullet_pattern)):
                        if self.computer.bullet_pattern[i] == 'unknown':
                            self.computer.set_bullet_pattern(i,'live')
                if self.player.hp <= 0:
                    time.sleep(2)
                    print('**************************************')
                    print('你死了')
                    time.sleep(2)
                    return
                time.sleep(2)
                if len(remain_bullet) == 0:
                    print('子彈打完了')
                    print('進入下一局')
                    return
                if (self.computer.rage_king > 0) and (handsaw == False):
                    print('狂暴國王給予莉莉斯手鉅效果')
                    time.sleep(1)
                    handsaw = True
                    self.computer.rage_king -= 1
                if self.computer.item.count('腥紅皇后') > 0 & (not handsaw):
                    print('腥紅皇后使莉莉斯獲得手鋸效果')
                    time.sleep(1)
                    handsaw = True
                    self.computer.blood_queen -= 1
                #莉莉斯的行動判斷
                if len(self.computer.bullet_pattern) != len(remain_bullet):
                    raise Exception('子彈數量不符')
                if len(self.computer.item) > 2 :
                    if try_count >= 3:
                        action = random.randint(1,2)
                        if self.computer.bullet_pattern[0] == 'live':
                            action = 1
                        elif self.computer.bullet_pattern[0] == 'blank':
                            action = 2
                    elif random.randint(1,4) == 4:
                        action = random.randint(1,2)
                    else:
                        action = 3
                elif ('朦朧國王' in self.computer.item or '狂暴國王' in self.computer.item or '狡詐國王' in self.computer.item or '貪婪國王' in self.computer.item):
                    action = 3
                elif self.computer.bullet_pattern[0] == 'live':
                    action = 1
                elif self.computer.bullet_pattern[0] == 'blank':
                    action = 2
                elif len(self.computer.item) == 0:
                    action = random.randint(1,2)
                else:
                    action = random.randint(1,3)
                if (live_bullet > blank) & (action == 2):
                    action = 1
                if (self.computer.bullet_pattern[0] == 'live') and (action == 2):
                    action = 1
                elif (self.computer.bullet_pattern[0] == 'blank') and (action == 1):
                    action = 2
                
                if (self.computer.bullet_pattern[0] == 'blank') & ('轉換器' in self.computer.item):
                    print('莉莉斯使用了轉換器,現在這發子彈將反轉')
                    remain_bullet[0] = True
                    live_bullet += 1
                    blank -= 1
                    self.computer.bullet_pattern[0] = 'live'
                    self.computer.item.remove('轉換器')
                    time.sleep(2)
                    continue
                if (self.computer.bullet_pattern[0] == 'live') & ('手鋸' in self.computer.item) and not handsaw:  
                    handsaw = True
                    print('莉莉斯使用了手鋸,下一發子彈造成兩倍傷害')
                    time.sleep(2)
                    self.computer.item.remove('手鋸')
                    action = 1
                if '未知藍圖' in self.computer.item:
                    #馬上使用未知藍圖
                    print('莉莉斯使用了未知藍圖')
                    time.sleep(2)
                    temp = random.randint(1,5)
                    if temp == 1:
                        print('莉莉斯獲得了禁藥')
                        
                        self.computer.item.append('禁藥')
                    elif temp == 2:
                        print('莉莉斯獲得了大口徑子彈')
                        
                        self.computer.item.append('大口徑子彈')
                    elif temp == 3:
                        print('莉莉斯獲得了榴彈砲')
                        
                        self.computer.item.append('榴彈砲')
                    elif temp == 4:
                        print('莉莉斯獲得了彈藥包')
                        
                        self.computer.item.append('彈藥包')
                    elif temp == 5:
                        print('莉莉斯獲得了擴增背包')
                        
                        self.computer.max_item += 1
                    self.computer.item.remove('未知藍圖')
                    time.sleep(2)
                    continue
                if gun_lock and action == 2:
                    action = 1
                #莉莉斯的行動選項和玩家相同
                if action==1:
                    try_count = 0
                    if remain_bullet[0]&handsaw&killer_queen:
                        self.player.hp -= 10
                        print('莉莉斯使用漆黑皇后射中了你,造成十點傷害')
                        if self.player.blood_queen > 0:
                            print('腥紅皇后使你免疫額外傷害')
                            self.player.hp += 5
                            self.player.blood_queen -= 1
                        handsaw = False
                        killer_queen = False
                        live_bullet -= 1
                        self.computer.pop_bullet_pattern()
                    elif remain_bullet[0]&killer_queen:
                        self.player.hp -= 5
                        print('莉莉斯使用漆黑皇后射中了你,造成五點傷害')
                        live_bullet -= 1
                        self.computer.pop_bullet_pattern()
                        killer_queen = False
                    elif remain_bullet[0]&handsaw:
                        self.player.hp -= 2
                        print('莉莉斯射中了你,造成兩點傷害')
                        if self.player.blood_queen > 0:
                            print('腥紅皇后使你免疫額外傷害')
                            self.player.hp += 1
                            self.player.blood_queen -= 1
                        handsaw = False
                        live_bullet -= 1
                        self.computer.pop_bullet_pattern()
                    elif remain_bullet[0]:
                        self.player.hp -= 1
                        print('莉莉斯射中了你,造成一點傷害')
                        live_bullet -= 1
                        self.computer.pop_bullet_pattern()
                    else:
                        print('莉莉斯的子彈打空了')
                        blank -= 1
                        self.computer.pop_bullet_pattern()
                        handsaw = False
                    remain_bullet.pop(0)
                    handsaw = False
                elif action==2:
                    try_count = 0
                    if remain_bullet[0] and (self.computer.fog > 0):
                        print('朦朧國王使莉莉斯射偏了')
                        self.computer.fog -= 1
                        handsaw = False
                        killer_queen = False
                        live_bullet -= 1
                        self.computer.pop_bullet_pattern()
                    elif remain_bullet[0]&handsaw&killer_queen:
                        self.computer.hp -= 10
                        print('莉莉斯使用漆黑皇后射中了自己,造成十點傷害')
                        if self.computer.blood_queen > 0:
                            print('腥紅皇后使你免疫額外傷害')
                            self.computer.hp += 5
                            self.computer.blood_queen -= 1
                        else:
                            print('你逃過了一截')
                        handsaw = False
                        killer_queen = False
                        live_bullet -= 1
                        self.computer.pop_bullet_pattern()
                    elif remain_bullet[0]&killer_queen:
                        self.computer.hp -= 5
                        print('莉莉斯使用漆黑皇后射中了自己,造成五點傷害')
                        print('你逃過了一截')
                        live_bullet -= 1
                        self.computer.pop_bullet_pattern()
                        killer_queen = False
                    elif remain_bullet[0]&handsaw:
                        self.computer.hp -= 2
                        print('莉莉斯射中了自己,造成兩點傷害')
                        if self.computer.blood_queen > 0:
                            print('腥紅皇后使莉莉斯免疫額外傷害')
                            self.computer.hp += 1
                            self.computer.blood_queen -= 1
                        handsaw = False
                        live_bullet -= 1
                        self.computer.pop_bullet_pattern()
                    elif remain_bullet[0]:
                        self.computer.hp -= 1
                        print('莉莉斯射中了自己,造成一點傷害')
                        live_bullet -= 1
                        self.computer.pop_bullet_pattern()
                        handsaw = False
                    else:
                        print('莉莉斯射向自己，子彈打空了,額外獲得一回合')
                        remain_bullet.pop(0)
                        self.computer.pop_bullet_pattern()
                        blank -= 1
                        handsaw = False
                        continue
                    remain_bullet.pop(0)
                    handsaw = False
                elif action==3:
                    item = random.randint(0,len(self.computer.item)-1)
                    if (self.computer.item[item] == '啤酒') & (self.computer.bullet_pattern[0]=='live'):
                        try_count +=1
                        continue
                    if (self.computer.item[item] == '手銬') & self.player.handcuff:
                        try_count +=1
                        continue
                    if (self.computer.item[item] == '手機') & (len(remain_bullet) <= 2):
                        try_count +=1
                        continue
                    if (self.computer.item[item] == '手鋸') & handsaw:
                        try_count +=1
                        continue
                    if (self.computer.item[item] == '手鋸') & (self.computer.bullet_pattern[0] == 'blank'):
                        try_count +=1
                        continue
                    if (self.computer.item[item] == '榴彈砲') & (self.computer.bullet_pattern[0] == 'blank'):
                        try_count +=1
                        continue
                    if (self.computer.item[item] == '放大鏡') & (self.computer.bullet_pattern[0] == 'blank'):
                        try_count +=1
                        continue
                    if (self.computer.item[item] == '放大鏡') & (self.computer.bullet_pattern[0] == 'live'):
                        try_count +=1
                        continue
                    if (self.computer.item[item] == '手機') & ('unknown' not in self.computer.bullet_pattern):
                        try_count +=1
                        continue
                    if (self.computer.item[item] == '腎上腺素') & (len(self.player.item) == 0):
                        try_count +=1
                        continue     
                    try_count = 0
                    if self.computer.item[item] == '手鋸':
                        handsaw = True
                        print('莉莉斯使用了手鋸,下一發子彈造成兩倍傷害')
                    elif self.computer.item[item] == '啤酒':
                        if remain_bullet.pop(0):
                            print('莉莉斯使用了啤酒,退掉一發實彈')
                            live_bullet -= 1
                            self.computer.pop_bullet_pattern()
                        else:
                            print('莉莉斯使用了啤酒,退掉一發空包彈')
                            blank -= 1
                            self.computer.pop_bullet_pattern()
                        if len(remain_bullet) == 0:
                            print('子彈打完了')
                            print('進入下一局')
                            return
                    elif self.computer.item[item] == '手機':
                        print('莉莉斯使用了手機')
                        if len(remain_bullet) == 1:
                            n = 0
                        else:
                            n=random.randint(1,len(remain_bullet)-1)
                        if remain_bullet[n]:
                            self.computer.set_bullet_pattern(n,'live')
                        else:
                            self.computer.set_bullet_pattern(n,'blank')
                    elif self.computer.item[item] == '轉換器':
                        print('莉莉斯使用了轉換器,現在這發子彈將反轉')
                        remain_bullet[0] = not remain_bullet[0]
                        if remain_bullet[0]:
                            live_bullet += 1
                            blank -= 1
                        else:
                            live_bullet -= 1
                            blank += 1
                        if self.computer.bullet_pattern[0] == 'live':
                            self.computer.set_bullet_pattern(0,'blank')
                        elif self.computer.bullet_pattern[0] == 'blank':
                            self.computer.set_bullet_pattern(0,'live')
                    elif self.computer.item[item] == '過期藥物':
                        print('莉莉斯使用了過期藥物')
                        self.computer.hp += 2
                        print('莉莉斯回復了兩點血量')
                    elif self.computer.item[item] == '放大鏡':
                        print('莉莉斯使用了放大鏡')
                        self.computer.set_bullet_pattern(0,'live' if remain_bullet[0] else 'blank')
                    elif self.computer.item[item] == '香菸':
                        print('莉莉斯使用了香菸,回復一點血量')
                        self.computer.hp += 1
                    elif self.computer.item[item] == '手銬':
                        print('莉莉斯使用了手銬,你下回合無法行動')
                        self.player.dohandcuff()
                    elif self.computer.item[item] == '朦朧國王':
                        print('莉莉斯使用了***朦朧國王***，每回合額外免疫一次傷害')
                        self.player.queen_used.append('朦朧國王')
                        #fog_king為上限，fog為當前免疫次數
                        self.computer.fog_king += 1
                        self.computer.fog += 1
                    elif self.computer.item[item] == '狂暴國王':
                        print('莉莉斯使用了***狂暴國王***，下5發子彈造成兩倍傷害')
                        self.player_queen_used.append('狂暴國王')   
                        self.computer.rage_king += 5
                    elif self.computer.item[item] == '狡詐國王':
                        print('莉莉斯使用了***狡詐國王***，能夠預知部分未來')
                        self.player.queen_used.append('狡詐國王')
                        self.computer.trick_king += 3
                    elif self.computer.item[item] == '貪婪國王':
                        print('莉莉斯使用了***貪婪國王***，偷走你的道具')
                        self.player.queen_used.append('貪婪國王')
                        #偷走玩家所有非皇后道具，留下皇后道具
                        temp_item = []
                        for i in range(len(self.player.item)):
                            if self.player.item[i] != '漆黑皇后' and self.player.item[i] != '神聖皇后' and self.player.item[i] != '蔚藍皇后' and self.player.item[i] != '腥紅皇后':
                                self.computer.item.append(self.player.item[i])
                            else:
                                temp_item.append(self.player.item[i])
                        self.player.item = temp_item                         
                        self.computer.item.remove('貪婪國王')
                        skip = True
                    elif self.computer.item[item] == '未知藍圖':
                        print('莉莉斯使用了未知藍圖')
                        time.sleep(2)
                        temp = random.randint(1,5)
                        if temp == 1:
                            print('莉莉斯獲得了禁藥')
                            self.computer.item.pop(item)
                            self.computer.item.append('禁藥')
                        elif temp == 2:
                            print('莉莉斯獲得了大口徑子彈')
                            self.computer.item.pop(item)
                            self.computer.item.append('大口徑子彈')
                        elif temp == 3:
                            print('莉莉斯獲得了榴彈砲')
                            self.computer.item.pop(item)
                            self.computer.item.append('榴彈砲')
                        elif temp == 4:
                            print('莉莉斯獲得了彈藥包')
                            self.computer.item.pop(item)
                            self.computer.item.append('彈藥包')
                        elif temp == 5:
                            print('莉莉斯獲得了擴增背包')
                            self.computer.item.pop(item)
                            self.computer.max_item += 1
                    elif self.computer.item[item] == '禁藥':
                        print('莉莉斯使用了禁藥')
                        self.computer.hp *= 2
                        self.computer.hp += 3
                        print('莉莉斯的血量大幅提升,現在血量為',self.computer.hp)
                    elif self.computer.item[item] == '大口徑子彈':
                        self.computer.item.pop(item)
                        if handsaw:
                            self.player.hp -= 6
                            print('莉莉斯使用了大口徑子彈,造成6點傷害')
                        else:
                            self.player.hp -= 3
                            print('莉莉斯使用了大口徑子彈,造成3點傷害')
                        if remain_bullet.pop(0):
                            live_bullet -= 1
                        else:
                            blank -= 1
                        self.computer.pop_bullet_pattern()
                        skip = True
                        handsaw = False
                    elif self.computer.item[item] == '榴彈砲':
                        self.computer.item.pop(item)
                        damage = self.computer.hp 
                        self.computer.hp = 1
                        if remain_bullet.pop(0):
                            if handsaw:
                                self.player.hp -= 2*damage
                                print('莉莉斯使用了榴彈砲,造成',2*damage,'點傷害')
                                handsaw = False
                            else:
                                self.player.hp -= damage
                                print('莉莉斯使用了榴彈砲,造成',damage,'點傷害')
                            live_bullet -= 1
                        else:
                            print('莉莉斯使用了榴彈砲,但是子彈打空了')
                            blank -= 1
                            handsaw = False

                        self.computer.pop_bullet_pattern()
                        skip = True
                    elif self.computer.item[item] == '彈藥包':
                        damage = live_bullet
                        if handsaw:
                            damage *= 2
                            handsaw = False 
                        self.player.hp -= damage
                        print('莉莉斯使用了彈藥包,對你造成',damage,'點傷害')
                        remain_bullet = []
                        live_bullet = 0
                        blank = 0
                        for i in range(8-len(remain_bullet)):
                            if random.randint(0,1):
                                remain_bullet.append(True)
                                live_bullet += 1
                            else:
                                remain_bullet.append(False)
                                blank += 1
                        random.shuffle(remain_bullet)
                        print('彈藥已重新裝填')
                        if self.player.blessing > 0:
                            handsaw = self.blessing(remain_bullet,'莉莉斯',handsaw)
                        self.computer.reset_bullet_pattern(live_bullet+blank)

                    elif self.computer.item[item] == '腎上腺素':    
                        print('莉莉斯使用了腎上腺素,可以偷取你的物品')
                        if len(self.player.item) == 0:
                            print('你沒有物品可以偷取')
                            continue
                        #隨機偷取玩家的一件物品，馬上使用偷取的物品
                        target = random.randint(0,len(self.player.item)-1)
                        steal = self.player.item.pop(target)
                        if steal == '手鋸':
                            handsaw = True
                            print('莉莉斯偷走了手鋸,下一發子彈造成兩倍傷害')
                        elif steal == '啤酒':
                            if remain_bullet.pop(0):
                                print('莉莉斯偷走了啤酒,退掉一發實彈')
                                live_bullet -= 1
                                self.computer.pop_bullet_pattern()
                            else:
                                print('莉莉斯偷走了啤酒,退掉一發空包彈')
                                blank -= 1
                                self.computer.pop_bullet_pattern()
                            if len(remain_bullet) == 0:
                                print('子彈打完了')
                                print('進入下一局')
                                return
                        elif steal == '手機':
                            print('莉莉斯偷走了手機')
                            if len(remain_bullet) == 1:
                                n = 0
                            else:
                                n=random.randint(1,len(remain_bullet)-1)
                            if remain_bullet[n]:
                                self.computer.set_bullet_pattern(n,'live')
                            else:
                                self.computer.set_bullet_pattern(n,'blank')
                        elif steal == '轉換器':
                            print('莉莉斯偷走了轉換器,現在這發子彈將反轉')
                            remain_bullet[0] = not remain_bullet[0]
                            if remain_bullet[0]:
                                live_bullet += 1
                                blank -= 1
                            else:
                                live_bullet -= 1
                                blank += 1
                            if self.computer.bullet_pattern[0] == 'live':
                                self.computer.set_bullet_pattern(0,'blank')
                            elif self.computer.bullet_pattern[0] == 'blank':
                                self.computer.set_bullet_pattern(0,'live')
                        elif steal == '過期藥物':
                            print('莉莉斯偷走了過期藥物')
                            self.computer.hp += 2
                            print('莉莉斯回復了兩點血量')
                        elif steal == '放大鏡':
                            print('莉莉斯偷走了放大鏡')
                            self.computer.set_bullet_pattern(0,'live' if remain_bullet[0] else 'blank')
                        elif steal == '香菸':
                            print('莉莉斯偷走了香菸,回復一點血量')
                            self.computer.hp += 1
                        elif steal == '手銬':
                            print('莉莉斯偷走了手銬,你下回合無法行動')
                            self.player.dohandcuff()
                        elif steal == '漆黑皇后':
                            #效果和玩家使用漆黑皇后相同
                            print('莉莉斯偷走了漆黑皇后，彈藥裝填為一發空包彈一發5點傷害實彈，祈禱吧!')
                            self.computer.item = []
                            self.player.item = []
                            remain_bullet = [True,False]
                            live_bullet = 1
                            blank = 1
                            self.computer.reset_bullet_pattern(live_bullet+blank)
                            random.shuffle(remain_bullet)
                            killer_queen = True
                            not_blue_print = False
                            if self.player.blessing > 0:
                                self.blessing(remain_bullet,'莉莉斯',handsaw)
                        elif steal == '神聖皇后':
                            #效果和玩家使用神聖皇后相同
                            print('莉莉斯偷走了神聖皇后，回復3點血量，背包上限+2，獲得3個隨機物品')
                            self.computer.hp += 3
                            self.computer.max_item += 2
                            self.give_participant_item(3,self.computer)
                        elif steal == '蔚藍皇后':
                            #效果和玩家使用蔚藍皇后相同
                            print('莉莉斯偷走了蔚藍皇后，你獲得回合時莉莉斯將獲得隨機物品')
                            self.computer.item_queen += 1
                        elif steal == '腥紅皇后':
                            #效果和玩家使用腥紅皇后相同
                            print('莉莉斯偷走了腥紅皇后，你獲得回合時莉莉斯將獲得手鋸效果')
                            self.computer.blood_queen += 1
                            
                        elif steal == '未知藍圖':
                            temp = random.randint(1,5)
                            if temp == 1:
                                print('莉莉斯獲得了禁藥')
                                self.computer.item.append('禁藥')
                            elif temp == 2:
                                print('莉莉斯獲得了大口徑子彈')
                                self.computer.item.append('大口徑子彈')
                            elif temp == 3:
                                print('莉莉斯獲得了榴彈砲')
                                self.computer.item.append('榴彈砲')
                            elif temp == 4:
                                print('莉莉斯獲得了彈藥包')
                                self.computer.item.append('彈藥包')
                            elif temp == 5:
                                print('莉莉斯獲得了擴增背包')
                                self.computer.max_item += 1
                        elif steal == '禁藥':
                            print('莉莉斯偷走了禁藥')
                            print('莉莉斯的血量大幅提升,現在血量為',self.computer.hp)
                        elif steal == '大口徑子彈':
                            if handsaw:
                                self.player.hp -= 6
                                print('莉莉斯偷走了大口徑子彈,造成6點傷害')
                            else:
                                self.player.hp -= 3
                                print('莉莉斯偷走了大口徑子彈,造成3點傷害')
                            if remain_bullet.pop(0):
                                live_bullet -= 1
                            else:
                                blank -= 1
                            handsaw = False
                            self.computer.pop_bullet_pattern()
                            if self.player.handcuff:
                                print('你被手銬銬住了,無法行動')
                                self.player.unhandcuff()
                                try_count = 0
                                continue
                            else:
                                break
                        elif steal == '榴彈砲':
                            damage = self.computer.hp 
                            self.computer.hp = 1
                            if remain_bullet.pop(0):
                                if handsaw:
                                    self.player.hp -= 2*damage
                                    print('莉莉斯偷走了榴彈砲,造成',2*damage,'點傷害')
                                    handsaw = False
                                else:
                                    self.player.hp -= damage
                                    print('莉莉斯偷走了榴彈砲,造成',damage,'點傷害')
                                live_bullet -= 1
                            else:
                                print('莉莉斯偷走了榴彈砲,但是子彈打空了')
                                blank -= 1
                                handsaw = False
                            self.computer.pop_bullet_pattern()
                            if self.player.handcuff:
                                print('你被手銬銬住了,無法行動')
                                self.player.unhandcuff()
                                try_count = 0
                                continue
                            else:
                                break
                        elif steal == '彈藥包':
                            damage = live_bullet
                            if handsaw:
                                self.player.hp -= 2*damage
                                handsaw = False
                            self.player.hp -= damage
                            print('莉莉斯偷走了彈藥包,對你造成',damage,'點傷害')
                            remain_bullet = []
                            live_bullet = 0
                            blank = 0
                            for i in range(8-len(remain_bullet)):
                                if random.randint(0,1):
                                    remain_bullet.append(True)
                                    live_bullet += 1
                                else:
                                    remain_bullet.append(False)
                                    blank += 1
                            random.shuffle(remain_bullet)
                            print('彈藥已重新裝填')
                            if self.player.blessing > 0:
                                handsaw = self.blessing(remain_bullet,'莉莉斯',handsaw)
                            self.computer.reset_bullet_pattern(live_bullet+blank)
                        elif steal == '腎上腺素':
                            print('莉莉斯試著偷取腎上腺素但失敗了')
                            self.player.item.append('腎上腺素')
                        elif steal == '琉璃皇后':
                            print('莉莉斯試著偷取琉璃皇后但失敗了')
                            self.player.item.append('琉璃皇后')
                    if skip and not self.player.handcuff:
                        break
                    elif skip and self.player.handcuff:
                        print('你被手銬銬住了,無法行動')
                        self.player.unhandcuff()
                        try_count = 0
                        continue
                    if not_blue_print:
                        self.computer.item.pop(item)
                    continue
                if self.player.hp <= 0:
                    time.sleep(2)
                    print('**************************************')
                    print('你死了')
                    time.sleep(2)
                    return
                if self.computer.hp <= 0:
                    time.sleep(2)
                    print('**************************************')
                    print('你贏了')
                    time.sleep(2)
                    return
                if self.player.handcuff:
                    print('你被手銬銬住了,無法行動')
                    self.player.unhandcuff()
                    try_count = 0
                    continue
                if len(remain_bullet) == 0:
                    print('子彈打完了')
                    print('進入下一局')
                    return
                if self.computer.item_queen > 0:
                    print('蔚藍皇后使莉莉斯獲得隨機物品')
                    time.sleep(1)
                for i in range(self.computer.item_queen):
                    self.give_participant_item(1,self.computer)
                break      

#新手教學
class tutorial_game(challenge_mode):
    def __init__(self,player,computer,hp):
        game.__init__(self,player,computer,hp,1)
    def basic_one_round(self, live_bullet, blank):
        super().one_round_Samael(live_bullet, blank, 0)
    def give_item(self, number):
        for i in range(number):
            if len(self.player.item) < self.player.max_item:                
                item = self.item_list[random.randint(0,len(self.item_list)-1)]
                print('你獲得了',item)
                self.player.item.append(item)
            else:
                print('你的物品欄已滿')
            if len(self.computer.item) < self.computer.max_item:
                self.computer.item.append(self.item_list[random.randint(0,len(self.item_list)-1)])
        self.player.item.sort(key = ['琉璃皇后','漆黑皇后','神聖皇后','蔚藍皇后','腥紅皇后','未知藍圖','禁藥','大口徑子彈','榴彈砲','彈藥包','放大鏡','香菸','手鋸','啤酒','手銬','手機','轉換器','過期藥物','腎上腺素'].index)
        self.computer.item.sort(key = ['朦朧國王','狂暴國王','狡詐國王','貪婪國王','未知藍圖','禁藥','大口徑子彈','榴彈砲','彈藥包','放大鏡','香菸','手鋸','啤酒','手銬','手機','轉換器','過期藥物','腎上腺素'].index)
    
    def item_one_round(self, live_bullet, blank, item_number):
        super().one_round_Lilit(live_bullet, blank, item_number)
        
#存讀檔
def save_game(main_player, lobby_NPC):
    with open('savefile.pkl', 'wb') as f:
        pickle.dump((main_player, lobby_NPC), f)
    print('遊戲已儲存')

def load_game():
    with open('savefile.pkl', 'rb') as f:
        main_player, lobby_NPC = pickle.load(f)
    return main_player, lobby_NPC
#主程式
if __name__ == '__main__':
    if os.path.exists('savefile.pkl'):
        action = input('是否載入存檔? y/n')
        if action == 'y':
            main_player, lobby_NPC = load_game()
            lobby_NPC[1]=(shopkeeper())
        else:
            main_player = player_in_lobby(input('請輸入角色名字:'),0)
            lobby_NPC = []
            lobby_NPC.append(collection_manager())
            lobby_NPC.append(shopkeeper())
            lobby_NPC.append(host())
            #新手教學  
            lobby_NPC[2].tutorial()
    else:
        main_player = player_in_lobby(input('請輸入角色名字:'),0)
        lobby_NPC = []
        lobby_NPC.append(collection_manager())
        lobby_NPC.append(shopkeeper())
        lobby_NPC.append(host())
        #新手教學  
        lobby_NPC[2].tutorial()
    while True:
        risk = 1
        first_move = '玩家'
        money = 0
        in_challenge_mode = False
        if main_player.money >= 10000000:
            lobby_NPC[0].unlock_achievement('第一桶金')
        if main_player.money >= 500000000:
            lobby_NPC[0].unlock_achievement('財富自由')
        if main_player.money >= 999999999999:
            lobby_NPC[0].unlock_achievement('富可敵國')

        #自動存檔
        save_game(main_player, lobby_NPC)

        print('=====================================    BuckShot    =====================================')
        print('你的名字是',main_player.name,'你的金錢是',main_player.money,'你的道具欄位是',main_player.max_item,'你的額外血量是',main_player.extra_hp)
        if len(main_player.unlockable_item) > 0:
            main_player.show_unlockable_item()
        if len(main_player.item) > 0:    
            main_player.show_item()
        print('==========================================================================================')
        action = input('你站在吵雜的賭場中，輸入1進入設定,輸入2造訪商店,輸入3前往圖鑑,按下Enter前往賭桌  ')
        if action == '1':
            main_player.money += int(input('請輸入你的金錢:'))
            continue
        elif action == '2':
            print('你走進了陰暗的店內')
            time.sleep(1)
            lobby_NPC[1].say_normal_dialogue()
            time.sleep(1.5)
            for i in range(len(lobby_NPC[1].shop)):
                lobby_NPC[1].shop[i].show_item(i+1)
            print('8 離開商店')
            action = input(f'你有 {main_player.money} 元，購買商品?')
            if action == '1':
                if main_player.money >= lobby_NPC[1].shop[0].price and lobby_NPC[1].shop[0].check_required_item(main_player):
                    main_player.buy_item('人工心臟',lobby_NPC[1].shop[0].price)
                    lobby_NPC[1].player_buy_item(0)
                    print('你購買了人工心臟，你現在有',main_player.unlockable_item.count('人工心臟'),'次復活機會')
                else:
                    print('你的錢不夠或者連勝數不足')
            elif action == '2':
                if main_player.money >= lobby_NPC[1].shop[1].price and lobby_NPC[1].shop[1].check_required_item(main_player):
                    main_player.max_item += 1
                    main_player.money -= lobby_NPC[1].shop[1].price  
                    lobby_NPC[1].player_buy_item(1) 
                    print('你的道具欄位增加了，現在可以保存',main_player.max_item,'個道具')
                else:
                    print('你的錢不夠或者連勝數不足')
            elif action == '3':
                if main_player.money >= lobby_NPC[1].shop[2].price and lobby_NPC[1].shop[2].check_required_item(main_player): 
                    print('你解鎖了永久隨機皇后') 
                    main_player.buy_item('隨機皇后',lobby_NPC[1].shop[2].price)
                    lobby_NPC[1].player_buy_item(2)
                else:
                    print('你的錢不夠或者連勝數不足')
            elif action == '4':
                if main_player.money >= lobby_NPC[1].shop[3].price and lobby_NPC[1].shop[3].check_required_item(main_player):
                    main_player.extra_hp += 1
                    main_player.money -= lobby_NPC[1].shop[3].price  
                    lobby_NPC[1].player_buy_item(3)
                    print('你的血量增加了，現在有',main_player.extra_hp,'點額外血量')
                    if main_player.extra_hp >= 4:
                        time.sleep(1)
                        lobby_NPC[0].unlock_achievement('滿血') 
                else:
                    print('你的錢不夠或者連勝數不足')
            elif action == '5':
                if main_player.money >= lobby_NPC[1].shop[4].price and lobby_NPC[1].shop[4].check_required_item(main_player):
                    main_player.buy_item('永久藍圖',lobby_NPC[1].shop[4].price)  
                    lobby_NPC[1].player_buy_item(4) 
                    print('你解鎖了永久未知藍圖')
                else:
                    print('你的錢不夠或者連勝數不足')
            elif action == '6':
                if main_player.money >= lobby_NPC[1].shop[5].price and lobby_NPC[1].shop[5].check_required_item(main_player):
                    main_player.buy_item('琉璃皇后',lobby_NPC[1].shop[5].price)
                    lobby_NPC[1].player_buy_item(5)
                    print('你解鎖了琉璃皇后')
                else:
                    print('你的錢不夠或者連勝數不足')
            elif action == '7':
                if main_player.money >= lobby_NPC[1].shop[6].price and lobby_NPC[1].shop[6].check_required_item(main_player):
                    main_player.buy_item('最終試煉',lobby_NPC[1].shop[6].price)
                    lobby_NPC[1].player_buy_item(6)
                    print('你解鎖了最終試煉')
                    lobby_NPC[1].unlock_final_challenge()
                else:
                    print('你的錢不夠或者連勝數不足')
            time.sleep(2)
            continue
        elif action == '3':
            print('你走進閱覽室，這裡的氣氛令你感到舒適，一本圖鑑被放在最顯眼的位置')
            time.sleep(1)
            if '嗜血印記' in main_player.unlockable_item:
                lobby_NPC[0].unlock_mark_item('嗜血印記')
            if '扭曲印記' in main_player.unlockable_item:
                lobby_NPC[0].unlock_mark_item('扭曲印記')
                lobby_NPC[0].unlock_snake_item()
            if '墮天使印記' in main_player.unlockable_item:
                lobby_NPC[0].unlock_mark_item('墮天使印記')
            lobby_NPC[0].say_normal_dialogue()
            time.sleep(1.5)
            lobby_NPC[0].show_list()
            time.sleep(1)
            continue
            
        #下注階段
        while True:
            try:
                money = (int(input('請輸入你的下注金額:')))
                break
            except ValueError:
                print('請輸入正確的數字:')
            
        if money > main_player.money:
            print('你的錢不夠')
            continue
        else:
            main_player.money -= money
        #加注階段
        #risk預設為1，判斷用質數乘法
        #risk % 2 == 0 高風險模式，倍率5倍
        print('高風險模式下，特殊道具可以直接出現，玩家獲得皇后和莊家獲得藍圖的機率翻倍')
        print('每回合有50%機率雙方血量大幅提升，獲勝時獎金5倍，須至少完成5局才有額外倍率')
        risk_input = input('是否下注高風險模式? : 1.是 2.否')
        if risk_input == '1':
            risk *= 2
        #risk % 3 == 0 殺手國王模式，倍率10倍
        print('殺手國王模式下，莊家有機會獲得獨特的"國王"道具，獲勝時獎金10倍，須至少完成5局才有額外倍率') 
        risk_input = input('是否下注殺手國王模式? : 1.是 2.否')
        if risk_input == '1':
            risk *= 3
        #risk % 5 == 0 幽閉皇后模式，倍率7倍
        print('幽閉皇后模式下，玩家無法獲得"皇后"道具，獲勝時獎金7倍，須至少完成5局才有額外倍率')
        risk_input = input('是否下注幽閉皇后模式? : 1.是 2.否')
        if risk_input == '1':
            risk *= 5    
        #risk % 7 == 0 莊家先手模式，倍率50倍
        print('莊家先手模式下，莊家先行動，獲勝時獎金50倍，須至少完成5局才有額外倍率')
        risk_input = input('是否下注莊家先手模式? : 1.是 2.否')
        if risk_input == '1':
            risk *= 7
            first_move = '莊家'
        #試煉模式(暫定)
        in_challenge_mode = bool(int(input('是否進入試煉模式? : 1.是 0.否')))
        round = 0
        player1 = player(5,main_player.item,money)
        if not in_challenge_mode:
            player1.enable_mark('嗜血印記' in main_player.unlockable_item, '扭曲印記' in main_player.unlockable_item, '墮天使印記' in main_player.unlockable_item)
        computer1 = computer(5,[])
        hp=random.randint(2,6)
        win_count = 0
        if not in_challenge_mode:
            games={}
            games[round] = game(player1,computer1,hp,risk)
            games[round].player_bonus(win_count)
        #計算勝場數
        while in_challenge_mode == False:
            live_bullet = random.randint(1,4)
            blank = random.randint(1,4)
            item_number = random.randint(2,5)
            games[round].set_first_move(first_move)
            games[round].one_round(live_bullet,blank,item_number)
            games[round].round += 1
            if player1.hp <= 0:
                if '人工心臟' in main_player.unlockable_item:
                    print('你的人工心臟啟動了，你獲得了一次復活機會')
                    main_player.unlockable_item.remove('人工心臟')
                    time.sleep(1)
                    print('手術花費你50%的財產')
                    main_player.revive()
                    time.sleep(2)
                    lobby_NPC[0].unlock_achievement('恢復呼吸')
                    break
                else:
                    print('你的屍體旁躺著未能帶走的',player1.money+main_player.money,'元')
                    main_player.die()
                    break
            elif computer1.hp <= 0:
                player1.end_snake_mark()
                win_count += 1
                if player1.money == 0:
                    player1.money = random.randint(14000,52459)
                    print('你獲得了',player1.money,'元')
                    time.sleep(2)
                    print('加倍或放棄?')
                    print('1.加倍 2.放棄')
                    action = input()
                    if action == '1':
                        round += 1
                        print('你帶著',player1.money,'元繼續遊戲')
                        computer1 = computer(5,[])
                        hp=random.randint(2,6)
                        games[round] = game(player1,computer1,hp,risk)
                        continue
                    else:
                        print('你帶著',player1.money,'元離開了賭桌')
                        main_player.earn_money(player1.money)
                        main_player.save_item(player1.item)
                        input('按下Enter離開')
                        lobby_NPC[0].unlock_achievement('見好就收')
                        for item in player1.queen_used:
                            lobby_NPC[0].unlock_queen_king_item(item)
                        lobby_NPC[0].unlock_normal_item()
                        lobby_NPC[0].unlock_special_item()
                        time.sleep(2)
                        break
                else:
                    player1.money *= 2
                    print('你獲得了',player1.money,'元')
                    time.sleep(2)
                    print('你連勝了',win_count,'場')
                    print('加倍或放棄?')
                    print('1.加倍 2.放棄')
                    action = input()
                    if action == '1':
                        round += 1
                        print('你帶著',player1.money,'元繼續遊戲')
                        computer1 = computer(5,[])
                        hp=random.randint(2,6)
                        games[round] = game(player1,computer1,hp,risk)
                        games[round].player_bonus(win_count)
                        for i in range(int(round/3)):
                            games[round].computer_bonus(i)
                        continue
                    else:
                        print('你使用了',player1.queen_used.count('漆黑皇后'),'個漆黑皇后，每個獎金倍率為1.7')
                        time.sleep(1)
                        print('你使用了',player1.queen_used.count('腥紅皇后'),'個腥紅皇后，每個獎金倍率為1.5')
                        time.sleep(1)
                        print('你使用了',player1.queen_used.count('蔚藍皇后'),'個蔚藍皇后，每個獎金倍率為1.2')
                        time.sleep(1)
                        print('你使用了',player1.queen_used.count('神聖皇后'),'個神聖皇后，每個獎金倍率為1.1')
                        time.sleep(1)
                        print('原始獎金為',player1.money,'元')
                        n = pow(1.7,player1.queen_used.count('漆黑皇后'))*pow(1.5,player1.queen_used.count('腥紅皇后'))*pow(1.2,player1.queen_used.count('蔚藍皇后'))*pow(1.1,player1.queen_used.count('神聖皇后'))
                        time.sleep(1)
                        print('皇后獎金倍率為',n)
                        if (risk % 2 == 0) and (win_count >= 5):
                            n *= 5
                            time.sleep(1)
                            print('高風險模式下，獎金5倍')
                        if (risk % 3 == 0) and (win_count >= 5):
                            n *= 10
                            time.sleep(1)
                            print('殺手國王模式下，獎金10倍') 
                        if (risk % 5 == 0) and (win_count >= 5):
                            n *= 7
                            time.sleep(1)
                            print('幽閉皇后模式下，獎金7倍')
                        if (risk % 7 == 0) and (win_count >= 5):
                            n *= 50
                            time.sleep(1)
                            print('莊家先手模式下，獎金50倍')
                        time.sleep(1)
                        print('最終倍率為',n)
                        time.sleep(1)
                        print('最終獎金為',int(player1.money*n),'元')
                        time.sleep(1)
                        print('你帶著',int(player1.money*n),'元離開了賭桌')
                        if (win_count >= 5) and ('五連勝標記' not in main_player.unlockable_item):
                            main_player.unlockable_item.append('五連勝標記')
                            print('你獲得了五連勝標記')
                        if (win_count >= 10) and ('十連勝標記' not in main_player.unlockable_item):
                            main_player.unlockable_item.append('十連勝標記')
                            print('你獲得了十連勝標記')
                        if (win_count >= 20) and ('二十連勝標記' not in main_player.unlockable_item):
                            main_player.unlockable_item.append('二十連勝標記')
                            print('你獲得了二十連勝標記')
                        if (win_count >= 50) and ('五十連勝標記' not in main_player.unlockable_item):
                            main_player.unlockable_item.append('五十連勝標記')
                            print('你獲得了五十連勝標記')
                        if (win_count >= 5):
                            print('你連勝了',win_count,'場')
                        input('按下Enter離開')
                        if win_count >= 10:
                            if risk % 2 == 0:
                                lobby_NPC[0].unlock_achievement('風險大師')
                            if risk % 3 == 0:
                                lobby_NPC[0].unlock_achievement('互相傷害呀')
                            if risk % 5 == 0:
                                lobby_NPC[0].unlock_achievement('真實力')
                            if risk % 7 == 0:
                                lobby_NPC[0].unlock_achievement('你才是挑戰者')
                            if risk == 210:
                                lobby_NPC[0].unlock_achievement('賭神')
                        for item in player1.queen_used:
                            lobby_NPC[0].unlock_queen_king_item(item)
                        lobby_NPC[0].unlock_normal_item()
                        lobby_NPC[0].unlock_special_item()
                        time.sleep(2)
                        main_player.earn_money(int(player1.money*n))
                        main_player.save_item(player1.item)
                break
        if in_challenge_mode == True:
            action = input('試煉等級? 1.莉莉斯 2.利維坦 3.薩邁爾')
            challenger = lobby_NPC[int(action)-1]
            round = 1
            win_count = 0
            player1 = player(5,main_player.item,money)
            computer1 = computer(5,[])
            hp=random.randint(2,6)
            challenge_games={}
            if challenger.name == '莉莉斯':
                #幽閉皇后+高風險
                risk = 10
            elif challenger.name == '利維坦':
                #莊家先手+殺手國王
                risk = 21
            elif challenger.name == '薩邁爾':
                risk = 1
            elif challenger.name == '惡魔公主':
                pass
            challenge_games[round] = challenge_mode(player1,computer1,hp,risk,challenger.name)
            challenge_games[round].player_bonus(win_count)
        while in_challenge_mode == True:
            if challenger.name == '莉莉斯':
                max_round = 5
                live_bullet = random.randint(1,4)
                blank = random.randint(1,4)
                item_number = random.randint(2,5)
                challenge_games[round].set_first_move('玩家')
                challenge_games[round].one_round_Lilit(live_bullet,blank,item_number)
                if (player1.hp > 0) and (computer1.hp > 0):
                    if challenge_games[round].computer.handcuff:
                        challenge_games[round].computer.unhandcuff()
                        print('莉莉斯咬碎手銬，恢復行動')
                    else:
                        challenge_games[round].Lilit_life_steal()
                
            elif challenger.name == '利維坦':
                risk = 21
                max_round = 5
                live_bullet = random.randint(1,4)
                blank = random.randint(1,4)
                item_number = random.randint(3,5)
                challenge_games[round].set_first_move('莊家')
                challenge_games[round].one_round_Leviathan(live_bullet,blank,item_number)

            elif challenger.name == '薩邁爾':
                risk = 1
                max_round = 3
                if round == 1:
                    live_bullet = 2
                    blank = 2
                    foresee = 2
                elif round == 2:
                    live_bullet = 4
                    blank = 4
                    foresee = 4
                elif round == 3:
                    live_bullet = 1
                    blank = 1
                    foresee = 0
                item_number = 0
                challenge_games[round].set_first_move('玩家')
                challenge_games[round].one_round_Samael(live_bullet,blank,foresee)
            challenge_games[round].round += 1
            if player1.hp <= 0:
                if '人工心臟' in main_player.unlockable_item:
                    print('你的人工心臟啟動了，你獲得了一次復活機會')
                    main_player.unlockable_item.remove('人工心臟')
                    time.sleep(1)
                    print('手術花費你50%的財產')
                    main_player.revive()
                    time.sleep(1)
                    lobby_NPC[0].unlock_achievement('恢復呼吸')
                    break

                else:
                    print('你的靈魂被',challenger.name,'徵收了，未能帶走的',player1.money+main_player.money,'元被回收了')
                    main_player.die()
                    break
            elif computer1.hp <= 0:
                win_count += 1
                player1.end_snake_mark()
                if win_count < max_round:
                    challenger.challenge_mode_dialogue(win_count,computer1)
                    round += 1
                    challenger_item_list = computer1.item
                    computer1 = computer(5,challenger_item_list)
                    hp=random.randint(2,6)
                    challenge_games[round] = challenge_mode(player1,computer1,hp,risk,challenger.name)
                    challenge_games[round].player_bonus(win_count)
                    continue
                else:
                    challenger.challenge_mode_dialogue(win_count)
                    time.sleep(1)
                    print('你戰勝了',challenger.name,'通過了試煉')
                    challenger.challenge_mode_reward(main_player)
                    input('按下Enter離開')
                    for item in player1.queen_used:
                        lobby_NPC[0].unlock_queen_king_item(item)
                    lobby_NPC[0].unlock_normal_item()
                    lobby_NPC[0].unlock_special_item()
                    time.sleep(2)
                break
        if main_player.die_state:
            print('遊戲結束')
            break
