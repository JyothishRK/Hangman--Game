import random

#function to print the current status of word
def printing(list):
    for i in list:
        print(i,end=" ")
    print()

#word bank
words=['Python','Computer','Java','FullStack','Development','Inception']
#Choosing a random word from the above list
choice =random.randrange(0,len(words)-1,1)
word=words[choice]
#Game begins
print('-'*25)
print('Welcome to Hangman Game')
print('-'*25)
list=[]
for i in word:
    list.append('_')
print()
c=len(word)
chance=10
while chance>0 and c>0:
    printing(list)
    print('No of Guesses remaining:',chance)
    dat=input('Enter Your guess:')
    f=1
    for i in range(len(word)):
        if(word[i].lower()==dat.lower()):
            list[i]=word[i]
            c-=1
            f=0
    if(f):
       print('Wrong guess')
       chance-=1
    print()
print('The word is',word)
if(chance==0):
    print('Game over, Try again!')
else:
    print('Congratulations you won!!!')