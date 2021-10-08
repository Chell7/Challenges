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