#CHALLENGES 20-26
#20
name= input('Enter your first name')
length= len(name)
print(length)

#21
name1= input('Enter your first name ')
name2= input('Enter your last name')
fullname= name1 + ' ' + name2
print(fullname, len(fullname))

#22
name1= input('Enter your first name in lower case')
name2= input('Enter your last name in lower case')
name1= name1.title()
name2= name2.title()
fullname= name1 + ' ' + name2
print(fullname)

#23
phrase= input('Enter the first line of a nursery rhyme :')
lenght= len(phrase)
print('This has', lenght,'letters in it')
start=int(input('Enter a starting number'))
end= int(input('Enter an end number'))
part=(phrase[start : end])
print(part)

#24
word=input('Type in a word :')
word.upper()
print(word)

#25
name= input('Enter your first name')
if len(name)<5 :
    surname = input('Enter your surname')
    fullname= name+surname   
    print(fullname.upper())
elif len(name) >=5 :
    print (name.lower())

#26
#Pig Latin
word= input('Enter a word:')
first=word[0]
lenght=len(word)
rest=word[1:lenght]
if first !='a' and first !='A' and first !='e' and first !='i' and first !='o' and first !='u':
    newword= rest+ first+ 'ay'
else :
    newword= word+ 'way'
print(newword.lower())
