#예약어
import keyword
print(keyword.kwlist)

print('-' * 20)
#달력
import calendar
print(calendar.month(2022, 4))
print(calendar.month(2005, 10))
print(calendar.month(2022, 12))
print(calendar.month(1977, 10))

print('-'*200)
#현재 날짜와 시각 보기
import datetime
now = datetime.datetime.now()
print(now)
print(now.year, now.month, now.day, now.hour, now.minute, now.second)
birthday = datetime.datetime(2022, 4, 11)
print(now - birthday)
my_birthday = datetime.datetime(2005, 10, 27)
print(now-my_birthday)
christmas = datetime.datetime(2022, 12, 25)
print(christmas-now)

print('-' * 200)
# #윈도우 보기
# import tkinter as tk
# base = tk.Tk()
# base.mainloop()

#turtle
import turtle as t
t.shape('turtle')
# t.forward(100)
# t.right(90)
# t.forward(100)
# t.right(90)
# t.forward(100)
# t.right(90)
# t.forward(100)
# t.right(90)
# t.speed() : 속도

#foward : fd / left : rt / right : rt
#pen

t.bgcolor('red')
t.forward(300)
t.left(144)
t.fillcolor('white')
t.bgcolor('orange')
t.forward(300)
t.left(144)
t.fillcolor('black')
t.bgcolor('yellow')
t.forward(300)
t.left(144)
t.fillcolor('white')
t.bgcolor('green')
t.forward(300)
t.left(144)
t.fillcolor('black')
t.bgcolor('blue')
t.forward(300)
t.left(144)
t.fillcolor('white')
t.bgcolor('purple')
#t.fillcolor('blue')

t.mainloop()

