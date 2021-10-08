#CHALLENGES 35-44

#35
name= input('Enter your name : \n')
for i in range (0,3) :
    print(name)

#36
name= input('Enter your name : \n')
number=int(input('Enter a number : \n'))
for i in range (0,number) :
    print(name)

#37
name= input('Enter your name : \n')
for i in name :
    print(i)

#38
name= input('Enter your name : \n')
number=int(input('Enter a number : \n'))
for x in range(0,number):
    for i in name:
        print(i)

#39
number= int(input('Enter a number between 1 and 12 : \n'))
for i in range(1,13) :
    answer= i* number
    print(i, 'x', number,'=', answer)

#40
number= int(input('Enter a number below 50 :\n'))
for i in range (50, number-1, -1) :
    print(i)

#41
name=input('Enter your name :\n')
number= input('Enter a number less than 10 :\n')
if number < 10:
    for i in range(0,number):
        print(name)
else:
    for i in range(0,3) :
        print('Too high')

#42
total=0
for i in range(0,5) :
    number =int(input('Enter the number'))
    ask=input('Do you want that number included ?')
    if ask=='yes':
        total= total + number
print(total)

#43
ask= input('What direction do you want to count?')
if ask=='up':
    number=int(input('Enter the top number : \n'))
    for i in range(1, number +1) :
        print(i)
elif ask=='down':
    number=int(input('Enter a number below 20 :\n'))
    for i in range (20, number -1, -1) :
        print(i)
else:
    print('I do not understand !')

#44
pers=int(input('How many persons do you want to invite to the party ?'))
if pers<10:
    for i in range(0,pers) :
        name=input('Enter a name')
        print(name, 'has been invited')
elif pers>=10 :
    print('Too many people')

