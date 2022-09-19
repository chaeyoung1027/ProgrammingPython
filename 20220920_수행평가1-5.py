#사용한 시간을 인자로 받아 PC방 요금을 리턴하는 fare_pc 함수
'''
10분당 1000원
1분 초과 해도 1000원 추가
'''
def fare_pc(minuates):
    #minuates을 10으로 나누자. 몫
    share = minuates//10
    #몫*1000 = 요금
    fare = share* 10000
    #minuate을 10으로 나눈 나머지가 있으면 +1000
    if minuates%10!=0:
        fare+=1000
    return fare

fare_pc(60)
fare_pc(10)
fare_pc(102)