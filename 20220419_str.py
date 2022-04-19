greeting = 'hello'
to = 'world!'
say_hello = greeting+','+to
print(say_hello)
print(greeting * 5)
print(greeting + '\n' + to)
print("\""+greeting+"\"")
print('\''+greeting+'\'')
#주석 달기
names = '''양다연
인소리
이예진
'''
print(names)

#*** 시험문제   indexing, slicing
#indexing
names = '양다연인소리이예진'
print(names[2])#연 출력
print(names[4])#소
print(names[8])#진
print(names[-1])#진
print(names[-2])#예
student_number = '2112'
print(student_number[0]+'학년')    #학년 알아내기
print(f'{student_number[0]}학년')
print(f'{student_number[1]}반')
#slicing
print(names[2:5])   #[2]~[4]
print(names[2:4])   #연인
print(names[-7:-5])
print(names[4:7])   #소리이
print(names[7:9])   #예진
print(f'{student_number[2:4]}번')
print(f'{student_number[-2:]}번')    #start : end-1 [start: ] : 끝까지
print(f'{student_number[0:2]}''학년반')
print(f'{student_number[0:-2]}''학년반')
print(f'{student_number[:-2]}''학년반') #start : end-1 [: end-1] : 앞까지
print(f'f{student_number[:]}')         #start : end-1 [ : ] : 앞~ 끝까지

#문자열 함수
print(f'길이 : {len(student_number)}') #4
print(f'2의 개수 : {student_number.count("2")}')
print(f'{"NCT dream darling".upper()}') #다 대문자
print(f'{"NCT dream darling".lower()}') #다 소문자
s = "       NCT dream buffering         "
print(f'{s.strip()}')   #공백 벗기기
print(f'{s.rstrip()}')  #오른쪽 벗기기
print(f'{s.lstrip()}')  #왼쪽 벗기기
print(f'{s.find("d")}') #[7]
print(f'{s.rfind("d")}') #오른쪽부터 찾기
print(f'{s.find("z")}') #없으면 -1
print(f'{s.count("e")}')   #e의 개수세기
#print(f'{s.index("d")}') #없으면 에러(ValueError : substring not found)
print(f'{s.replace("buffering", "hello future")}')     #바꾸기(원본이 바뀌는 것이 아니라 바뀐 문자열로 return만 함.
print(s)

#있나 없나(true or false)
print('e' in s)
print('z' in s)

#split, join
#split : 쪼개기
ip = '10.253.123.419'
ip_list = ip.split('.')
print(ip_list)
names = '양다연, 최자윤, 임채영, 이예진, 인소리'
names_list = names.split(',')
print(names_list)
print(names_list[2 : 4])
ip_list_str = '::'.join(ip_list)
print(ip_list_str)
names_list_str = ' | '.join(names_list)
print(names_list_str)
print(", ".join(names_list))