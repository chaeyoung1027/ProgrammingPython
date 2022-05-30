'''
조건식 = True 또는 Flase로 결정되는 문장
파이썬에서 if문 작성시 유의해야 할 사항 - 콜론, 들여쓰기
'''
if True:
    print("실행")

# 교통수단 결정 문제
# money = 15000
if money >= 10000:
    print("택시를 타라")
else:
    print("버스를 타라")
# input()은 string
# input 함수
x = input()
print(x, type(x))
num = int(input())
print(num.type(num))

# 교통수단 결정 문제 + input 함수
money = int(input('돈을 입력하시오 : '))
if money >= 10000:
    print("택시를 타라")
else:
    print("버스를 타라")

# 짝수 판별 문제
num = int(input('정수를 입력하시오 : '))  # int로 꼭 변환해야한다
if num % 2 == 0:
    print("짝수")
else:
    print("홀수")

# 문제 2
password = input('문자를 입력하시오 : ')
if password == "미림여자정보과학고":
    print("암호이다")
else:
    print("암호가 아니다")

