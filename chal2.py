#CHALLENGES 12-19
#12
num1= int(input('Enter the first number :'))
num2= int(input('Enter the second number :'))
if num1>num2 :
    print(num2, num1)
else :
    print(num1,num2)

#13
num1= int(input('Enter a value under 20 :'))
if num1>=20 :
    print('Too high')
else :
    print('Thank you')

#14
num1= int(input('Enter a value between 10 and 20 :'))
if 10<=num1<=20 :
    print('Thank you')
else :
    print('Incorrect answer')

#15
color= (input('Type in your favorite color'))
if color=='red' or color=='RED' or color=='Red':
    print ('I like red too !')
else :
    print ('I don’t like', color, ',I prefer red')

#16
rain= input('Is it raining ?')
rain=str.lower(rain)
if rain=='yes':
    windy=input('Is it windy?')
    windy= str.lower(windy)
    if windy=='yes':
        print ('It is too windy to take an umbrella !')
    else:
        print ('Take an umbrella')
else : 
    print('Enjoy your day !')

#17
age= int(input('How old are you?'))
if age>=18 :
    print('You can vote ')
elif age==17:
    print ('You can learn to drive')
elif age==16 :
    print('You can buy a lottery ticket')
elif age<16 :
    print ('You can go Trick or Treating')

#18
num=int(input('Enter a number :'))
if num<10 :
    print('Too low')
elif 10<=num<=20 :
    print('Correct')
else :
    print('Too high')

#19
num=int(input('Enter 1, 2 or 3 :'))
if num==1 :
    print('Thank you')
elif num==2 :
    print('Well done')
elif num==3 :
    print('Correct')
else:
    print('Error')
