class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛 생성.".format(self.name))
        print("체력 {0}, 공격력{1}\n".format(self.hp, self.damage))


marine1 = Unit("마린1", 100, 20)
marine2 = Unit("마린2", 50, 10)
tank = Unit("탱크", 150, 50)
