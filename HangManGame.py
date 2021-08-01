import random
def hangman():
    word=random.choice(["pugger","little pugger","superman","thor","thanos",\
          "newton","tiger","dani","valentina","aubrey"])
    validLetters="abcdefghijklmnopqrstuvwxyz"
    Tries=10
    guessMade=""                                    #word to be updated
    
    while len(word)>0:
        main=""                                     #word to be compared
        
        for letter in word:                         #checking the letter in the word
            if letter in guessMade:                 #checking the letter in the updated guess
                main+=letter
            else:
                main+="_"+" "
                
        if main==word:                              #winning condition
            print(main)                                
            print("You Win!")
            break
        
        print("Guess The Word:",main)
        guess=input()                               #guess of characters to be stored
                
        if guess in validLetters:                   #check if the letter in validLetters
            guessMade=guessMade+guess               #updating the guessMade
        else:
            print("Enter A valid Character")
            guess=input()
            
        if guess not in word:
            Tries-=1
            if Tries==9:
                print(f"9 turns left")
                print("-------------------------")
                
            if Tries==8:
                 print(f"8 turns left")
                 print("-------------------------")
                 print("            O            ")
                 
            
            if Tries==7:
                 print(f"7 turns left")
                 print("-------------------------")
                 print("            O            ")    
                 print("            |            ")

            if Tries==6:
                 print(f"6 turns left")
                 print("-------------------------")
                 print("            O            ")    
                 print("            |            ")
                 print("           /             ")
                 
            if Tries==5:
                 print(f"5 turns left")
                 print("-------------------------")
                 print("            O            ")    
                 print("            |            ")
                 print("           / \           ")
                 
            if Tries==4:
                 print(f"4 turns left")
                 print("-------------------------")
                 print("          \ O            ")    
                 print("            |            ")
                 print("           / \           ")

            if Tries==3:
                 print(f"3 turns left")
                 print("-------------------------")
                 print("          \ O /          ")    
                 print("            |            ")
                 print("           / \           ")

            if Tries==2:
                 print(f"2 turns left")
                 print("-------------------------")
                 print("          \ O /|         ")    
                 print("            |            ")
                 print("           / \           ")
                 
            if Tries==1:
                 print(f"1 turn left")
                 print("Last Breaths Counting,Take Care!")
                 print("-------------------------")
                 print("          \ O_ /|        ")    
                 print("            |            ")
                 print("           / \           ")

            if Tries==0:
                 print("You Lose!")
                 print("You Let A Kind Man Die!")
                 print("-------------------------")
                 print("            O_|          ")    
                 print("           /|\           ")
                 print("           / \           ")
                 break
             
                
Name=input("Enter Your Name:")

print(f"\n Hello {Name}!\n Welcome to The HangMan Game.")
print("-----------------------------------------------------")
print(f" Try To Guess The word in less Than 10 tries!")
hangman()
print()