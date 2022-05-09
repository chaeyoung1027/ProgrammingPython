empty_list = []
player = ['Faker', 10, True]    #문자, 숫자, 불리안
print(len(empty_list))  #0
print(len(player))      #3
print(type(empty_list), type(player))
empty_list2 = list()
print(len(empty_list2)) #0
message = list('miracle')
print(message)  #['m', 'i', 'r', 'a', 'c', 'l', 'e']
# numbers = list(56)
# print(numbers)  #TypeError: 'int' object is not iterable
print(player)
#list추가
player = player + [10,11]   #리스트 풀려서 하나씩 추가
print(player)
player.append([20,21])  #리스트 한 덩어리 통째로 추가. list안에 list
print(player)
player.append(56)   #**
print(player)
player.insert(2, 'SKT T-1') #index, 값   원하는 공간에 넣기
print(player)
player.extend([30,31])  # +=과 같은 의미 풀려서 하나씩 추가
print(player)
#append : 리스트 통째로 추가
#+=, extend : 리스트 풀어서 하나씩 추가
#insert : index에 값 추가 / 원하는 위치에
print(player)
player.append(40)
print(player)
#맨 끝에 50 추가 insert()
#player.insert(11,50)
#player.insert(-1,50)   #실패, 맨마지막 두번째에 추가, 마지막 거가 마지막으로 가게 된다.
player.insert(len(player), 50)
print(player)
#수정
print(player[0:4])
print(player[0:])
player[0] = '스티치'
print(player[0])
print(player)
print(player[6])
player[6] = 16
#player[6][0] = 22
print(player)
player[6] = 16
print(player)
#삭제
del player[2]   #인덱싱으로 지우기
print(player)
player.remove(30)   #값으로 지우기
print(player)
player.pop()    #맨 뒤에서 지우기
print(player)
player.pop(2)   #인덱스로 지우기
print(player)
# player.clear()  #리스트 초기화
# print(player)
#remove() : 값으로 지우기
#pop(index), del 리스트명[index] : 인덱스로 지우기
#pop() : 맨 뒤에서 지우기
print(100 in player)    #false
print(10 in player)     #True
print('아이유' in player)#false
print(player)
player[0] = 1
print(player)
player.sort()   #정렬
print(player)
player.reverse()    #뒤집기(내림차순 정렬 x)
print(player)
#/********range() : 범위
a = range(14)
print(a)
a2 = list(a)
print(a2)
print(list(range(14)))
b = range(1, 14+1)    #시작번호를 알려줌
print(list(b))
c = range(1, 14+2, 2)
print(c)
#range(stop) : range(0, stop) : 0, 1, 2, ..., stop-1
#range(star, stop) : start, start+1, start+2, ..., stop-1
#range(star, stop, step) : start, start+step, star+step+step, ..., stop-1
반1 = list(range(1, 14+1))
반2 = list(range(1, 14+1))
반3 = list(range(1, 14+1))
반3.remove(6)
반3.remove(10)
print(반3)
#두자리 숫자 중 홀수인 숫자 리스트 출력하기
두자리 = list(range(11, 100, 2))
print(두자리)
#한자리 숫자 중 짝수인 숫자 출력
print(list(range(8, 0, -2)))


