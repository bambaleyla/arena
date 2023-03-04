import random
from items import items


class hero:
    def __init__(self,name,id,agility,strange,intelegence,mana,IdInventory):
        self.items=items()

        self.name=name
        self.hp = None
        self.break_damage=False

        self.magic_damage=None
        self.dmg=None

        self.agility=agility
        self.strange=strange

        self.mana = mana
        self.intelegence=intelegence

        self.magic_resistance=0
        self.armor=0

        self.idinventory=IdInventory
        self.inventory=[]
        self.money=150
        self.type=[]

        self.id=id
    def hp_count(self):
        self.hp=self.strange*40

    def magic_damage_count(self):
        self.magic_damage=(self.intelegence*5)


    def dmg_count(self):
        self.dmg = (self.agility * 6) + (self.strange* 1.2)

    def mana_count(self):
        self.mana=self.mana+(self.intelegence*10)

    def intelegence_count(self):
        self.intelegence=self.intelegence

    def AttackFisCommon(self):
        return self.dmg,"fis"

    def AttackCrit(self):
        return self.dmg*2,"fis"

    def AttackStrong(self):
        att=random.uniform(1, 2)
        return self.dmg*att,"fis"

    def MagicHeal(self):
        if self.mana>=50:
            self.hp+=self.intelegence*5+50
            return 0,"magic"
        else:
            return 0, "magic"
    def MagicBlockAttack(self):
        self.break_damage=True
        return 0,"fis"

    def MagicAttackCommon(self):
        if self.mana>=50:
            return self.magic_damage,"magic"
        else:
            return 0,"magic"

    def MagicAttackStrong(self):
        if self.mana>=100:
            return self.magic_damage*2.5,"magic"
        else:
            return 0,"magic"
    def InventoryUpdate(self):
        if type(self.idinventory)==int:
            self.idinventory=[self.idinventory]
        elif type(self.idinventory) == str:
            self.idinventory=[]
        for elm in self.idinventory:
            if self.items.call(elm)!=None:
                self.inventory.append(self.items.call(elm))
        for i in self.inventory:
            self.dmg+=i[0]
            self.magic_damage+=i[1]
            self.armor+=i[2]
            self.magic_resistance+=i[3]
            self.hp+=i[4]
            self.mana+=i[5]
            self.type.append(i[8])
    def WinMoney(self,mone):
        self.money+=mone


    def Initiolization(self):
        self.hp_count()
        self.intelegence_count()
        self.mana_count()
        self.magic_damage_count()
        self.dmg_count()
        self.InventoryUpdate()

    def Info(self):
        print(
            f"hp={self.hp} mana={self.mana} strange={self.strange} agility={self.agility} intelegence={self.intelegence}"
            f"dmg={self.dmg} magicDMG={self.magic_damage} armor={self.armor} magic_resistance={self.magic_resistance}")

    def ShortInfo(self,dmg):
        print(f"hp={self.hp} mana={self.mana} name={self.name} dmg that you got={self.GetDmg(dmg)}")

    def GetDmg(self,dmg):
        if self.break_damage==False:
            if dmg[1]=="magic":
                res=dmg[0]-((self.magic_resistance/100)*dmg[0])
                self.hp = self.hp - res
                if self.hp < 0:
                    self.hp = 0


            elif dmg[1]=="fis":
                res = dmg[0] - ((self.armor / 100) * dmg[0])
                self.hp = self.hp - res
                if self.hp < 0:
                    self.hp = 0
        else:
            self.break_damage=False
    def ChooseSkill(self):
        res=0
        while True:
            if self.hp <= 100 and self.mana >= 50:
                res = self.MagicHeal()
                break
            num=input(f"Выберите скилл если AttackFisCommon то введите 1 \n"
                      "если AttackCrit то введите 2 \n"
                      "если AttackStrong то введите 3 \n"
                      "если MagicBlockAttack стоимость 50 маны то введите 4 \n"
                      "если MagicAttackCommon стоимость 50 маны то введите 5 \n"
                      "если MagicAttackStrong стоимость 100 маны то введите 6 \n"
                      f"ваша текущаю мана {self.mana}")
            num=int(num)
            if 0<num<7:
                if num==1:
                    res = self.AttackFisCommon()
                    break
                elif num==2:
                    res = self.AttackCrit()
                    break
                elif num==3:
                    res = self.AttackStrong()
                    break
                elif num==4 and self.mana>=50:
                    res = self.MagicBlockAttack()
                    break
                elif num==5 and self.mana>=50:
                    res = self.MagicAttackCommon()
                    break
                elif num==6 and self.mana>=100:
                    res = self.MagicAttackStrong()
                    break

            else:
                print("вы ввели недопустимое значение")
        return res




# obj=hero("shadow fiend",1,5,5,20,50,[8,5])
# obj.Initiolization()
# obj.Info()


