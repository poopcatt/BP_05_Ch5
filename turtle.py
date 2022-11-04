#기초파이썬 5장 연습문제 터틀그래픽


8. #사용자로부터 2개의 원에 대한 정보를 받아서 화면에 원을 그린 후에 조건문을 사용하여 큰 원 안에 작은 원이 포함되는지를 
   #판단하는 프로그램을 작성하라.
   
import turtle
t = turtle.Turtle()
t.shape("turtle")

x1 = int(input("큰 원의 중심좌표 x1: "))
y1 = int(input("큰 원의 중심좌표 y1: "))
r1 = int(input("큰 원의 반지름: "))
x2 = int(input("작은 원의 중심좌표 x2: "))
y2 = int(input("작은 원의 중심좌표 y2: "))
r2 = int(input("작은 원의 반지름: "))

d = ((x1-x2)**2 + (y1-y2)**2)**0.5

t.up()
t.goto(x1, y1-r1)
t.down()
t.circle(r1)
 
t.up()
t.goto(x2, y2-r2)
t.down()
t.circle(r2)
 
if (d + r2 < r1):
   t.write("두번째 원이 첫번째 원의 내부에 있습니다.")
elif (d < r1 + r2):
   t.write("두번째 원은 첫번째 원에 걸쳐 있습니다.")
else:
   t.write("작은 원은 큰 원 외부에 있습니다.")
t.screen.exitonclick()
