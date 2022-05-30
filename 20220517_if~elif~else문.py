#교통수단 문제
# money = int(input('돈을 입력하시오 : '))
# if money >= 10000:
#     print("택시를 타라")
# elif money >=720:
#     print("버슬를 타라")
# else:
#     print("그냥 걸어가라")

#배수 판별 문제
# num = int(input('정수를 입력하시오 : '))
# if num % 4 ==0:
#     print("4의 배수")
# elif num % 3 ==0:
#     print("3의 배수")
# elif num % 2 == 0:
#     print("2의 배수")
#
# print('----------------------------')
#
# num = int(input('정수를 입력하시오 : '))
# if num % 4 ==0:
#     print("4의 배수")
# if num % 3 ==0:
#     print("3의 배수")
# if num % 2 == 0:
#     print("2의 배수")
#

#나이대 판별 문제
# age = int(input('나이를 입력하시오 : '))
# if age >= 10 and age < 20 : #10 <= age < 20
#     print("10대")
# elif age >=30 and age <40:  #30 <= age < 40
#     print("30대")
# else:
#     print("10대,30대가 아님")
#
# print("-----------------------")
# print(str(age//10*10) + "대")

#논리연산자 문제
# x = int(input('정수를 입력하시오 : '))
# if x > 10 and x % 2 ==0:
#     print("10 초과 짝수")

#점수 등급 문제
# jumsu = int(input('점수를 입력하시오 : '))
# if 100 <= jumsu >=90:
#     print("A")
# elif jumsu >=80:
#     print("B")
# elif jumsu >=70:
#     print("C")
# elif jumsu >= 60:
#     print("D")
# else:
#     print("F")

#mbti 문제
# mbti = input('MBTI를 입력하시오 : ')
# if mbti == "ESTP" or mbti == "estp":    #mbti.upper() == ESTP
#     print("IoT 개발형")
# elif mbti == "INFP" or mbti == "infp":
#     print("블록체인형")
# else:
#     print("아직 개발중입니다.")

# #중첩제어문 문제
# x = int(input('정수를 입력하세요 : '))
# if x > 10:
#     if x % 2 ==0:
#         print("10초과 짝수")
#     else:
#         print("10초과 홀수")
# else:
#     print("10이하")

#문제
nickname = "yejin18"
id = "yejin"
password = "qwer1234"
id = input('ID를 입력하세요 : ')
if id == id:
    id = input('PW를 입력하세요 : ')
    if password == password:
        print('환영합니다 { } 님'.format(nickname))
    else:
        print("패스워드가 틀렸습니다")
else:
    print("알 수 없는 사용자입니다.")
