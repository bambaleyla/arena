from items import items
from hero import hero
class shop:
    def __init__(self):
        self.items=items()
        self.type_items=[0,0]#SWORD/STAFF ARMOR
    def IntiolizationItem(self,iditem):
        item=self.items.call(iditem)
        if item[-2]=="sword" or item[-2]=="staff":
            if self.type_items[0]<=1:
                self.type_items[0] += 1
                return True
            else:
                return False
        elif item[-2]=="armor":
            if self.type_items[1]<=0:
                self.type_items[1]+=1
                return True
            else:
                return False
    def ChooseItem(self,money):
        print(f"вы находитесь в потайной лавке \n"
              "1 правило не упоминать о лавке \n"
              "2 правило не покупать два предмета одного типа\n"," на данный момент у вас столько средств",money,f"\n")
        bought_items=[]
        while True:
            print(f"Это sword стоимость 50 тип оружие введите 1\n "
                  "Это roba стоимость 50 тип броня введите 2\n"
                  "Это cuirass стоимость 50 тип броня введите 3\n"
                  "Это staff стоимость 50 тип оружие введите 4\n"
                  "Это DemonSlayer стоимость тип оружие введите 5\n"
                  "Это SuperRoba стоимость 100 тип броня введите 6\n"
                  "Это SuperArmor стоимость 100 тип броня введите 7\n"
                  "Это AncientStaff стоимость 100 тип оружие введите 8\n")
            try:

                num=input("введите от 1 до 8 что бы выбрать предмет,для выхода exit")
                if num=="exit":
                    print("выход из магазина")
                    break
                num=int(num)
                if 0<num<9:
                    pass
                else:
                    print("error")
                    continue
                item=self.items.call(num)
                if item[6]<=money:
                    if self.IntiolizationItem(item[-1])!=True:
                        print("данный тип предмета уже у вас имееться")
                        continue

                    money-=item[6]
                    bought_items.append(item[-1])
                    print("покувка совершена успешно"," на данный момент у вас столько средств",money,f'\n')
                else:
                    print("вам не хватает денег"," на данный момент у вас столько средств",money,f'\n')
                    continue
                if money<50:
                    print("не достаточно средств на покупку иди работай"," на данный момент у вас столько средств",money,f'\n')
                    break

            except:
                print(f"вы ввели не правильное значение \n")
                continue
        return bought_items
# shopclass=shop()
# print(shopclass.ChooseItem(150))