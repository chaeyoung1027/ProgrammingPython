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
print('-'*20)
print('-'*20)
