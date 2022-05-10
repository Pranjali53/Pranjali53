import random
def Start_the_game():
    name=input("Please enter your name: ")
    print("Your most wellcome",name,"in Hangan game!!")
    print("Try to guess word in less then 8 attempts\notherwise you will loss the game!")
    word_list=["pranjali","upasana","navya","ayushi","gurpreet","ravya",""]
    choose_word=random.choice(word_list)
    word_length=len(choose_word)
    print("I giving one hint:-Your length of word is: ",word_length)
    all_letters=set("abcdefghijklmnopqrstuvwxyz")
    new_display=' '
    lives=8
    while len(choose_word)>0:
        display=""
        for letter in choose_word:
            if letter in new_display:
                display+=letter
            else:
                display+=" _ "
        if display==choose_word:
            print(display)
            print("Congratulations---",name,"you win the game")
            break
        print("guess the word",display)
        guess=input("Enter a guess : ")
        if guess in all_letters:
            new_display+=guess
        else:
            print("enter valid letter")
            
            guess=input("Enter a guess : ")
        if guess not in choose_word:
            lives-=1
            if lives==7:
                print('''   
                    +---+
                    |   |
                        |
                        |
                        |
                        |
                        =========''')
                print("Your 7 lives are left!")
            if lives==6:
                print(''' 
                    +---+
                    |   |
                    0   |
                        |
                        |
                        |
                        =========''')
                print("your 6 lives are left!")
            if lives==5:
                print('''
                    +---+
                    |   |
                    0   |
                   /    |
                        |
                        |
                        =========''')
                print("Your 5 lives are left!")
            if lives==4:
                print('''
                    +---+
                    |   |
                    0   |
                   /|   |
                        |
                        |
                        =========''')
                print("Your 4 lives are left!")
            if lives==3:
                print('''
                    +---+
                    |   |
                    0   |
                   /|\  |
                        |
                        |
                        =========''')
                print("Your 3 lives are left!")           
            if lives==2:                   
                    print('''
                        +---+
                        |   |
                        0   |
                       /|\  |
                        |   |
                            |
                            =========''')
                    print("Your 2 lives are left!! Save Your Man")
            if lives==1:
                    print('''
                            +---+
                            |   |
                            0   |
                           /|\  |
                            |   |
                           /    |
                                =========''')
                    print("only 1 live are left!!   Hangman on his last breath")
            if lives==0:
                    print('''
                            +---+
                            |   |
                            0   |                         _
                           /|\  |
                            |   |
                           / \  |
                                =========''')
                    print("Oops you losse the game")
                    print("Now the Game is over")
                    break
Start_the_game()
while True:
    Play_again=input("Do you want to Play again \n 1. Yes\n 2. No\n")
    if Play_again=="Yes":
        Start_the_game()
    else:
        break       

    