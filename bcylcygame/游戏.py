import random
import time
from colorama import Fore,Back,init
init(autoreset=True)
from 技能 import*
print(Fore.BLUE+'欢迎来挑战魔王,你需要选择其中一种难度')
#大厅
while True:
    print('简单(1)\n你的血量:500\n魔王的血量:10000\n普通(2)\n你的血量:250\n魔王的血量:25000\n困难(3)\n你的血量:200\n魔王的血量:30000')
    put_level = input()
    if put_level == '1':
        from 血量与金币easy import*
        break 
    if put_level =='2':
        from 血量与金币 import*
        break
    if put_level =='3':
        from 血量与金币hard import*
        break
    else:
        print(Fore.RED+'你必需选择其中一种难度!')
        continue
#剧情
print (Back.WHITE+Fore.BLACK+'恶魔之城?黑气笼罩,似乎是个不吉之地......\n魔王奴役着人民,他们需要你!\n别害怕,坤坤会用唱跳Rap和篮球助你一臂之力!\n出发吧,圣骑士,一定要活着回来!/开始(Enter)' ) 
# 游戏循环
while True:        
    # 金币随机增加        
    coin += random.randint(coin_scopes[0], coin_scopes[1])
    # 减少道具冷却   
    if basketball_time > 0:
        basketball_time -= 1
    else:
        basketball_time = 0 
    if ctr_time > 0 :
        ctr_time -= 1
    else:
        ctr_time = 0 
    if CD_short_time > 0:
        CD_short_time -= 1
    else:
        CD_short_time = 0 
    if hp_back_time > 0:
        hp_back_time -= 1
    else:
        hp_back_time = 0    
    # 随机暴击    
    king = random.randint(1, int(1/attack_rate))  
    # 攻击
    put = input()
    if put == '':
        if king == 1:
            king_hp -= 2*attack 
        else:
            king_hp -= attack
    # 控制 
    if king == 1 and put == '':        
        print('暴击!') 
    if put == '':   
        print('魔王血量还有' + str(king_hp),',你的血量还有'+ str(you_hp),',金币剩余' + str(coin), '/攻击(Enter)/进入商店(B)/使用道具(I)/尝逝逃跑(X)')    
    #被伤害
    if king_hp <= 1250 and put == '':   
        #随机扣血   
        you = random.randint(1, int(1/hurt_rate))  
        if you == 1:
            you_hp -= hurt    
    # 商店
    elif put == 'B' or put == 'b':
        while True:
            print(Fore.BLUE+'商店,金币剩余' + str(coin))
            print(basketball, '/购买(1)')
            print(ctr,'/购买(2)')
            print(hp_back,'/购买(3)')
            print(CD_short,'/无需购买')
            print('\n选择你要购买的商品吧/离开商店(X)')
            put_shop = input()
            # 篮球
            if put_shop == '1':
                if basketball_state == 0:
                    if coin >= 1000:
                        coin -= 1000
                        basketball_state += 1
                        basketball_time = 0
                        print(Fore.YELLOW+'购买成功')
                    else:
                        print(Fore.RED+'你是想白嫖吗?')
                else:
                    print(Fore.RED+'做人不要太贪心')
            #唱跳RAP
            if put_shop == '2':
                if ctr_state == 0:
                    if coin >= 1500:
                        coin -= 1500
                        ctr_state += 1
                        ctr_time = 0
                        print(Fore.YELLOW+'购买成功')
                    else:
                        print(Fore.RED+'你是想白嫖吗?')
                else:
                    print(Fore.RED+'做人不要太贪心')
            #生命恢复药水
            if put_shop == '3':
                if hp_back_state == 0:
                    if coin >= 1250:
                        coin -= 1250
                        hp_back_state += 1
                        hp_back_time = 0
                        print(Fore.YELLOW+'购买成功')
                    else:
                        print(Fore.RED+'你是想白嫖吗?')
                else:
                    print(Fore.RED+'做人不要太贪心')   
            elif put_shop == 'X' or put_shop == 'x':
                print('离开商店')
                break
    #技能
    elif put == 'I' or put == 'i':
        while True:
            if basketball_state == 0 and ctr_state == 0 and hp_back_state == 0:
                print(Fore.RED+'你是想白嫖吗?你还没有买技能呢/退出(X)')
            if basketball_state == 1 or ctr_state == 1 or hp_back_state == 1:
                print(Fore.BLUE+'技能,金币剩余' + str(coin))
                print(basketball, '冷却剩余(' + str(basketball_time), ')/发动(1)')
                print(ctr,'冷却剩余(' + str(ctr_time), ')/发动(2)')
                print(hp_back,'冷却剩余(' + str(hp_back_time), ')/发动(3)') 
                print(CD_short,'冷却剩余(' + str(CD_short_time), ')/发动(4)') 
                print('\n选择你要使用的道具吧/取消使用(X)')
            put_pro = input()
            # 篮球
            if put_pro == '1':
                if basketball_state == 0:
                    print(Fore.RED+'你还没买篮球呢!')
                if basketball_time == 0 and basketball_state == 1: 
                    print(Fore.GREEN+str(king_hp) + '-10')
                    king_hp -= 10
                    print(Fore.GREEN+str(king_hp) + '-10')
                    king_hp -= 10
                    print(Fore.GREEN+str(king_hp) + '-10')
                    king_hp -= 10
                    print(Fore.GREEN+str(king_hp) + '-10')
                    king_hp -= 10
                    print(Fore.GREEN+str(king_hp) + '-10')
                    king_hp -= 10
                    basketball_time = 5
                else:
                    print(Fore.YELLOW+'还没冷却完成,再等等吧')
            elif put_pro == 'X' or put_pro == 'x':
                print('取消使用')
                break
            #唱跳RAP
            if put_pro == '2':
                if ctr_state == 0:
                    print(Fore.RED+'你还没买唱跳Rap呢!')   
                if ctr_time == 0 and ctr_state == 1:
                    print(Fore.GREEN+str(king_hp) + '-5')
                    king_hp -= 5
                    print(Fore.GREEN+str(king_hp) + '-10')
                    king_hp -= 10
                    print(Fore.GREEN+str(king_hp) + '-15')
                    king_hp -= 15
                    print(Fore.GREEN+str(king_hp) + '-20')
                    king_hp -= 20
                    print(Fore.GREEN+str(king_hp) + '-25')
                    king_hp -= 25
                    print(Fore.GREEN+str(king_hp) + '-30')
                    king_hp -= 30
                    ctr_time = 15
                else:
                    print(Fore.YELLOW+'还没冷却完成,再等等吧')
            elif put_pro == 'X' or put_pro == 'x':
                print('取消使用')
                break    
            #生命恢复药水
            if put_pro == '3':
                if king_hp <= 1250:
                    if hp_back_state == 0:
                        print(Fore.RED+'你还没买生命恢复药水呢!')   
                    if hp_back_time == 0 and hp_back_state == 1:
                        you_hp += 25
                        print(Fore.YELLOW+'回血成功!')
                        hp_back_time = 25
                    else:
                        print(Fore.YELLOW+'还没冷却完成,再等等吧')
                else:
                    print(Fore.RED+'魔王还没攻击你,别想提前使用药水')
            elif put_pro == 'X' or put_pro == 'x':
                print('取消使用')
                break
            #减冷却 
            if put_pro == '4':
                if ctr_state == 1:  
                    if CD_short_time == 0:
                        if ctr_time == 15:  
                            if coin >= 50:
                                coin -= 50 
                                ctr_time -= 15
                                CD_short_time = 50
                                print(Fore.YELLOW+'减冷却成功!')
                            else:
                                print(Fore.RED+'你是想白嫖吗?')           
                        else:
                            print(Fore.RED+'好人做到底,唱跳RAp的冷却点数不足15,下次再逝吧')    
                    else:
                        print(Fore.YELLOW+'还没冷却完成,再等等吧') 
                else:
                    print(Fore.RED+'你还没买唱跳RAP呢!')                                                
            elif put_pro == 'X' or put_pro == 'x':
                print('取消使用')
                break          
    # 逃跑 
    if put == 'X' or put == 'x':
        print(Back.RED+'胆小鬼,你逃离了恶魔之城,你连攻击都不会吗?真的太逊了!')  
        break
    #同归于尽
    if king_hp <= 0 and you_hp <= 0:
        print(Fore.RED+'你和魔王同归于尽了')
        print('再来一局吧')
        break
    else: 
        # 战胜
        if king_hp <= 0:   
            print(Fore.YELLOW+'英雄,你战胜了魔王!!!')
            break
        #你死了
        if you_hp <= 0: 
            print(Fore.RED+'你死了')            
            break
#特别鸣谢
print('\n代码早期制作:bcy\n代码维护:lcy\n场外援助:zmt\n感谢以上所有参与制作的人')
time.sleep(5) 