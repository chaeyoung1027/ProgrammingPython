#2. 영단어를 인자로 받아, 모음이 a, e, i, o, u만 *로 대체하여 리턴
def encrypt(word):
    result = ''
    #영단어를 한글자씩 꺼내자
    for char in word:
    #a인지 또는 e인지 또는 i인지 또는 o인지 또는 u인지 구분하자
        if char == 'a' or char == 'e' or char == 'i' or char=='o' or char=='u':
    #맞으면 *로 바꾸기
            char='*'
            result+=char
    #다르면 그대로
        else:
            result+=char
    return result

print(encrypt('ive'))   #*v*

#문자열 리턴: 숫자 sum과 비슷
# string = ''
# for 하나 in 덩어리:
#     string += 하나
