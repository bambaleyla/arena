class items:
    def __init__(self):#dmg magigDmg armor resitanceMagic hp mana cost name type id
        self.sword=[50,0,0,0,0,0,50,'sword','sword',1]
        self.roba=[0,15,5,30,0,50,50,'roba','armor',2]
        self.cuirass=[0,0,35,5,50,0,50,'cuirass','armor',3]
        self.staff=[10,50,0,0,0,50,50,'staff','staff',4]
        self.DemonSlayer=[100,0,0,0,0,0,100,'DemonSlayer','sword',5]
        self.SuperRoba=[0,30,10,50,0,75,100,'SuperRoba','armor',6]
        self.SuperArmor=[0,0,55,10,75,0,100,'SuperArmor','armor',7]
        self.AncientStaff=[20,75,0,10,0,75,100,'AncientStaff','staff',8]
    def call(self,id):
        if id==1:
            return self.sword
        elif id==2:
            return self.roba
        elif id==3:
            return self.cuirass
        elif id==4:
            return self.staff
        elif id == 5:
            return self.DemonSlayer
        elif id == 6:
            return self.SuperRoba
        elif id == 7:
            return self.SuperArmor
        elif id == 8:
            return self.AncientStaff