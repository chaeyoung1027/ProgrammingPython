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

#3. N-Sum 10자리 숫자보다 작은 숫자를 넣으면 각자리의 숫자의 합계를 출력하기
# print('숫자를 입력하세요 -> ', end='')
num = 12345
sum_val = 0
#숫자 한자리씩 빼서 계산
while num!=0:
    sum_val += num%10
    num = num// 10
print(sum_val)

#문자 한자리씩 빼서 계산
num = 12345
number_s = str(num)
sum_val2 = 0
for n in number_s:
    sum_val2+=int(n)
print(sum_val2)
