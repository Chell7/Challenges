#CHALLENGES 1-11
#1
name = input('Enter your first name')
print('Hello',name)

#2
name = input('Enter your first name')
name1 = input('Enter your surname')
print('Hello',name, name1)

#3
print('What do you call a bear with no teeth ?\n A gummy bear !')

#4
num1 = int(input('Enter the first number'))
num2 = int(input('Enter the second number'))
answer= num1+num2
print('The answer is', answer)

#5
num1 = int(input('Enter the first number'))
num2 = int(input('Enter the second number'))
num3 = int(input('Enter the third number'))
answer= (num1+num2)*num3
print('The answer is', answer)

#6
totalparts= int(input('Enter the first number'))
partseaten= int(input('Enter the second number'))
partsleft= totalparts-partseaten
print('The parts of pizza left are', partsleft)

#7
name= input('What is your name ?')
age= int(input('How old are you?'))
newage= age + 1
print (name, ', next birthday you will be', newage)

#8
bill= int(input('Enter the amount of the bill'))
diners= int(input('Enter the quantity of persons'))
billunity= bill/diners
print('Each person must pay', billunity )

#9
numberofdays= int(input('Enter the quantity of days'))
hours= numberofdays *24
minutes= hours*60
seconds= minutes*60
print('In days : \n','There are', hours, 'hours ;' , minutes,'minutes ;',  seconds ,'seconds .')

#1o
kg= int(input('Enter the weight in kilogram: '))
pounds= 2.204*kg
print('The result is', pounds, 'pounds')

#11
num1=int(input('Enter a number over 100 : '))
num2=int(input('Enter a number under 100 : '))
answer= num1//num2
print('The smaller number goes into the larger number', answer, 'times.')

#CHALLENGES 12-29

#Notinchallenges
# # num= int(input('Enter a number :'))
# # if num >= 10:
# #     if num <= 20:
# #         print('This is between 10 and 20')
# #     else:
# #         print('This is over 20')
# # else:
# #     print('This is under 10')


# text = str.lower('Love is enough')
# print (text)
#Notinchallenges

# num1= int(input('Enter the first number :'))
# num2= int(input('Enter the second number :'))
# if num1>num2 :
#     print(num2, num1)
# else :
#     print(num1,num2)

# num1= int(input('Enter a value under 20 :'))
# if num1>=20 :
#     print('Too high')
# else :
#     print('Thank you')

# num1= int(input('Enter a value between 10 and 20 :'))
# if 10<=num1<=20 :
#     print('Thank you')
# else :
#     print('Incorrect answer')

# color= (input('Type in your favorite color'))
# if color=='red' or color=='RED' or color=='Red':
#     print ('I like red too !')
# else :
#     print ('I don’t like', color, ',I prefer red')

# rain= input('Is it raining ?')
# rain=str.lower(rain)
# if rain=='yes':
#     windy=input('Is it windy?')
#     windy= str.lower(windy)
#     if windy=='yes':
#         print ('It is too windy to take an umbrella !')
#     else:
#         print ('Take an umbrella')
# else : 
#     print('Enjoy your day !')

# age= int(input('How old are you?'))
# if age>=18 :
#     print('You can vote ')
# elif age==17:
#     print ('You can learn to drive')
# elif age==16 :
#     print('You can buy a lottery ticket')
# elif age<16 :
#     print ('You can go Trick or Treating')

# num=int(input('Enter a number :'))
# if num<10 :
#     print('Too low')
# elif 10<=num<=20 :
#     print('Correct')
# else :
#     print('Too high')

# num=int(input('Enter 1, 2 or 3 :'))
# if num==1 :
#     print('Thank you')
# elif num==2 :
#     print('Well done')
# elif num==3 :
#     print('Correct')
# else:
#     print('Error')

# print('Don\'t cry baby !')

# name=input('Type your surname :')
# num=input('Enter a number :')
# ID= name + num
# print(ID)

# word=('lory has a boyfriend.')
# print(word.upper())

# text="Hello world !"
# # print(text.strip(''))

# print ('Hello World' [7])

# name= input('Enter your first name')
# length= len(name)
# print(length)

# name1= input('Enter your first name ')
# name2= input('Enter your last name')
# fullname= name1 + ' ' + name2
# print(fullname, len(fullname))

# name1= input('Enter your first name in lower case')
# name2= input('Enter your last name in lower case')
# name1= name1.title()
# name2= name2.title()
# fullname= name1 + ' ' + name2
# # print(fullname)

# phrase= input('Enter the first line of a nursery rhyme :')
# lenght= len(phrase)
# print('This has', lenght,'letters in it')
# start=int(input('Enter a starting number'))
# end= int(input('Enter an end number'))
# part=(phrase[start : end])
# print(part)

# grandma= input('Enter your grandma\'name')
# print(len(grandma), grandma[2:5])

# word=input('Type in a word :')
# word.upper()
# print(word)

#25
# name= input('Enter your first name')
# if len(name)<5 :
#     surname = input('Enter your surname')
#     fullname= name+surname   
#     print(fullname.upper())
# elif len(name) >=5 :
#     print (name.lower())

#26
# #Pig Latin
# word= input('Enter a word:')
# first=word[0]
# lenght=len(word)
# rest=word[1:lenght]
# if first !='a' and first !='A' and first !='e' and first !='i' and first !='o' and first !='u':
#     newword= rest+ first+ 'ay'
# else :
#     newword= word+ 'way'
# print(newword.lower())

#Challenges 27-34
# import math

# num=float(input('Enter a number'))
# print(round(num,2))

# print(math.sqrt(18))

# print(math.pi)

# num=float(input('Enter a number with a lot of decimals :'))
# pro= num*2
# print(pro)

# print(round(pro,2))

# import math
# num=int(input('Enter a number over 500 :'))
# sqrt= math.sqrt(num)
# print (round(sqrt,2))

#import math
# print(round(math.pi, 5))

#import math
# radius= int(input('Enter the radius of a circle :'))
# area= math.pi*radius**2
# print(area)

#import math
# radius= int(input('Enter the radius of a cylinder :'))
# depth= int(input('Enter the depth of a cylinder :'))
# circlearea= math.pi * radius**2
# volume= circlearea*depth
# print(round(volume,3))

#import math
# num1= int(input('Enter the first number :'))
# num2= int(input('Enter the second number :'))
# div= num1//num2
# remain= num1%num2
# print( num1, ' divided by', num2, 'is', div, 'with', remain, 'remaining ')

#import math
# x= int(input( ' 1) Square \n 2) Triangle \n \n Enter a number:' ))
# print(x)
# if x==1 :
#     side= int(input('Enter the lenght of one side :'))
#     area1= side*side
#     print('The area of your chosen shape is', area1)
# elif x==2:
#     base= int(input('Enter the base :'))
#     height= int(input('Enter the height :'))
#     area2= (base*height)/2
#     print('The area of your chosen shape is', area2) 
# else:
#     print('Incorrect option selected')


#Challenges 35-44
#35
# name= input('Enter your name : \n')
# for i in range (0,3) :
#     print(name)

#36
# name= input('Enter your name : \n')
# number=int(input('Enter a number : \n'))
# for i in range (0,number) :
#     print(name)

#37
# name= input('Enter your name : \n')
# for i in name :
#     print(i)

#38
# name= input('Enter your name : \n')
# number=int(input('Enter a number : \n'))
# for x in range(0,number):
#     for i in name:
#         print(i)

#39
# number= int(input('Enter a number between 1 and 12 : \n'))
# for i in range(1,13) :
#     answer= i* number
#     print(i, 'x', number,'=', answer)

#40
# number= int(input('Enter a number below 50 :\n'))
# for i in range (50, number-1, -1) :
#     print(i)

#41
# name=input('Enter your name :\n')
# number= input('Enter a number less than 10 :\n')
# if number < 10:
#     for i in range(0,number):
#         print(name)
# else:
#     for i in range(0,3) :
#         print('Too high')

#42
# total=0
# for i in range(0,5) :
#     number =int(input('Enter the number'))
#     ask=input('Do you want that number included ?')
#     if ask=='yes':
#         total= total + number
# print(total)

#43
# ask= input('What direction do you want to count?')
# if ask=='up':
#     number=int(input('Enter the top number : \n'))
#     for i in range(1, number +1) :
#         print(i)
# elif ask=='down':
#     number=int(input('Enter a number below 20 :\n'))
#     for i in range (20, number -1, -1) :
#         print(i)
# else:
#     print('I do not understand !')

#44
# pers=int(input('How many persons do you want to invite to the party ?'))
# if pers<10:
#     for i in range(0,pers) :
#         name=input('Enter a name')
#         print(name, 'has been invited')
# elif pers>=10 :
    # print('Too many people')

#Challenges 45-51
#45
# total=0 
# while total <=50 :
#     num=int(input('Enter a number :\n'))
#     total= total+ num
#     print('The total is', total)

#46
# num=0
# while num<= 5:
#     num=int(input('Enter a number \n'))
# print('The last number you entered was a', num)

# #47
# num1=int(input('Enter the first number :\n'))
# total=num1
# again='y'
# while again=='y' :
#       num2=int(input('Enter another number :\n')) 
#       total = total + num2
#       again= input('Do you want to add another number ? (y/n')
# print('The total is', total)

#48 
# again='y'
# count= 0
# while again=='y' :
#     name = input('Enter the name of the person you would like to invite :\n')
#     print(name, 'has now been invited')
#     count= count + 1
#     again = input('Do you want to invite someone else ?')
# print('You have', count, 'people coming to your party')

# #49
# compnum= 50 
# guess= int(input('Can you guess the number I am thinking of ?'))
# count=1 
# while guess!= compnum:
#     if guess < compnum :
#         print('Too low')
#     else :
#         print('Too high')
#     count= count + 1
#     guess= int(input('Have another guess :\n'))
# print('Well done, you took', count, 'attempts')

# #50
# num= int(input('Enter a number between 10 and 20 : \n'))
# while num<10 or num > 20 :
#     if num<10 :
#         print('Too low')
#     else:
#         print('Too high')
#         num= int(input('Try again : \n'))

# print('Thank you !')

#51
# num= 10
# while num>0 :
#     print('There are', num, 'green bottles hanging on the wall.')
#     print(num, 'green bottles hanging on the wall.')
#     print('And if 1 green botlle should accidentally fall,')
#     num = num - 1
#     answer = int(input('How many green bottlles will be hanging on the wall ?'))
#     if answer==num :
#         print('There will be', num, 'green bottles hanging on the wall')
#     else:
#         while answer != num:
#             answer= int(input('No, try again !'))

# print('There are no more green bottles hanging on the wall')

#Challenges 52-59 
# #52
# import random
# num=  random.randint(1,100)
# print (num)

# #53
# import random
# fruits=random.choice(['Watermelon', 'Strawberry', 'Cherry', 'Orange', 'Pineapple'])
# print(fruits)

# #54
# import random
# ask= input('Make a choice : h or t')
# choose=random.choice(['h', 't'])
# if ask==choose :
#     print('You win')
# else :
#     print('Bad luck')
#     print('The computer has selected', choose)

#55
# import random
# ask= int(input('Enter a number between one and five :'))
# choose= random.randint(1,5)
# if ask==choose :
#     print('Well done !')
# elif ask > choose :
#     print('The number you have chosen is too high !')
#     ask= int(input('Enter a number between one and five :'))
#     if ask==choose :
#         print('Correct !')
#     else :
#         print('You lose !')
# elif ask < choose :
#     print('The number you have chosen is too low !')
#     ask= int(input('Enter a number between one and five :'))
#     if ask==choose :
#         print('Correct !')
#     else :
#         print('You lose !')


#56
# import random
# ask=int(input('Enter a number between one and ten '))
# num=random.randint(1,10)
# while ask != random :
#     ask=int(input('Enter a number between one and ten '))

#57
# import random
# ask=int(input('Enter a number between one and ten '))
# num=random.randint(1,10)
# if ask > random :
#     print('The number you have chosen is too high !')
#     ask=int(input('Enter a number between one and ten '))
# elif ask < random :
#     print('The number you have chosen is too low !')
#     ask=int(input('Enter a number between one and ten '))

#58 
# import random
# score=0
# for i in range (1,6) :
#     num1 = random.randint(1,50)
#     num2= random.randint(1,50)
#     correct= num1+num2
#     print(num1, '+', num2,'=')
#     answer= int(input('Your answer :'))
#     print()
#     if correct==answer : 
#         score = score + 1

# print('You scored', score, 'out of 5')
        
#59
# import random 
# print('Select from red, blue, green, white, black ')
# color= random.choice(['Red', 'Blue', 'Yellow', 'White', 'Black'])  
# ask= input('Choose a color :')
# tryagain= True
# while tryagain== True :
#     theirchoice= input('Enter a color :')
#     theirchoice= theirchoice.lower()
#     if color== theirchoice :
#         print('Well done')
#         tryagain= False
#     else :
#         if color=='red' :
#             print('I bet you are seeing RED right now')
#         elif color =='blue' :
#             print ('Do not feel BLUE')
#         elif color =='green' :
#             print(' I bet you are GREEN with envy right now')
#         elif color == 'white' :
#             print('Are you WHITE as a sheet, as you did not guess correctly ? ')
#         elif color == 'pink' :
#             print('Shame you are not feeling in the PINK, as you got it  wrong')

#Challenges 60-68
#60
# import turtle 
# for i in range (4) :
#     turtle.forward(100)
#     turtle.left(90)

# turtle.exitonclick()

#61
# import turtle 
# for i in range(3) :
#     turtle.left(120)
#     turtle.forward(100)

# turtle.exitonclick()

#62
# import turtle 
# for i in range(360) :
#         turtle.forward(1)
#         turtle.right(1)

# turtle.exitonclick()

#63
# import turtle 
# turtle.color('green')
# turtle.begin_fill()
# for i in range (4) :
#     turtle.forward(100)
#     turtle.left(90)
# turtle.penup()
# turtle.end_fill()
# turtle.forward(100)
    
# turtle.pendown
# turtle.color('yellow')
# turtle.begin_fill()
# for i in range (4) :
#     turtle.forward(100)
#     turtle.left(90)
# turtle.penup()
# turtle.end_fill()
# turtle.forward(100)

# turtle.pendown
# turtle.color('black')
# turtle.begin_fill()
# for i in range (4) :
#     turtle.forward(100)
#     turtle.left(90)
# turtle.end_fill()

# turtle.exitonclick()

# #64
# import turtle 
# for i in range (5) :
#     turtle.forward(100)
#     turtle.right(144)

# turtle.exitonclick()

#65
# import turtle

# turtle.left(90)
# turtle.forward(100)
# turtle.right(90)
# turtle.penup()
# turtle.forward(50)
# turtle.pendown()
# turtle.forward(75)
# turtle.right(90)
# turtle.forward(50)
# turtle.right(90)
# turtle.forward(75)
# turtle.left(90)
# turtle.forward(50)
# turtle.left(90)
# turtle.forward(75)
# turtle.penup()
# turtle.forward(50)
# turtle.pendown()
# turtle.forward(75)
# turtle.left(90)
# turtle.forward(50)
# turtle.left(90)
# turtle.forward(45)
# turtle.left(180)
# turtle.forward(45)
# turtle.left(90)
# turtle.forward(50)
# turtle.left(90)
# turtle.forward(75)

# turtle.hideturtle()

# turtle.exitonclick()

#66
# import turtle
# import random

# turtle.pensize(4)

# for i in range (0,8) :
#     turtle.color(random.choice(['red','orange','green', 'blue', 'black', 'pink']))
#     turtle.forward(50)
#     turtle.right(45)

# turtle.exitonclick()

#67
# import random
# import turtle

# for x in range (0,10) :
#     for i in range (0, 8) :
#         turtle.forward(50)
#         turtle.right(45)
#     turtle.right(36)

# turtle.hideturtle()

# turtle.exitonclick()

#68
# import turtle
# import random

# lines= random.randint(5,20)

# for y in range (0,lines) :
#     length = random.randint(25, 100)
#     rotate= random.randint(1,365)
#     turtle.forward(length)
#     turtle.right(rotate)

# turtle.exitonclick

#Challenges 69-79
#69
#challenge 069
# country_tuple = ("France", "England", "Spain", "Germany", "Australia")
# print(country_tuple)
# print()
# country = input("Please enter one of the countries from above: ")
# print(country, "has index number", country_tuple.index(country))

# #challenge 070
# country_tuple = ("France", "England", "Spain", "Germany", "Australia")
# print(country_tuple)
# print()
# country = input("Please enter one of the countries from above: ")
# print(country, "has index number", country_tuple.index(country))
# print()
# num = int(input("Enter a number betwen 0 and 4: "))
# print(country_tuple[num])

# #challenge 071
# sports_list =["tennis","football"]
# sports_list.append(input("what is your favorite sport? "))
# sports_list.sort()
# print(sports_list)

# #challenge 072
# subject_list = ["maths", "english", "computing", "history", "science", "spanish"]
# print(subject_list)
# dislike = input("Which of these subjects do you dislike? ")
# getrid = subject_list.index(dislike)
# del subject_list(getrid)
# print(subject_list)

# #challenge 073
# food_dictionary = {}
# food1 = input("Enter a food you like: ")
# food_dictionary[1] = food1
# food2 = input("Enter another food you like: ")
# food_dictionary[2] = food2
# food3 = input("Enter third food you like: ")
# food_dictionary[3] = food3
# food4 = input("Enter one last food you like: ")
# food_dictionary[4] = food4
# print(food_dictionary)
# dislike = int(input("Which of these do you want to get rid of? "))
# del food_dictionary[dislike]
# print (sorted(food_dictionary.values()))

# #challenge 074
# colours = ["red", "blue", "green", "black", "white", "pink", "grey", "purple", "yellow", "brown"]
# start = int(input("Enter a starting number (0-4): "))
# end = int(input("Enter an end number (5-9): "))
# print(colours[start:end])

# #challenge 075
# nums = [123, 345, 234, 765]
# for i in nums:
#     print(i)
# selection = int(input("Enter a number from the list: "))
# if selection in nums:
#     print(selection, "is in position", nums.index(selection))
# else:
#     print("That is not in the list")
    
# #challenge 076
# name1 = input("Enter a name of somebody you want to invite to your party: ")
# name2 = input("Enter a another name: ")
# name3 = input("Enter a third name: ")
# party = [name1, name2, name3]
# another = input("Do you want to invite another (y/n): ")
# while another == "y":
#     newname = party.append(input("Enter another name: )"))
#     another = input("Do you want to invite another (y/n): ")
# print("You have", len(party), "people coming to your party")

# #challenge 077
# name1 = input("Enter a name of somebody you want to invite to your party: ")
# name2 = input("Enter a another name: ")
# name3 = input("Enter a third name: ")
# party = [name1, name2, name3]
# another = input("Do you want to invite another (y/n): ")
# while another == "y":
#     newname = party.append(input("Enter another name: )"))
#     another = input("Do you want to invite another (y/n): ")
# print("You have", len(party), "people coming to your party")
# print(party)

# #challenge 078
# tv = ["Task Master", "Top grear", "The Big Bang Theory", "How I Met Your Mother"]
# for i in tv:
#     print(i)
# print()
# newtv = input("Enter another TV show: ")
# position = int(input("Enter a number between 0 and 3: "))
# tv.insert(position,newtv)
# for i in tv:
#     print(1)
    
# #challenge 079
# nums = []
# count = 0
# while count <3:
#     num = int(input("Enter a number: "))
#     nums.append(num)
#     print(nums)
#     count = count + 1
# lastnum = input("Do you want the last number saved (y/n): ")
# if lastnum == "n":
#     nums.remove(num)
# print(nums)

# # challenge 080
# fname = input("Enter your first name: ")
# print("That has", len(fname), "characters in it")
# sname = input("Enter your surname: ")
# print("That has", len(sname), "characters in it")
# name = fname + " " + sname
# print("Your full name is", name)
# print("That has", len(name), "characters in it")

# #challenge 081
# subject = input("Enter your favourite school subject: ")
# for letter in subject:
#     print(letter, end = "-")
    
# #challenge 082
# poem = "Oh, I wish I'd looked after me teeth, "
# print (poem)
# start = int(input("Enter a starting number: "))
# end = int(input("Enter a ending number: "))
# print(poem[start:end])

# #challenge 083
# msg = input("Enter a message in uppercase: ")
# tryagain = False
# while tryagain == False:
#     if msg.isupper():
#         print("Thank you")
#         tryagain = True
#     else:
#         print("Try again")
#         msg = input("Enter a message in uppercase: ")
        
# #challenge 084
# postcode = input("Enter your postcode: ")
# start = postcode[0:2]
# print(start.upper())

# #challenge 085
# name = input("Enter your name: ")
# count = 0
# name = name.lower()
# for x in name:
#     if x == "a" or x == "e" or x == "i" or x == "o" or x == "u":
#         count = count + 1
# print("Vowels =", count)

# #challenge 086
# pswd1 = input("Enter a password: ")
# pswd2 = input("Enter it again: ")
# if pswd1 == pswd2:
#     print("Thank you")
# elif pswd1.lower() == pswd2.lower():
#     print("They must be the same case")
# else:
#     print("Incorrect")
    
# #challenge 087
# word = input("Enter a word: ")
# length = len(word)
# num = 1 
# for x in word:
#     position = length - num
#     letter = word[position]
#     print(letter)
#     num = num + 1

# #challenge 088
# from array import *
# nums = array ('i', [])
# for i in range (0,5):
#     num = int(input("Enter a number: "))
#     nums.append(num)
# nums = sorted(nums)
# nums.reverse()
# print(nums)

# #challenge 089
# from array import *
# import random
# nums = array('i', [])
# for i in range (0,5):
#     num = random.randint(1,100)
#     nums.append(num)
# for i in nums:
#     print(i)
    
# #challenge 090
# from array import *
# nums = array('i', [])
# while len(nums) < 5:
#     num = int(input("Enter a number between 10 and 20: "))
#     if num >= 10 and num <= 20:
#         nums.append(num)
#     else:
#         print("Outside the range")
# for i in nums:
#     print(i)
    
# #challenge 091
# from array import *
# nums = array('i', [5, 7, 9, 2, 9])
# for i in nums:
#     print(i)
#     num = int(input("Enter a number: "))
# if nums.count(num) == 1 :
#     print (num, "is in the list once")
# else:
#     print(num, "is in the list", nums.count(num), "times")
    

# #challenge 092
# from array import *
# import random
# num1 = array ('i', [])
# num2 = array ('i', [])
# for i in range (0, 3):
#     num = int(input("Enter a number: "))
#     num1.append(num)
# for i in range (0, 5):
#     num = random.randint(1,100)
#     num2.append(num)
# num1.extend(num2)
# num1 = sorted(num1)
# for i in num1:
#     print(i)
    
# #challenge 093
# from array import *
# nums = array ('i', [])
# for i in range(0,5):
#     num = int(input("Enter a number: "))
#     nums.append(num)
    
# nums = sorted(nums)
# for i in nums:
#     print(i)
    
# num = int(input("Select a number from the array: "))
# if num in nums:
#     num.remove(num)
#     num2 = array('i', [])
#     num2.append(num)
#     print(nums)
#     print(num2)
# else:
#     print("That is not a value in the array")
    
# #challenge 094
# from array import *
# nums = array ('i', [4, 6, 8, 2, 5])
# for i in nums:
#     print(i)
# num = int(input("Select one of the numbers: "))
# tryagain = True
# while tryagain == True:
#     if num in nums:
#         print ("This is in position", num.index(num))
#         tryagain = False
#     else:
#         print("Not in array")
#         num = int(input("Select one of the numbers: "))
        
# #challenge 095
# from array import *
# import math
# nums = array('f',[34, 75, 27, 23, 99, 58, 45, 26, 28, 65])
# tryagain = True
# while tryagain == True:
#     num = int(input("Enter a number between 2 and 5: "))
#     if num<2 or num>5:
#         print("Incorrect value, try again.")
#     else:
#         tryagain = False
# for i in range (0,5):
#     ans = nums[1]/num
#     print(round(ans, 2))

# #challenge 096
# list = [[2, 5, 8], [3, 7, 4], [1, 6, 9], [4, 2, 0]]

# #challenge 097
# list = [[2, 5, 8], [3, 7, 4], [1, 6, 9], [4, 2, 0]]
# row = int(input("Select a row: "))
# col = int(input("Select a column: "))
# print(list[row] [col])

# #challenge 098
# list = [[2, 5, 8], [3, 7, 4], [1, 6, 9], [4, 2, 0]]
# row = int(input("Select a row: "))
# print(list[row])
# newvalue = int(input("Enter a new number: "))
# list[row].append(newvalue)
# print(list[row])

# #challenge 099
# list = [[2, 5, 8], [3, 7, 4], [1, 6, 9], [4, 2, 0]]
# row = int(input("Select a row: "))
# print(list[row])
# col = int(input("Select a column: "))
# print(list[row] [col])
# change = input("Do you want to change the value? y/n ")
# if change == "y":
#     newvalue = int(input("Enter new value: "))
#     list[row] [col] = newvalue
# print(list[row])

# #challenge 100
# sales = {"John":{"N":3056, "S":8463, "E":8441, "W":2694},
# "Tom":{"N":4832, "S":6786, "E":4737, "W":3612},
# "Anne":{"N":5239, "S":4802, "E":5820, "W":1859},
# "Fiona":{"N":3904, "S":3645, "E":8821, "W":2451}}

# #challenge 101
# sales = {"John":{"N":3056, "S":8463, "E":8441, "W":2694},
# "Tom":{"N":4832, "S":6786, "E":4737, "W":3612},
# "Anne":{"N":5239, "S":4802, "E":5820, "W":1859},
# "Fiona":{"N":3904, "S":3645, "E":8821, "W":2451}}
# person = input("Enter sales person's name")
# region = input("Select region: ")
# print(sales[person][region])
# newdata = int(input("Enter new data: "))
# sales[person] [region] = newdata
# print(sales[person])

# #challenge 102
# list = []
# for i in range (0, 4):
#     name = input("Enter name: ")
#     age = int(input("Enter age"))
#     shoe = int(input("Enter shoe size: "))
#     list[name]= {"Age":age,  "Shoe size":shoe}
    
# ask = input("Enter a name: ")
# print(list[ask])

# #challenge 103
# list = []
# for i in range (0, 4):
#     name = input("Enter name: ")
#     age = int(input("Enter age"))
#     shoe = int(input("Enter shoe size: "))
#     list[name]= {"Age":age,  "Shoe size":shoe}
    
# for name in list:
#     print((name), list[name] ["Age"])
    

# #challenge 104
# list = []
# for i in range (0, 4):
#     name = input("Enter name: ")
#     age = int(input("Enter age"))
#     shoe = int(input("Enter shoe size: "))
#     list[name]= {"Age":age,  "Shoe size":shoe}  
# getrid = input("Who do you want to remove from the list? ")
# del list[getrid]
# for name in list:
#     print((name), list[name] ["Age"],list[name] ["Shoe size"])
# #challenge 105
# file = open("Numbers.txt", "w")
# file.write("4, ")
# file.write("6, ")
# file.write("10, ")
# file.write("8, ")
# file.write("5, ")
# file.close()

# #challenge 106
# file = open("Names.txt", "w")
# file.write("Bob\n")
# file.write("Tom\n")
# file.write("Gemma\n")
# file.write("Sarah\n")
# file.write("Timothy\n")
# file.close()

# #challenge 107
# file = open("Names.txt", "W")
# print(file.read())
# file.close()

# #challenge 108
# file = open("Names.txt", "a")
# newname = input("Enter a new name")
# file.write(newname + "\n")
# file.close

# #challenge 109
# print("1) Create a new file")
# print("2) Display the file")
# print("3) Add a new item to the file")
# selection = int(input("Make a selection 1, 2 or 3: "))
# if selection == 1:
#     subject = input("Enter a school subject: ")
#     file = open("Subject.txt", "w")
#     file.write(subject + "\n")
#     file.close()
# elif selection == 2:
#     file = open("Subject.txt", "r")
#     print(file.read())
# elif selection == 3:
#     file = open("Subject.txt", "a")
#     subject = input("Enter a school subject: ")
#     file.write(subject + "\n")
#     file.close()
#     file = open("Subject.txt","r")
#     print(file.read())
# else:
#     print("Invalid option")
    
# #challenge 110
# file = open("Names.txt", "r")
# print(file.read())
# file.close()

# file = open("Names.txt", "r")
# selectedname = input("Enter a name from the list: ")
# selectedname = selectedname + "\n"
# for row in file:
#     if row != selectedname:
#         file = open("Names2.txt", "a")
#         newrecord = row
#         file.write(newrecord)
#         file.close()
# file.close()
    
    
# #challenge 111
# import csv

# file = open("Books.csv","w")
# newrecord = "To Kill A Mockingbird, Harper Lee, 1960\n"
# file.write(str(newrecord))
# newrecord = "A Brief History of time, Stephen Hawking, 1988\n"
# file.write(str(newrecord))
# newrecord = "The Great Gatsby, F. Scott Fritzgerald, 1922\n"
# file.write(str(newrecord))
# newrecord = "The Man Who Mistook His Wife for a Hat, Oliver Sacks, 1985\n"
# file.write(str(newrecord))
# newrecord = "Pride and Prejudice, Jane Austen, 1813\n"
# file.write(str(newrecord))
# file.close()

# #challenge 112
# import csv
# file = open("Books.csv","a")
# title = input("Enter a title: ")
# author = input("Enter author: ")
# year = input("Enter the year it was released: ")
# newrecord = title + "," + author + "," + year + "\n"
# file.write(str(newrecord))
# file.close()

# file = open("Books.csv","r")
# for row in file:
#     print(row)
# file.close()

# #challenge 113
# import csv
# num = int(input("How many books do you want to add to the list? "))
# file = open("Books.csv","a")
# for x in range (0, num):
#     title = input("Enter a title: ")
#     author = input("Enter author: ")
#     year = input("Enter the year it was released: ")
#     newrecord = title + "," + author + "," + year + "\n"
#     file.write(str(newrecord))
# file.close()

# searchauthor = input("Enter an authors name to search for: ")

# file = open("Books.csv","r")
# count = 0
# for row in file:
#     if searchauthor in str(row):
#         print(row)
#         count = count + 1
# if count == 0:
#     print("There are no books by that author in this list.")
# file.close()

# #challenge 114
# import csv

# start = int(input("Enter a starting year: "))
# end = int(input("Enter an end year: "))

# file = list(csv.reader(open("Books.csv")))
# tmp = []
# for row in file:
#     tmp.append(row)
    
# x = 0
# for row in tmp:
#     if int(tmp[x][2]) >= start and int(tmp[x][2]) <=end:
#         print(tmp[x])
#     x = x+1
    
# #challenge 115
# import csv

# file = open("Books.csv","r")
# x = 0
# for row in file:
#     display = "Row " + str(x) + " - " + row
#     print(display)
#     x = x + 1
    
# #challenge 116
# import csv

# file = list(csv.reader(open("Books.csv")))
# Booklist = []
# for row in file:
#     Booklist.append(row)
    
# x = 0
# for row in Booklist:
#     display = x,Booklist[x]
#     print(display)
#     x = x + 1
# getrid = int(input("Enter a row number to delete: "))
# del Booklist[getrid]

# x = 0
# for row in Booklist:
#     display = x,Booklist[x]
#     print(display)
#     x = x + 1
# alter = int(input("Enter a row number to alter: "))
# x = 0
# for row in Booklist[alter]:
#     display = x, Booklist[alter][x]
#     print(display)
#     x = x + 1
# part = int(input("which part do you want to change? "))
# newdata = input("Enter new data: ")
# Booklist[alter][part] = newdata
# print(Booklist[alter])

# file = open("Books.csv", "w")
# x = 0
# for row in Booklist:
#     newrecord = Booklist[x][0]+ ", " + Booklist[x][1]+ ", " + Booklist[x][2] + "\n"
#     file.write(newrecord)
#     x = x+1
# file.close()

# #challenge 117
# import csv
# import random

# score = 0
# name = input("What is your name: ")
# q1_num1 = random.randint(10,50)
# q1_num2 = random.randint(10,50)
# question1 = str(q1_num1) + "+" + str(q1_num2) + "_"
# ans1 = int(input(question1))
# realans1 = q1_num2 + q1_num2
# if ans1 == realans1:
#     score = score + 1 
# q2_num1 = random.randint(10,50)
# q2_num2 = random.randint(10,50)
# question2 = str(q2_num1) + "+" + str(q2_num2) + "_"
# ans2 = int(input(question2))
# realans2 = q2_num2 + q2_num2
# if ans2 == realans2:
#     score = score + 1 

# file = open("QuizScore.csv", "a")
# newrecord = name + ","+ question1 + "," + question2 + "," + str(ans2) + str(score)+"\n"
# file.write(str(newrecord))
# file.close()

# #challenge 118

# def ask_value(): 
#     num= int (input ("Enter a number: ")) 
#     return num

# def count (num):
#     n = 1
#     while n <= num: 
#         print (n) 
#         n = n + 1

# def main ():
#     num = ask_value ()
#     count (num)

# main ()

# #challenge 119

# import random

# def pick_num():
#     low = int (input ("Enter the bottom of the range: ")) 
#     high = int (input ("Enter the top of the range: ")) 
#     comp_num= random.randint (low, high)
#     return comp_num

# def first_guess ():
#     print ("I am thinking of a number...") 
#     guess = int (input ("What am I thinking of: ")) 
#     return guess

# def check_answer (comp_num, guess) :
#     try_again = True 
#     while try_again == True:
#         if comp_num == guess: 
#             print ("Correct, you win.")
#             try_again = False
#         elif comp_num > guess:
#             guess = int (input ("Too low, try again: "))
#         else:
#             guess = int (input ("Too high, try again: "))

# def main ():
#     comp_num = pick_num()
#     guess = first_guess () 
#     check_answer (comp_num, guess)

# main ()

# #challenge 120
# import random

# def addition ():
#     num1 = random.randint (5,20) 
#     num2 = random.randint (5,20)
#     print (num1, "+", num2, "= ")
#     user_answer = int(input("Your answer: "))
#     actual_answer = num1 + num2
#     answers = (user_answer, actual_answer)
#     return answers


# def subtraction ():
#     num3 = random.randint (25,50)
#     num4 = random.randint (1,25)
#     print (num3, "-",num4,"= ")
#     user_answer = int(input("Your answer: "))
#     actual_answer = num3 -  num4
#     answers = (user_answer, actual_answer)
#     return answers

# def check_answer(user_answer, actual_answer):
#     if user_answer == actual_answer:
#         print ("Correct")
#     else:
#         print ("Incorrect, the answer is", actual_answer)

# def main ():
#     print ("1) Addition")
#     print ("2) Subtraction")
#     selection = int(input("Enter 1 or 2: "))
#     if selection == 1:
#         user_answer, actual_answer = addition ()
#         check_answer(user_answer, actual_answer)
#     elif selection == 2:
#         user_answer, actual_answer = subtraction ()
#         check_answer(user_answer, actual_answer)
#     else:
#         print("Incorrect selection")

# main ()

# #challenge 121

# def add_name ():
#     name = input("Enter a new name: ")
#     name.append(name)
#     return name

# def change_name () :
#     num = 0
#     for x in num:
#         print (num, x)
#         num = num + 1
#     select_num = int (input ("Enter the number of the name you want to change: "))
#     name = input ("Enter new name: ")
#     names = [select_num] = name
#     return names

# def delete_name ():
#     num = 0
#     for x in name:
#        print (num, x)
#     num = num + 1
#     select_num = int (input ("Enter the number of the name you want to delete: "))
#     del names [select_num]
#     return names

# def view_names ():
#     for x in names:
#         print (x)
# print ()

# def main():
#     again = "y"
#     while again == "y":
#         print ("1) Add a name")
#         print ("2) Change a name")
#         print ("3) Delete a name")
#         print ("4) View namea")
#         print ("5) Quit")
#         selection = int(input ("What do you want to do? "))
#         if selection == 1:
#             names = add_name ()
#         elif selection == 2:
#             names = change_name ()
#         elif selection == 3:
#             names = delete_name()
#         elif selection == 4:
#             names = view_names ()
#         elif selection == 5:
#             again = "n"
#         else:
#             print("Incorrect option: ")
#             data = (names, again)

# names = []

# main ()

# #challenge 122
# import csv

# def addtofile():
#     file = open("Salaries.csv","a") 
#     name = input ("Enter name: ")
#     salary = int (input ("Enter salary: ")) 
#     newrecord = name + ", " + str(salary) + "\n"
#     file.write(str (newrecord))
#     file.close()

# def viewrecords ():
#     file = open("Salaries.csv","r")
#     for row in file:
#         print (row)
#     file.close()

# tryagain = True

# while tryagain == True:
#     print ("I) Add to file")
#     print ("2) View all records")
#     print ("3) Quit program")
#     print ()
#     selection = input ("Enter the number of your selection: ")
#     if selection == "1":
#         addtofile()
#     elif selection == "2":
#         viewrecords ()
#     elif selection == "3":
#         tryagain = False
#     else:
#         print ("Incorrect option")

# #challenge 123

# import csv

# def addtofile():
#     file = open("Salaries.csv","a")
#     name = input ("Enter name: ")
#     salary = int (input ("Enter salary: ")) 
#     newrecord = name + ", " + str(salary) + "\n"
#     file.write (str (newrecord)) 
#     file.close()

# def viewrecords ():
#     file = open("Salaries.csv", "r")
#     for row in file:
#         print(row)
#     file.close()

# def deleterecord ():
#     file = open("Salaries.csv","r")
#     x = 0
#     tmplist = []
#     for row in file:
#         tmplist.append(row)
#     file.close()
#     for row in tmplist:
#         print (x, row)
#         x = x + 1
#     rowtodelete = int (input ("Enter the row number to delete: "))
#     del tmplist [rowtodelete]
#     file = open("Salaries.csv","w")
#     for row in tmplist: 
#         file.write (row)
#     file.close()

# tryagain = True
# while tryagain == True: 
#     print ("1) Add to file")
#     print ("2) View all records") 
#     print ("3) Delete a record")
#     print ("4) Quit program")
#     print()

# selection = input ("Enter the number of your selection: ")
# if selection == "1":
#     addtofile()
# elif selection == "2":
#     viewrecords ()
# elif selection == "3":
#     deleterecord ()
# elif selection == "4":
#     tryagain = False
# else:
#     print("Incorrect option")

# #challenge 124

# from tkinter import *

# def click():
#     name = textbox1.get()
#     message = str("Hello " + name)
#     textbox2 ["bg"] = "yellow"
#     textbox2 ["fg"] = "blue"
#     textbox2 ["text"]= message

# window = Tk ()
# window.geometry("500x200")

# label1 = Label(text = "Enter your name:")
# label1.place (x = 30, y=20)

# textbox1 = Entry (text = "")
# textbox1.place (x = 150, y = 20 , width = 200 , height = 25)
# textbox1 ["justify"] = "center" 
# textbox1.focus ()

# button1= Button (text = "Press me", command = click) 
# button1.place (x = 30, y=  50, width = 120, height = 25)

# textbox2 = Message(text = "")
# textbox2.place(x = 150, y = 50, width = 200, height=25)
# textbox2 ["bg"] = "white"
# textbox2 ["fg"] = "black"
# window.mainloop()

# #challenge 125

# from tkinter import * 
# import random

# def click ():
#     num = random.randint (1,6)
#     answer["text"] = num

# window = Tk () 
# window.title ("Roll a dice")
# window.geometry("100x120") 

# button1 = Button (text = "Roll", command = click)
# button1.place (x = 30, y = 30 , width = 50 , height=25) 

# answer = Message (text = "")
# answer.place (x = 40, y=70, width=30, height = 25)

# window.mainloop()

# #challenge 126

# from tkinter import *

# def add_on():
#     num = enter_txt.get() 
#     num= int(num)
#     answer = output_txt["text"]
#     answer = int(answer)
#     total = num + answer
#     output_txt["text"] = total

# def reset():
#     total = 0.
#     output_txt["text"]= 0 
#     enter_txt.delete(0, END)
#     enter_txt.focus()

# total = 0 
# num = 0

# window = Tk()
# window.title ("Adding Together")
# window.geometry("450x100")

# enter_lb1 = Label (text = "Enter a number:") 
# enter_lb1.place (x = 50, y = 20, width = 100, height = 25)

# enter_txt = Entry(text = 0) 
# enter_txt.place (x = 150, y = 20, width = 100, height = 25) 
# enter_txt["justify"] = "center"
# enter_txt. focus ()

# add_btn  = Button(text = "Add", command = add_on)
# add_btn.place (x = 300, y = 20, width = 50,  height = 25)

# output_lb1 = Label (text = "Answer = ") 
# output_lb1.place (x = 50, y = 50, width = 100,  height = 25)

# output_txt= Message (text = 0) 
# output_txt.place(x = 150, y = 50, width = 100, height = 25)
# output_txt["bg"] = "white"
# output_txt["relief"] = "sunken"

# clear_btn = Button (text = "Clear", command = reset)
# clear_btn.place ( x = 300,  y =  50, ldth = 50 , height = 25)

# window.mainloop()

# #challenge 127

# from tkinter import *

# def add_name ():
#     name = name_box.get() 
#     name_list.insert(END, name)
#     name_box.delete (0, END)
#     name_box.focus()


# def clear_list ():
#     name_list.delete (0, END) 
#     name_box.focus ()

# window = Tk ()
# window.title("Names list") 
# window.geometry("400x200")

# label1 = Label(text = "Enter a name:")
# label1.place (x = 20, y=20, width=100, height = 251 )

# name_box = Entry(text = 0)
# name_box.place(x = 120, y=20, width=100, height=25)
# name_box.focus ()

# button = Button (text = "Add to list", command = add_name) 
# button.place (x = 250, y = 20 , width = 100, height = 25)

# name_list = Listbox()
# name_list.place (x = 120, y = 50, width = 100, height=100)

# button2= Button (text = "Clear list", command = clear_list) 
# button2.place (x = 250, y=50, width = 100, height = 25 )

# window.mainloop()

# #challenge 128

# def convert1 () : #Important to review 
#     km = 10 
# def convert2():
#     km = textbox1.get()
#     km = int(km) 
#     message = km * 0.6214
#     textbox2.delete (0, END) 
#     textbox2.insert (END, message)
#     textbox2.insert (END," miles")



# window = Tk()
# window.title("Distance") 
# window.geometry("260x200")

# label1 = Label(text="Enter the value you want to convert:") 
# label1.place(x = 30, y = 20)

# textbox1 = Entry (text= "")
# textbox1.place (x = 30, y=50, width = 200, height=25) 
# textbox1["justify"] = "center"
# textbox1.focus()

# convert1 = Button(text= "Convert km miles to ", command = convert1)
# convert1.place (x = 30, y = 80 , width = 200, height = 25)



# convert2 = Button(text= "Convert in to mile", command = convert2)
# convert2.place ( x=30, y = 110 , width= 200, height = 25)

# textbox2 = Entry (text = "") 
# textbox2.place (x= 30, y =140, width = 200 , height = 25)

# textbox2["justify"]="center"

# window.mainloop()

# # Challenge 129

# from tkinter import *

# def add_number (): 
#     num = num_box.get()
#     if num.isdigit():
#         num_list.insert (END, num) 
#         num_box.delete (0, END) 
#         num_box.focus()
#     else: 
#         num_box.delete (0, END) 
#         num_box.focus()

# def clear_list (): 
#     num_list.delete (0, END)
#     num_box.focus()

# window = Tk()
# window.title ("Number list")
# window.geometry ("400x200")

# label1 = Label (text = "Enter a number:") 
# label1.place (x = 20, y = 20, width = 100 , height=25)

# num_box = Entry ( t=0) 
# num_box.place (x = 120, y=20, width = 100, height=25)
# num_box.focus ()

# button = Button(text = "Add to List", command = add_number) 
# button1.place (x = 250, y = 20, width = 100, height = 25)

# num_list = Listbox ()
# num_list.place (x = 120, y = 50, width = 100, height=100)

# button2 = Button (text = "Clear list", command = clear_list) 
# button2.place (x = 250, y = 50, width= 100, height = 25)

# window.mainloop()

# #Challenge 130

# from tkinter import *

# import csv

# def add_number ():
#     num = num_box.get()
#     if num.isdigit():
#         num_list.insert(END, num)
#         num_box.delete (0, END) 
#         num_box.focus ()
#     else:
#         num_box.delete (0, END) 
#         num_box.focus()

# def clear_list (): 
#     num_list.delete (0, END) 
#     num_box. ocus()

# def save_list():
#     file = open ("numbers.csv","w") 
#     tmp_list = num_list.get (0, END)
#     item = 0
#     for x in tmp_list:
#         newrecord = tmp_list[item] + "\n" 
#         file.write(str(newrecord)) 
#         item = item + 1
#     file.close()

# window = Tk()
# window.title ("Number list") 
# window.geometry ("400x200")

# label1 = Label (text="Enter a number:") 
# label1.place (x = 20, y = 20, width= 100, height=25)

# num_box= Entry(text = 0) 
# num_box.place (x = 120, y=20, width=100, height = 25)
# num_box.focus()

# button1 = Button (text = "Add to list", command = add_number) 
# button1.place (x = 250, y = 20 , width = 100, ght=25)

# num_list = Listbox()
# num_list.place (x = 120, y = 50 ,width = 100, height=100)

# button2 = Button (text = "Clear list", command= clear_list)
# button2.place (x = 250, y = 50, width =100, height = 25)

# button3 = Button (text = "Save list", command = save_list) 
# button3.place (x = 250, y = 80, width = 100 , height=25)

# window.mainloop()

# #challenge 131

# from tkinter import *
# import csv

# def create_new (): 
#     file = open ("ages.csv","w")
#     file.close()

# def save_list ():
#     file = open("ages.csv","a") 
#     name = name_box.get()
#     age = age_box.get()
#     newrecord = name + "," + age + "\n"
#     file.write (str(newrecord))
#     file.close() 
#     name_box.delete (0, END)
#     age_box.delete (0, END) 
#     name_box.focus ()

# window = Tk () 
# window.title ("People List")
# window.geometry("400x100")

# label1 = Label (text="Enter a name: ") 
# label1.place (x = 20, y=20, width = 100 , height=25)

# name_box = Entry (text = "") 
# name_box.place (x = 120, y = 20 , width=100, height = 25)
# name_box["justify"] = "left"
# name_box. focus ()

# labe12 = Label (text="Enter their age:") 
# labe12.place (x = 20, y = 50 , width = 100, height = 25)

# age_box = Entry (text = "") 
# age_box.place (x = 120, y = 50, width = 100 , height=25) 
# age_box["justify"] = "left"

# button1 = Button (text = "Create new file", command= create_new)
# button1.place (x = 250, y = 20, width = 100, height = 25) 

# button2 = Button (text = "Add to file", command = save_list)
# button2.place (x = 250, y = 50 , kh = 100 , height = 25)

# window.mainloop()

# #challenge 132

# from tkinter import *
# import csv

# def save_list ():
#     file = open("ages.csv", "a") 
#     name = name_box.get()
#     age = age_box.get()
#     newrecord = name + "," + age + "\n"
#     file.write(str (newrecord))
#     file.close()
#     name_box.delete (0, END)
#     age_box.delete (0, END) 
#     name_box.focus()

# def read_list (): 
#     name_list.delete (0, END)
#     file = list(csv. reader (open ("ages.csv")))
#     tmp = []
#     for row in file:
#         tmp.append(row)
#     x = 0
#     for i in tmp:
#         data= tmp[x]
#         name_list.insert (END, data)
#         x = x+1

# window = Tk()
# window.title("People List") 
# window.geometry ("400x200")

# label1 = Label (text="Enter a name: ") 
# label1.place ( x = 20, y = 20 , width = 100, height = 25)

# name_box = Entry (text = "")
# name_box.place (x = 120, y = 20, width = 100 ,height=25) 
# name_box["justify"]="left"
# name_box.focus()

# label2 = Label(text = "Enter their age:")
# label2.place (x = 20, y = 50, width = 100, height=25)

# age_box = Entry (text = "") 
# age_box.place (x = 120, y = 50, width=100,height=25) 
# age_box["justify"]="left"

# button1 = Button (text = "Add to file", command = save_list)

# button1.place (x = 250, y = 20, width = 100, height = 25)

# button2 = Button (text="Read list", command = read_list) 
# button2.place (x = 250, y = 50 , width=100, height =25)

# label3 = Label (text = "Saved Names:")
# label3.place (x = 20, y = 80 , width =100, height = 25)

# name_list = Listbox ()
# name_list.place (x = 120, y = 8 , width = 230 , height = 100)

# window.mainloop()

# 133

# from tkinter import *

# def click ():
#     name = textbox1.get() 
#     message = str("Hello " + name)
#     textbox2["text"] = message

# window = Tk ()
# window.title ("Names"). window.geometry ("450x350")
# window.wm_iconbitmap ("stripes.ico")
# window.configure (background= "black")

# logo = PhotoImage (file = "Mylogo.gif") 
# logoimage= Label (image = logo) 
# logoimage.place (x = 100, y=20, width = 200,  height = 150)

# label1 = Label (text = "Enter your name:")
# label1.place(x = 30, y=200) 
# label1["bg"] = "black"
# label1["fg"]= "white"

# textbox1 =Entry (text = "") 
# textbox1.place (x = 150, y = 200,width=200, height=25) 
# textbox1["justify"] = "center"
# textbox1.focus ()

# button1 = Button (text="Presa me", command = click) 
# button1.place (x = 30, y=250, width = 120, height = 25)
# button1 ["bg"] = "yellow"

# textbox2 = Message (text = "") 
# textbox2.place (x=150, y=250, width=200, height=25)
# textbox2 ["bg"] = "white" 
# textbox2 ["fg"] = "black"

# #challenge 134

# from tkinter import *
# import random

# def checkans ():
#     theirans = ansbox.get() 
#     theirans = int(theirans)
#     num1 = num1box["text"] 
#     num1 = int(num1)
#     num2 = num2box["text"]
#     num2 = int(num2)
#     ans = num1 + num2 
#     if theirans == ans:
#         img = PhotoImage (file = "correct.gif") 
#         imgbx.image = img
#     else:
#         img = PhotoImage (file = "wrong.gif") 
#         imgbx.image = img
#     imgbx["image"]= img
#     imgbx.update()

# def nextquestion (): 
#     ansbox.delete (0, END)
#     num1 = random.randint (10,50)
#     num1box["text"] = num1
#     num2 = random.randint (10,50)
#     num2box["text"] = num2
#     img = PhotoImage (file = "")
#     imgbx.image = img
#     imgbx ["image"]=img 
#     imgbx.update()

# window = Tk ()
# window.title = ("Addition") 
# window.geometry ("250x300")

# num1box = Label (text = "0")
# num1box.place (x = 50, y = 30, width = 25 , height=25)
# addsymbl = Message (text = "") 
# addsymbl.place (x = 75, y = 30, width = 25, height=25) 
# num2box = Label (text = "0")
# num2box.place (x = 100, y = 30, width = 25, height=25) 
# eqlsymbl = Message (text = "=" )
# eqlsymbl.place(x = 125, y = 30, width = 25, height = 25) 
# ansbox = Entry (text = "")
# ansbox.place (x = 150, y=30, width = 25, height = 25)
# ansbox ["justify"]="center"
# ansbox.focus() 
# checkbtn = Button (text = "Check", command = checkans)
# checkbtn.place (x = 50, y = 60, width = 75, height = 25)
# nextbtn = Button (text = "Next", command = nextquestion) 
# nextbtn.place (x = 130, y = 60, width= 75, height = 25)
# img = PhotoImage (file = "")
# imgbx = Label(image = img) 
# imgbx.image = img
# imgbx.place (x=25, y = 100, width = 200, height=150)

# nextquestion ()

# window.mainloop()

# #challenge 135

# from tkinter import *

# def clicked ():
#     sel = selectcolour.get ()
#     window.configure (background = sel)

# window = Tk
# window.title ("background") 
# window.geometry("200x200")

# selectcolour = StringVar(window)
# selectcolour.set ("Grey")

# colourlist = OptionMenu(window, selectcolour, "Grey","Red", "a1","Green", "Yellow")
# colourlist.place (x = 50 , y = 30)

# clickme = Button (text= "Click Me", command =clicked)
# clickme.place ( x = 50 , y = 150, width = 60, height = 30)

# mainloop()

# #challenge 136

# from tkinter import *

# def add_to_list ():
#     name = namebox.get() 
#     namebox.delete (0, END)
#     genderselection = gender.get() 
#     gender.set ("M/F")
#     newdata = name + ", " + genderselection + "\n" 
#     name_list.insert (END, newdata) 
#     namebox.focus ()

# window = Tk ()
# window.title ("People List") 
# window.geometry ("400x400")

# namelbl= Label (text = "Enter their name:")
# namelbl.place (x = 50, y = 50, width= 100, height=25) 
# namebox = Entry (text = "") 
# namebox.place (x = 150, y = 50 , width = 150,  height = 25)
# namebox.focus ()

# genderlbl = Label (text = "Select Gender") 
# genderlbl.place ( x = 50, y = 100 , width = 100, height = 25) 
# gender = StringVar (window)
# gender.set ("M/F")
# gendermenu = OptionMenu (window, gender, "M", "F")
# gendermenu.place (x = 150, y = 100)

# name_list = Listbox ()
# name_list.place( x = 150 , y = 150, width = 150 , height=100) 
# addbtn = Button (text ="Add to List", command = add_to_list) 
# addbtn.place (x = 50, y = 300, width=100, height = 25)

# window.mainloop()

# #challenge 137

# from tkinter import *

# def add_to_list ():
#     name = namebox.get() 
#     namebox.delete (0, END)
#     genderselection = gender.get() 
#     gender.set ("M/F")
#     newdata = name + ", " + genderselection + "\n"
#     name_list.insert (END, newdata)
#     namebox.focus ()
#     file = open("names.txt", "a")
#     file.write (newdata)
#     file.close()

# def print_list():
#     file = open("names.txt","r")
#     print (file.read())

# window = Tk()
# window.title ("People List") 
# window.geometry ("400x400")

# namelbl = Label (text = "Enter their name:")
# namelbl.place(x = 50, y = 50, width= 100, height=25)
# namebox = Entry (text = "")
# namebox.place (x = 150, y = 50, width=150, height=25) 
# namebox.focus()

# genderlb1 = Label (text= "Select Gender")
# genderlbl.place (x = 50, y = 100, width=100, height=25)
# gender = StringVar (window) 
# gender.set ("M/F")
# gendermenu = OptionMenu (window, gender, "M","F")
# gendermenu.place ( x=150, y = 100)

# name_list = Listbox ()
# name_list.place (x = 150, y = 150, width = 150, height=100)

# addbtn = Button (text = "Add to List", command = add_to_list) 
# addbtn.place(x = 50, y = 300 , width=100, height = 25)

# printlst = Button (text = "Print List", command= print_list)
# printlst.place (x = 175, y = 300, width = 100, height=25)

# window.mainloop()

# #challenge 138

# from tkinter import *

# def clicked ():
#     num = selection.get() 
#     artref = num + ".gif"
#     photo = PhotoImage (file = artref) 
#     photobox.image = photo 
#     photobox ["image"]=photo
#     photobox.update ()

# window = Tk ()
# window.title ("Art") 
# window.geometry("400x350")

# art = PhotoImage (file="1.gif")
# photobox = Label (window, image = art)
# photobox.image = art
# photobox.place ( x = 100, y = 20 , width=200, height=150)

# label = Label (text = "Select Art number: ")

# label.place ( x = 50 , y = 200, width = 100, height =25)

# selection = Entry (text = "") 
# selection.place ( epsilon = 200, y = 200, width=100,height=25) 
# selection.focus ()

# button = Button (text = "See Art", command = clicked) 
# button.place (x = 150, y=250, width=100, height =25)

# window.mainloop()




