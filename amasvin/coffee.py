from drink import Drink # 같은 디렉토리에 있을 땐 amasvin.drink 대신 drink만 써야한다.

class Coffee(Drink):
    pass

if __name__ == '__main__':
    커피1 = Coffee('카페모카', 3500)
    커피1.order()
    print(커피1)