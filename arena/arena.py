from enemy import enemy
from hero import hero
from shop import shop
from items import items


def presets():#name,money,id,agility,strange,intelegence,mana,IdInventory
    preset_num = int(input("ведите 1 если хотите сражаться с shadow fiend ведите 2 если хотите сражаться с evil god ведите 3 если хотите сражаться с Chase"))
    if preset_num==1:
        return "shadow fiend",150,1,5,10,5,150,[8,5]
    if preset_num==2:
        return "evil god",250,2,15,10,10,150,[3,5]
    if preset_num==3:
        return "Chase",100,3,5,5,10,250,[2,8]
def stats():
    points=20
    agility=0
    strange=0
    intelegence=0
    print(f"Введите характеристики героя у вас {points} очков,а так же дайте ему имя")
    name = input("введите имя героя")
    while True:
        try:
            current_a=int(input(f"введите колличество очков в ловкость на данный момент {points}"))
            if current_a<=points:
                agility=current_a
                points-=current_a
            else:
                print("вы ввели недопустимое значение")
                continue
            current_s=int(input(f"введите колличество очков в сила на данный момент {points}"))
            if current_s<=points:
                strange=current_s
                points-=current_s
            else:
                print("вы ввели недопустимое значение")
                continue
            current_i=int(input(f"введите колличество очков в интелект на данный момент {points} \n"))
            if current_i <= points:
                intelegence = current_i
                points -= current_i

                break
            else:
                print("вы ввели недопустимое значение \n")
                continue
        except:
            agility=0
            intelegence=0
            strange=0
            points=20

    return name,100,agility,strange,intelegence,150

class arena:
    def __init__(self):
        self.shop=shop()
        stat=list(stats())
        stat+=[self.shop.ChooseItem(stat[-1])]
        self.character_one=hero(stat[0],stat[1],stat[2],stat[3],stat[4],stat[5],stat[6])
        preset = list(presets())
        self.character_two=enemy(preset[0],preset[1],preset[2],preset[3],preset[4],preset[5],preset[6],preset[7])
        self.items=items()
        self.character_one.Initiolization()
        self.character_two.Initiolization()
        self.character_one.Info()
        self.character_two.Info()
    def TeamFight(self):
        while True:
            self.character_one.ShortInfo(self.character_one.GetDmg(self.character_two.II()))
            self.character_two.ShortInfo(self.character_two.GetDmg(self.character_one.ChooseSkill()))
            if self.character_one.hp>0 and self.character_two.hp>0:
                self.character_two.GetDmg(self.character_one.ChooseSkill())
                if self.character_two.hp>0:
                    self.character_one.GetDmg(self.character_two.II())

                else:
                    print(f"победил {self.character_one.name} вы получили {self.character_two.money} монет")
                    self.character_one.WinMoney(self.character_two.money)
                    break
            elif self.character_two.hp>0 and self.character_one.hp<=0:
                print(f"победил {self.character_two.name}")
                break
            elif self.character_one.hp>0 and self.character_two.hp<=0:
                print(f"победил {self.character_one.name} вы получили {self.character_two.money} монет")
                self.character_one.WinMoney(self.character_two.money)
                break
            elif self.character_one.hp<=0 and self.character_two.hp<=0:
                print(f"победила дружба вы получили ноль монет")
                break


obj=arena()
obj.TeamFight()
