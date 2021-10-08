#CHALLENGES 27-34
#27
num=float(input('Enter a number with a lot of decimals :'))
pro= num*2
print(pro)

#28
num=float(input('Enter a number with a lot of decimals :'))
pro= num*2
print(round(pro,2))

#29
import math
num=int(input('Enter a number over 500 :'))
sqrt= math.sqrt(num)
print (round(sqrt,2))

#30
import math
print(round(math.pi, 5))

#31
import math
radius= int(input('Enter the radius of a circle :'))
area= math.pi*radius**2
print(area)

#32
import math
radius= int(input('Enter the radius of a cylinder :'))
depth= int(input('Enter the depth of a cylinder :'))
circlearea= math.pi * radius**2
volume= circlearea*depth
print(round(volume,3))

#33
import math
num1= int(input('Enter the first number :'))
num2= int(input('Enter the second number :'))
div= num1//num2
remain= num1%num2
print( num1, ' divided by', num2, 'is', div, 'with', remain, 'remaining ')

#34
import math
x= int(input( ' 1) Square \n 2) Triangle \n \n Enter a number:' ))
print(x)
if x==1 :
    side= int(input('Enter the lenght of one side :'))
    area1= side*side
    print('The area of your chosen shape is', area1)
elif x==2:
    base= int(input('Enter the base :'))
    height= int(input('Enter the height :'))
    area2= (base*height)/2
    print('The area of your chosen shape is', area2) 
else:
    print('Incorrect option selected')
