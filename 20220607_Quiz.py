#1. 휴대전화번호를 입력하면 -, /, 띄어쓰기를 없애고 숫자만 출력
phone_number = '010-7240-4658'
# 01072404658
#방법 1
for n in phone_number:
    if n == '-' or n=='/' or n==' ':
        continue
    print(n, end = '')

print()

# 방법 2
phone_number = phone_number.replace('-','')
phone_number = phone_number.replace('/','')
phone_number = phone_number.replace(' ','')
print(phone_number)

print('-'*40)

#2. 학번 -> 학년, 반, 학과, 번호 출력하기
student_number = '2108'
# #2학년 1반 뉴미디어소프트웨어과 08번
# if student_number[1] == '1' or student_number[1]=='2' :
#     g = '뉴미디어소프트웨어과'
# elif student_number[1] == '3' or student_number[1]=='4':
#     g = '뉴미디어웹솔루션과'
# elif student_number[1] == '5' or student_number[1]=='6':
#     g = '뉴미디어디자인과'

majors = ['뉴미디어소프웨어과', '뉴미디어소프웨어과', '뉴미디어웹솔류션과', '뉴미디어웹솔류션과', '뉴미디어디자인과', '뉴미디어디자인과']
index = int(student_number[1])
g = majors[index-1]

print(f'{student_number[0]}학년 {student_number[1]}반 {g} {int(student_number[2:])}번 ')

print('-'*40)