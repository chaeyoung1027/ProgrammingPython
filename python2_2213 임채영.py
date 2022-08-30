# 2213 임채영
# 1
def sum_odd(num):
    sum_val = 0
    for n in num:
        if int(num)%2==0:
            sum_val=sum_val+int(n)
    return sum_val

result = sum_odd('01012345678')
print(result)
result = sum_odd('01022224444')
print(result)
result = sum_odd('01099999999')
print(result)


# 2
def encrypt(yd):
    yd = yd.replace('a', '*')
    yd = yd.replace('A', '*')
    yd = yd.replace('e', '*')
    yd = yd.replace('E', '*')
    yd = yd.replace('i', '*')
    yd = yd.replace('I', '*')
    yd = yd.replace('o', '*')
    yd = yd.replace('O', '*')
    yd = yd.replace('u', '*')
    yd = yd.replace('U', '*')
    return yd

print(encrypt('ive'))
print(encrypt('nct dream'))
print(encrypt('AEiou'))
print(encrypt('GOOGLE'))
print(encrypt('BTS'))
print('-'*30)
# 3
def dec_to_bin(num):
    num = bin(num)
    num = num.replace('0b', '')

    return num

print(dec_to_bin(10))
print(dec_to_bin(2))
print(dec_to_bin(77))
print(dec_to_bin(1024))
print('-'*30)

# 4
# def avvreviate(name):
#     for i in name:
#         if i==' ':
#             continue
#             a=i
#     return a

#print(avvreviate("Maverick"))

# 5
def fare_pc(minute):
    min = 0
    money = 0
    min = (minute - (minute % 10)) / 10
    if minute % 10 != 0:
        min = min + 1
    return int(min * 1000)


print(fare_pc(minute=3))
print(fare_pc(minute=20))
print(fare_pc(minute=34))

print('-'*30)

# 6
def get_bmi(height, weight):
    height = height / 100
    bmi = round(weight / (height ** 2), 2)
    bj = ''
    if bmi < 18.5:
        bj = "저체중"
    elif bmi >= 18.5 and bmi < 23:
        bj = "정상"
    elif bmi >= 23 and bmi < 25:
        bj = "과체중"
    elif bmi >= 25:
        bj = "비만"
    return bj, bmi


print(get_bmi(height=170, weight=60))
print(get_bmi(height=150, weight=60))
print(get_bmi(height=180, weight=50))
print(get_bmi(height=160, weight=60))

print('-'*30)

# 7
def minus_time(hour1, minute1, hour2, minute2):
    hour = hour1 - hour2
    minute = minute1 - minute2
    if minute<0 and hour>0:
        hour=hour-1
        minute=minute+60

    if minute >= 0:
        sign = '+'
    elif minute < 0:
        sign = '-'
    if minute < 0:
        minute = -minute
    if hour < 0:
        hour = -hour

    return sign, hour, minute


sign, hour, minute = minus_time(hour1=13, minute1=40, hour2=6, minute2=33)
print(sign, hour, minute)
sign, hour, minute = minus_time(hour1=6, minute1=33, hour2=13, minute2=40)
print(sign, hour, minute)
sign, hour, minute = minus_time(hour1=13, minute1=40, hour2=13, minute2=40)
print(sign, hour, minute)
sign, hour, minute = minus_time(hour1=2, minute1=3, hour2=0, minute2=4)
print(sign, hour, minute)
sign, hour, minute = minus_time(hour1=2, minute1=3, hour2=2, minute2=4)
print(sign, hour, minute)

print('-'*30)

#8
def rgb_to_hex(r, g, b):
    color = ''
    r = hex(r)
    g = hex(g)
    b = hex(b)
    color=('#'+str(r)+str(g)+str(b))
    color = color.replace('0x', '')
    color = color.replace('0', '00')
    return color

print(rgb_to_hex(r = 255, g=255, b=255))
print(rgb_to_hex(r = 255, g=0, b=127))
print(rgb_to_hex(r = 0, g=0, b=0))
# 2213 임채영
