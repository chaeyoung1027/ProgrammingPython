#숫자
student_number = 2113
age = 18
height = 165.7

#문자
name = '임채영'

print(f'학번 : {student_number}\n이름 : {name}\n나이 : {age}\n키 : {height}\n')  #학번 : 2213

print(type(student_number)) #<class 'int'>
print(type(name)) #<class 'str'>
print(type(age))#<class 'int'>
print(type(height))#<class 'float'>
print(type(10.27))#<class 'float'>
print(type(1027))#<class 'int'>
print(type('1027'))#<class 'str'>
print((10/27))#java : 0, python/ 0.37037037037037035
print((27/10))#java : 2, python/ 2.7
#java : 몫 = /, 나머지 = %  python : 우리가 알고있는 나누기(float형이 됨)
print(27//10) #python : 나눈 몫을 구할 때 / 2개  !!!!!!!!!!!!!!시험문제(정수형임)
print(27%10) #python : 나머지 : 7
print(type(10/27))#<class 'float'>
print(type(10//27))#<class 'int'>
print(10/5) #2.0 <class 'float'>

#변수 이름 규칙, 자료형반환
#my_mbti, my_function(), MyClass  #myMbti : camel-case, my_mbti : snake-case
my_mbti = "INFP" #""를 쓰면 오류가 나는 이유 : 문자열 말고 변수명으로 인식하기 때문
print(f'My MBTI {my_mbti}')

print('My MBTI : '+my_mbti+'age : '+str(age))    #java : String.toString(age); python : str(age)
height = '170'
print(float(height)+10) #java : Float.parseFloat(height);   python : float(heihgt);

#str(), int(), float() : 자료형변환 함수
#+연산자 : 숫자+숫자 => 덧셈, 문자+문자 =>문자문자, 문자 * 숫자 : 문자를 숫자만큼 반복
print(18+2)     #20
print('18'+'2') #'182'
print(18 * 2)   #36
print('2'*2)    #2222

#짝을 10번 출력
print('짝'*10)

print(18 ** 3)  #거듭제곱

#진수 #java : 8진수 0o; 16진수 0x
#binary : 2진수의
print(0b10) #2진수 2
print(0o10) #8진수 8
print(0x10)   #10진수 10
print(0xFF)   #16진수 FF : 255 소문자 가능

#10진수 -> 2진수
print(bin(10))  #Ob1010
print(bin(9))