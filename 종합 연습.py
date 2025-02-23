import math

hole = [0,10]
my_ball = [10,0]
target = [7,6]
r = 1
a = math.sqrt(hole[-1]**2 + my_ball[0] **2)
b = math.sqrt((hole[-1] - target[-1])**2 + target[0] **2)
print(r,a,b)
ga = math.atan(my_ball[0]/hole[-1])
ga = math.radians(ga)
ga = math.degrees(ga)
da = math.acos(b/a)
print(ga,da)