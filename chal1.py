#CHALLENGES 52-59
#52
import random
num=  random.randint(1,100)
print (num)

#53
import random
fruits=random.choice(['Watermelon', 'Strawberry', 'Cherry', 'Orange', 'Pineapple'])
print(fruits)

#54
import random
ask= input('Make a choice : h or t')
choose=random.choice(['h', 't'])
if ask==choose :
    print('You win')
else :
    print('Bad luck')
    print('The computer has selected', choose)

#55
import random
ask= int(input('Enter a number between one and five :'))
choose= random.randint(1,5)
if ask==choose :
    print('Well done !')
elif ask > choose :
    print('The number you have chosen is too high !')
    ask= int(input('Enter a number between one and five :'))
    if ask==choose :
        print('Correct !')
    else :
        print('You lose !')
elif ask < choose :
    print('The number you have chosen is too low !')
    ask= int(input('Enter a number between one and five :'))
    if ask==choose :
        print('Correct !')
    else :
        print('You lose !')


#56
import random
ask=int(input('Enter a number between one and ten '))
num=random.randint(1,10)
while ask != random :
    ask=int(input('Enter a number between one and ten '))

#57
import random
ask=int(input('Enter a number between one and ten '))
num=random.randint(1,10)
if ask > random :
    print('The number you have chosen is too high !')
    ask=int(input('Enter a number between one and ten '))
elif ask < random :
    print('The number you have chosen is too low !')
    ask=int(input('Enter a number between one and ten '))

#58 
import random
score=0
for i in range (1,6) :
    num1 = random.randint(1,50)
    num2= random.randint(1,50)
    correct= num1+num2
    print(num1, '+', num2,'=')
    answer= int(input('Your answer :'))
    print()
    if correct==answer : 
        score = score + 1

print('You scored', score, 'out of 5')
        
#59
import random 
print('Select from red, blue, green, white, black ')
color= random.choice(['Red', 'Blue', 'Yellow', 'White', 'Black'])  
ask= input('Choose a color :')
tryagain= True
while tryagain== True :
    theirchoice= input('Enter a color :')
    theirchoice= theirchoice.lower()
    if color== theirchoice :
        print('Well done')
        tryagain= False
    else :
        if color=='red' :
            print('I bet you are seeing RED right now')
        elif color =='blue' :
            print ('Do not feel BLUE')
        elif color =='green' :
            print(' I bet you are GREEN with envy right now')
        elif color == 'white' :
            print('Are you WHITE as a sheet, as you did not guess correctly ? ')
        elif color == 'pink' :
            print('Shame you are not feeling in the PINK, as you got it  wrong')

