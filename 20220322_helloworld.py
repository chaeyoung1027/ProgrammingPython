# ""와 ''의 구분이 (없음)
print("Hello, World!") #""와 ''가 같다.
name = "양다연"
print('Hello, '+name+'!') #java 형식
print('Hello, &s' + name) #c 형식
print('Hello, {}'.format(name)) #format함수
print(f'hello,{name}!') # f-string 형식#f-string형식

print('Red velvet\'s favorite song is Red flavour')
print("Red velvet's favorite song is Red flavour")
#문자 ' = \'로 표현할 수 있음.

student_number = "2113"
name = "임채영"# ",'로 묶지 않으면 변수로 봄.
print(f"학번 : "+student_number+", 이름 : "+name)# 앞에 f : format
print(f"학번 : {student_number}, 이름 : {name}")