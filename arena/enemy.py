import random
from items import items

class enemy:
    def __init__(self,name,money,id,agility,strange,intelegence,mana,IdInventory):
        self.items=items()

        self.name=name
        self.hp = None

        self.magic_damage=None
        self.dmg=None
        self.break_damage = False

        self.agility=agility
        self.strange=strange

        self.mana = mana
        self.intelegence=intelegence

        self.magic_resistance=0
        self.armor=0

        self.idinventory=IdInventory
        self.inventory=[]
        self.money=money


        self.id=id
    def hp_count(self):
        self.hp=self.strange*40

    def magic_damage_count(self):
        self.magic_damage=(self.intelegence*6)


    def dmg_count(self):
        self.dmg = (self.agility * 6) + (self.strange* 1.2)

    def mana_count(self):
        self.mana=self.mana+(self.intelegence*10)

    def intelegence_count(self):
        self.intelegence=self.intelegence

    def AttackFisCommon(self):
        return self.dmg,"fis"

    def AttackCrit(self):
        att = random.uniform(1, 2)
        return self.dmg * att, "fis"

    def AttackStrong(self):
        return self.dmg*1.5,"fis"

    def MagicHeal(self):
        if self.mana>=50:
            self.mana -= 50
            self.hp+=self.intelegence*5+50
            return 0,"magic"
        else:
            return 0,"magic"
    def MagicBlockAttack(self):
        self.break_damage = True
        self.mana -= 50
        return 0, "fis"

    def MagicAttackCommon(self):
        if self.mana>=50:
            self.mana -= 50
            return self.magic_damage,"magic"
        else:
            return 0,"magic"

    def MagicAttackStrong(self):
        if self.mana>=100:
            self.mana-=100
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

    def ReturnMoney(self):
        return self.money

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
        print(f"hp={self.hp} mana={self.mana} name={self.name} dmg that he got={self.GetDmg(dmg)}")
    def GetDmg(self,dmg):
        if self.break_damage == False:
            if dmg[1] == "magic":
                res = dmg[0] - ((self.magic_resistance / 100) * dmg[0])
                self.hp = self.hp - res
                if self.hp < 0:
                    self.hp = 0


            elif dmg[1] == "fis":
                res = dmg[0] - ((self.armor / 100) * dmg[0])
                self.hp = self.hp - res
                if self.hp < 0:
                    self.hp = 0
        else:
            self.break_damage=False





    def II(self):
        DmgPercent=self.dmg*100/(self.dmg+self.magic_damage)
        MagicDmgPercent=self.magic_damage*100/(self.dmg+self.magic_damage)
        res=0
        while True:
            randomaise=random.randint(1,100)
            if DmgPercent>=75:
                if self.hp<=100 and self.mana>=50:
                    res=self.MagicHeal()
                    break
                elif randomaise<=28:
                    res=self.AttackFisCommon()
                    break
                elif 29<=randomaise<=56:
                    res=self.AttackStrong()
                    break
                elif 57<=randomaise<70:
                    res=self.AttackCrit()
                    break
                elif 70<=randomaise<83 and self.mana>=50:
                    res=self.MagicAttackCommon()
                    break
                elif 83<=randomaise<96 and self.mana>=50:
                    res=self.MagicBlockAttack()
                    break
                elif 96<=randomaise<=100 and self.mana>=100:
                    res = self.MagicAttackStrong()
                    break



            elif MagicDmgPercent>=75:
                if self.hp<=100 and self.mana>=50:
                    res=self.MagicHeal()
                    break
                elif randomaise<=28 and self.mana>=50:
                    res=self.MagicAttackCommon()
                    break
                elif 29<=randomaise<=56 and self.mana>=100:
                    res=self.MagicAttackStrong()
                    break
                elif 57<=randomaise<70 and self.mana>=50:
                    res=self.MagicBlockAttack()
                    break
                elif 70<=randomaise<83:
                    res=self.AttackFisCommon()
                    break
                elif 83<=randomaise<96:
                    res=self.AttackStrong()
                    break
                elif 96<=randomaise<=100:
                    res = self.AttackCrit()
                    break

            else:
                if self.hp<=100 and self.mana>=50:
                    res=self.MagicHeal()
                    break
                elif randomaise<=18 and self.mana>=50:
                    res=self.MagicAttackCommon()
                    break
                elif 19<=randomaise<=37 and self.mana>=50:
                    res=self.MagicBlockAttack()
                    break
                elif 38<=randomaise<=56:
                    res=self.AttackFisCommon()
                    break
                elif 57<=randomaise<=75:
                    res=self.AttackStrong()
                    break
                elif 76<=randomaise<=88:
                    res = self.AttackCrit()
                    break
                elif 89<=randomaise<=100 and self.mana>=100:
                    res=self.MagicAttackStrong()
                    break
        return res

# obj=enemy("shadow fiend",100,1,5,5,20,50,[8,5])
# obj.Initiolization()
# obj.Info()


