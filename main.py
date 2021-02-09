import requests
import random

word_site = "https://www.mit.edu/~ecprice/wordlist.10000"

response = requests.get(word_site)
randomWords = response.content.splitlines()

idolField = [['_',' ',' ','-','/',' '],['_','|','O','|',' ',' '],[' ',' ',' ','-','\\',' ']]

currentField=[[' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ']]
def drawHangMan(field):
    for row in range(6):
        if row!=0:
            for col in range(5):
                if col!=3:
                    if col!=4:
                        if col==1 and row==1:
                            print("|",end='')
                        else:
                            print(field[col][row],end='')
                    else:
                        print("|")
                else:
                    print(" ",end='')
        else:
            for col in range(4):
                if col != 3:
                    print("_",end='')
                else:
                    print("_")

def consequence(mistake):
    if mistake == 1:
        currentField[1][2]='O'
    elif mistake == 2:
        currentField[1][3]="|"
    elif mistake == 3:
        currentField[0][3]="-"
    elif mistake == 4:
        currentField[2][3]="-"
    elif mistake == 5:
        currentField[0][4]='/'
    else:
        currentField[2][4]='\\'
    drawHangMan(currentField)



player=1
mistakes=0
print("Welcome to hangman!")
drawHangMan(idolField)
print("There are 2 modes\n1. Player 1 vs Computer.\n2.Player 1 vs Player 2.\nChoose one!")
mode = input("Enter mode no.:\n")
word=''
if mode == '1':
    word = random.choice(randomWords)
    word = word.decode("utf-8") 
else:
    word = input("Player 1 pick a word\n")
word = word.lower()
spaces=len(word)*' _'
print(chr(27) + "[2J")
drawHangMan(currentField)
print('\n')
print(spaces)
actualWord=word

while(True):
    spaceCount = spaces.count('_')
    if spaceCount != 0 and mistakes < 6:
        guess = input("Player 2 guess a letter\n")
        if len(guess)<2:
            if guess in word:
                word = list(word)
                index = word.index(guess)
                spaces = list(spaces)
                spaces[2*index+1]=guess
                spaces = ''.join(spaces)
                word[index] = ' '
                word = ''.join(word)
                print(chr(27) + "[2J")
                print(spaces)
            else:
                print(chr(27) + "[2J")
                print('\nyou are wrong!')
                mistakes = mistakes+1
                consequence(mistakes)
                print(spaces)
        else:
            print('Invalid input!')
    else:
        if spaceCount == 0:
            print("The man is safe!")
            print("Player 2 won!")
            break
        else:
            print("The man is dead!")
            print("Player 1 won!")
            print("The word was,",actualWord,'!')
            break

