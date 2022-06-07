#문자열
for ch in "SORI":
    print(ch, end = '*')    #end = ' ' 는 뒤에 공백을 붙여라. 기본 : end = '\n'가 생략되어있다.
print()
#리스트
for item in ["힙합", "발라드"]:
    print(item)
#튜플
for item in(12, 393):
    print(item)
for a,b in ((12, 33), (2, 35)):
    print(a, b)
#셋
for item in {"WSM", "JAVA", "PYTHON"}:
    print(item)
#딕셔너리
pl = {"C":1972, "JAVA":1995, "Python":1991}
for item in pl: #value를 제외한 key값만 들어가게 된다.
    print(item)
for key in pl.keys():
    pl.keys()
for val in pl.values():
    print(val)
for key, value in pl.items():
    print(key, val)

#num_list 문제
num_list = [-5, 127, -13, 9, -21, 100]
for num in num_list:
    if num>0 :
        print(num, end, ' ')
print()
#짝수, 홀수
num_list = [13, 8, 7, 55, 100, 2, 12, 10, 17]
for num in num_list:
    if num%2==0 :
        print("{}는 짝수이다.".format(num))
    else:
        print("{}는 홀수이다.".format(num))
print("-------------------------------------")
holzzak = ["짝수", "홀수"]
for num in num_list:
    print(num)
    print(holzzak[num%2])
    print("{}은 {}이다.".format(num, holzzak[num%2]))

#자리수
for num in num_list:
    print('{}은 {}자리수이다.'.format(num, len(str(num))))
print("=======================================")
#for문 실전문제
sev = {"에스쿱스":90,"정한":100,"조슈아":95,"버논":30, "디노":25}
for name, score in sev.items() :
    if score>=60 :
        print("{} 은(는) 합격입니다.".format(name))
    else :
        print("{} 은(는) 탈락입니다.".format(name))
#for문 - range()
#range(시작값, 종료값, 단계)
print(list(range(0, 10, 1)))
print(list(range(10, 0, -1)))
print(reversed(range(0,10)))
print(list(range(0, 10, 5)))

#시작값, 증가값 : 1
print(list(range(0, 10, 1)))
print(list(range(0,10)))
print(list(range(10)))
#리스트
nctdream = ['런쥔', '제노', '해찬', '마크', '재민', '지성', '천러']
for member in nctdream:
    print(member)

for i in range(0, len(nctdream)):
    print(i+1, nctdream[i])
#같은 값
for i, member in enumerate(nctdream):
    print(i+1, member)

#1부터 200까지 자연수 중 3의 배수의 합
sum_value = 0
for i in range(201):
    if i%3==0:
        sum_value+=i
print(sum_value)

#500부터 1000까지의 자연수 중 5의 배수의 합
sum_value = 0
for i in range(500, 1001, 5):
        sum_value+=i
print(sum_value)

print(sum(list(range(500, 1000, 5))))

#sum()함수, max, min
l = [1, 2, 3, 4, 5]
print(sum(l))
print(max(l))
print(min(l))
print("==========================")

for i in range(1, 10, 1):
    print("2 X {} = {}" .format(i, 2*i))
print("==============================")
for i in range(2, 10):
    for j in range(2, 10):
        print("{} X {} = {}".format(i, j, i*j))



