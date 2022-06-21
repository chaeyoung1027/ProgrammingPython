#예약어X
#snake_case
#sum = 0    TypeError:'int' object is not callable
#def sum(x):
#    print(x)#내장함수와 이름이 같으면 에러는 안나지만, 내장함수를 호출할 수 없음
a = sum([10, 20, 3])
print(a)    #none = null
print('-'*20)
'''
java 함수
접근제어자(:캡슐화를 위해서) 반환형 함수명(파라미터1, 파라미터2){
    return 값;
}

C 함수
반환형 함수명(파라미터1, 파라미터2){
    return 값;
}

python 함수
def(ine) 함수명(파라미터1, 파라미터2):
    return 값
'''
def my_print(age):
    print('임정훈 : '+str(age)+'살입니다.')# 이름: 살입니다.
    print('임정훈 :', age, '살입니다.')#이름 :  20 살입니다.
    print(f'임정훈 : {age}살입니다. ')


print('-'*20)

def my_print2(name, age):
    print(name +" : "+str(age)+'살입니다.')# 이름: 살입니다.
    print(name,':', age, '살입니다.')#이름 :  20 살입니다.
    print(f'{name} : {age}살입니다. ')
print('-'*20)

print(my_print2('안유진',20))
print(my_print2(age = 20, name = '안유진'))    #야규먼트 순서와 관계없이 파라미터 이름을 쓰면 거기에 들어감

def my_print3(name, age, group):
    print(name +" : "+str(age)+'살입니다.',group,'소속입니다.')# 이름: 살입니다.
    print(name,':', age, '살입니다.')#이름 :  20 살입니다.
    print(f'{name} : {age}살입니다. {group}소속입니다.')

print(my_print(20))   #my_print()실행 my_print()의 리턴값 출력
print(my_print2(age = 20, name = '안유진'))

print(my_print(20))   #my_print()실행 my_print()의 리턴값 출력
print(my_print2('안유진',20))
print(my_print2(age = 20, name = '안유진'))    #야규먼트 순서와 관계없이 파라미터 이름을 쓰면 거기에 들어감

my_print3(age = 20, name = '안유진', group = '아이브')
#my_print3(age = 20, name = '안유진', '아이브')#키워드 인자 뒤에는 계속 키워드 인자 해야함
my_print3('안유진', age = 20, group = '아이브')#위치 인자는 무조건 키워드 인자 앞에 있어야 함
print('-'*20)

def my_print4(name, age, group = '아이브'):
    print(name +" : "+str(age)+'살입니다.',group,'소속입니다.')# 이름: 살입니다.
    print(name,':', age, '살입니다.')#이름 :  20 살입니다.ㅜ
    print(f'{name} : {age}살입니다. {group}소속입니다.')
my_print4('안유진', age = 20, group = '아이즈원')#위치 인자는 무조건
print('-'*20)
#가변인자
def my_print5(*args):
    print('정보 : ')
    #print(type(args))
    for arg in args:
        print(arg)

def my_print6(name, *args):
    print('{name}정보 : ')
    #print(type(args))
    for arg in args:
        print(arg)

my_print5('안유진',20,'다이브 ','러브다이브')
my_print6('안유진',20,'다이브 ','러브다이브')
print('-'*20)

# def my_print7(name, age = 20, group):#기본값있는 파라미터 뒤에는 무조건 기본값있는 파타리머
# #    print(name +" : "+str(age)+'살입니다.',group,'소속입니다.')# 이름: 살입니다.
# #    print(name,':', age, '살입니다.')#이름 :  20 살입니다.ㅜ
# #    print(f'{name} : {age}살입니다. {group}소속입니다.')

def say(name, msg = '안녕하세요', feeling = '♥'):
    print(f'{name}, {msg}, {feeling}')
say('인소리')
say('채영', feeling='🤣')
print('-'*20)

def fn(a, b = []):
    b.append(a)
    print(b)
fn(3)   #[3]
fn(5)   #[5]X [3, 5]
fn(10, [1]) #[1, 10]
fn(7)   #[3, 5, 7]
print('-'*20)

say('현진', '미안행')
#지금부터 20년 후의 내 나이를 리턴하자
# def plus20(age):
#      age+20
#     # pass #지금 쓸 말이 기억이 안 나면 에러가 안 나도록 pass써두기
# a = plus20(18)
# print(a)    #None : plus20() reutrn 값이 없어서 None리턴 웬만하면 def안에 print하지말고 return

def plus20_2(age):
    return age+20
a = plus20_2(18)
print(a)
print('-'*20)

#전화번호 앞 자리(지역변호)와 맨 뒤 4자리 출력하자
def tel(number):
    index = number.find('-')
    f = number[:index]
    b = number[-4:]
    return f, b #(f, b)
# front = '010'
# back = '5678'
front, back = tel('010-8988-0515')

print(f'앞 : {front}\t뒤 : {back}')
print('-'*20)
#min_max([3, 31, 1, 6, 5, -6])
def min_max(*리스트):
    if len(리스트)<0:
        return None;
    a = 리스트[0]
    b = 리스트[0]
    for i in 리스트[1:]:   #리스트[1:] : 0번째는 비교하지 않아도 됨
        if a>i:
            a = i
        elif b<i:
            b = i
    return a, b

min_value, max_value = min_max(3, 31, 1, 6, 5, -6)
print(f'최소 : {min_value}\t최대 : {max_value}')
#count, sum, min, max


