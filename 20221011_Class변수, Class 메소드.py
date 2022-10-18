#클래스 변수 : 객체로 생성하지 않아도 클래스에 하나 존재하는 변수
#클래스 메소드 : 객체로 생성하지 않아도 클래스에 하나 존재하는 메소드

#학생
#속성 : 학번, 이름

#동아리
#속성 : 동아리명, 장소, 멤버들
#메소드 : 장소 설정하기(), 멤버 추가하기(), 활동하기

class Student:
    def __init__(self, student_number, name):
        self.student_number = student_number
        self.name = name
    def __str__(self):
        return f'학번 : {self.student_number}\t이름 : {self.name}'

    def __getitem__(self, key):     #객체[key] 재정의
        if key == '학번':
            return self.student_number
        #객체['학년'] 햇을 때, return 학년
        if key == '학년':
            return self.student_number[0]

#동아리
#속성 : 동아리명, 장소, 멤버들
#메소드 : 장소 설정하기(), 멤버 추가하기(), 활동하기()

class Club:
    count = 0 #클래스 변수

    @classmethod
    def get_count_club(cls):
        return f'만들어지는 클래스 수 : {cls.count}'

    def __init__(self, name):
        self.name = name    #동아리 이름
        self.location = None    #장소
        self.members = []       #멤버
        Club.count += 1 #self 안붙임

    def __str__(self):
        s = ''
        for member in self.members:
            s += str(member) + '\t'
        return f'동아리명 : {self.name}\n장소 : {self.location}\n멤버들 : {s}'
    def set_location(self, location):
        self.location = location

    def add_member(self, student):
        self.members.append(student)

    def set_action(self, action):
        self.action = action

    def act(self):
        print(self.action)


학생1 = Student('2213', '임채영')
print(학생1)
학생2 = Student('2106', '양다연')

동아리1 = Club("사진반")
동아리1.set_location("실습1실")
동아리1.set_action("사진 찍기")
동아리1.add_member(학생2)
동아리1.add_member(학생1)
print(동아리1)
동아리1.act()

동아리2 = Club("보드게임반")
동아리2.set_action("보드게임반")
동아리2.add_member(학생1)
print(동아리2)
동아리2.act()

print(Club.count)
print(동아리1.count)
print(Club.get_count_club())
print(동아리2.get_count_club())

#사진반 멤버 수 출력
print(len(동아리1.members))


#특수 메소드
#__init__(self, ...)    생성자 : 멤버변수 초기화
#__str__(self)     클래스의 객체를 문자열화 한다.(주로 객체의 속성을 알아볼 수 있도록 정보 표시) <주관식

#__len__(self)      len(객체) 재정의

#__getitem__(self, key)     객체[key] 재정의
print('__getitem__()')
print(학생1)
print(학생1['학번'])
print(학생1['학년'])

#__del__(self)