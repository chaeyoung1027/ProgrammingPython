#이니셜 abbreviate(약어)
def abbreviate(name):
    name = name.strip()
    #한글자씩 꺼내기
    for index, sp in enumerate(name):
        #첫 번째 글자 저장
        if index==0:
            result = sp.upper()+'. '
        #띄어쓰기! -> 한 칸 뒤에 있는 글자를 -> 대문자로 바꾸고 -> 저장
        if sp == ' ':
            result += name[index+1].upper()+'. '
    return result.strip()
#strip = 양 끝 공백 제거

def abbreviate2(name):
    result = '. '.join([word[0].upper() for word in name.split()])
    #name.split() : 띄어쓰기, 탭 등의 빈공간 단위로 잘라서 리스트에 넣어준다. 괄호에 문자를 넣으면 그 단위로 잘린다.
    return result+'. '

print(abbreviate('Maverick'))   #M.
print(abbreviate('Hae Chan'))   #H. C.
print(abbreviate('jin young park')) #J, Y, P.
print(abbreviate(' jin young park ')) #J, Y, P.

print(abbreviate2('jin young park')) #J, Y, P.
print(abbreviate2(' jin young park ')) #J, Y, P.