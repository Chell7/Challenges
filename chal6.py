#CHALLENGES 45-51
45
total=0 
while total <=50 :
    num=int(input('Enter a number :\n'))
    total= total+ num
    print('The total is', total)

#46
num=0
while num<= 5:
    num=int(input('Enter a number \n'))
print('The last number you entered was a', num)

#47
num1=int(input('Enter the first number :\n'))
total=num1
again='y'
while again=='y' :
      num2=int(input('Enter another number :\n')) 
      total = total + num2
      again= input('Do you want to add another number ? (y/n')
print('The total is', total)

#48 
again='y'
count= 0
while again=='y' :
    name = input('Enter the name of the person you would like to invite :\n')
    print(name, 'has now been invited')
    count= count + 1
    again = input('Do you want to invite someone else ?')
print('You have', count, 'people coming to your party')

#49
compnum= 50 
guess= int(input('Can you guess the number I am thinking of ?'))
count=1 
while guess!= compnum:
    if guess < compnum :
        print('Too low')
    else :
        print('Too high')
    count= count + 1
    guess= int(input('Have another guess :\n'))
print('Well done, you took', count, 'attempts')

#50
num= int(input('Enter a number between 10 and 20 : \n'))
while num<10 or num > 20 :
    if num<10 :
        print('Too low')
    else:
        print('Too high')
        num= int(input('Try again : \n'))

print('Thank you !')

#51
num= 10
while num>0 :
    print('There are', num, 'green bottles hanging on the wall.')
    print(num, 'green bottles hanging on the wall.')
    print('And if 1 green botlle should accidentally fall,')
    num = num - 1
    answer = int(input('How many green bottlles will be hanging on the wall ?'))
    if answer==num :
        print('There will be', num, 'green bottles hanging on the wall')
    else:
        while answer != num:
            answer= int(input('No, try again !'))

print('There are no more green bottles hanging on the wall')
