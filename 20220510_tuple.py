t = ()  #빈 튜플
xy = (2560, 1440)
color = 129, 247, 216
print(t)        #()
print(xy)       #(2560, 1440)
print(color)    #(129, 247, 216)
print(xy+color) #(2560, 1440, 129, 247, 216)
print(xy*2)     #(2560, 1440, 2560, 1440)
#패킹, 언패킹 : 자동
color = 129, 247, 216   #패킹
red, green, blue = color    #언패킹
print(red)  #129
x,y = (1920, 1080)
print(y)    #1080
print(color[1]) #인덱싱이 가능하다.
print(color[0:2])   #슬라이싱이 가능하다.
#color[1] = 255      #TypeError: 'tuple' object does not support item assignment
new_tuple = xy + color + (1440, 1080)
print(new_tuple)
print(new_tuple.index(1440))    #1
print(new_tuple.count(1440))    #2
임채영, 이예진 = 10, 8
print(임채영)
print(이예진)
이예진, 임채영 = 임채영, 이예진
print(임채영)
print(이예진)

