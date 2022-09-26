class food:
    def __init__(self, name):
        self.name = name
        self.style = None
        self.money = 0
    def setStyle(self, style):
        self.style = style
    def setMoney(self, money):
        self.money = money
    def __str__(self):
        return f'{self.name}\t 비용 : {self.money}\t style : {self.style}\t'



class delivery(food):
    def __init__(self, name):
        super().__init__(name)
        self.de_m = 0
    def setDe_m(self, de_m):
        self.de_m = de_m
    def __str__(self):
        return f'{super().__str__()}\t 배달료 : {self.de_m}'

치킨 = delivery('처갓집')
치킨.setStyle('튀김')
치킨.setMoney(36000)
치킨.setDe_m(2500)
print(치킨.__str__())

class street(food):
    def __init__(self, name):
        super().__init__(name)
        self.shape = None
        self.Season = None

    def setShape(self, shape):
        self.shape = shape

    def setSeason(self,Season):
        self.Season = Season

    def __str__(self):
        return f'{super().__str__()}\t 매장 형태 : {self.shape}\t 계절 : {self.Season}'

붕어빵 = street('황금 붕어빵')
붕어빵.setStyle('빵')
붕어빵.setMoney(5000)
붕어빵.setShape('수레')
붕어빵.setSeason('겨울')
print(붕어빵.__str__())