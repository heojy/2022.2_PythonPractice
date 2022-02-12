class champion:
    def __init__(self, name, hp, ad):
        self.name = name
        self.hp = int(hp)
        self.ad = int(ad) 
        print("{0} 생성.".format(self.name))


    def level_up():
        pass

def vs(cham1, cham2):
    while ((cham1.hp <= 0) or (cham2.hp<=0)):
        cham1.hp -= cham2.ad
        cham2.hp -= cham1.ad
    if (cham1.hp <= 0) :
        print("{0}의 승리 !".format(cham2.name))
    elif (cham2.hp <= 0) : 
        print("{0}의 승리 !".format(cham1.name))
    else:
        print("error")


트린다미어 = champion("트린다미어", 625, 72)
소나 = champion("소나", 482, 45)
vs(소나, 트린다미어)
#print(type(트린다미어.hp))
#print(트린다미어.hp)

