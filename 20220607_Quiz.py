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
