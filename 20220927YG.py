class Food:
    def __init__(self, name):
        self.name = name
        self.style = None
        self.money = 0

    def set_style(self, style):
        self.style = style

    def set_money(self, money):
        self.money = money

    def __str__(self):
        return f'{self.name}\t 비용 : {self.money}원\t style : {self.style}\t'


class DeliveryFood(Food):
    def __init__(self, name):
        super().__init__(name)
        self.delivery_money = 0

    def set_delivery_money(self, de_m):
        self.delivery_money = de_m

    def __str__(self):
        return f'{super().__str__()}\t 배달료 : {self.delivery_money}'


치킨 = DeliveryFood('처갓집')
치킨.set_style('튀김')
치킨.set_money(36000)
치킨.set_delivery_money(2500)
print(치킨)


class StreetFood(Food):
    def __init__(self, name):
        super().__init__(name)
        self.shape = None
        self.season = None

    def set_shape(self, shape):
        self.shape = shape

    def set_season(self, season):
        self.season = season

    def __str__(self):
        return f'{super().__str__()}\t 매장 형태 : {self.shape}\t 계절 : {self.season}'


붕어빵 = StreetFood('황금 붕어빵')
붕어빵.set_Style('빵')
붕어빵.set_money(5000)
붕어빵.set_shape('수레')
붕어빵.set_season('겨울')
print(붕어빵)