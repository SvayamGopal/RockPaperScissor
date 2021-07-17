import random

# User Input
print('''
---------------------------------------------
               INSTRUCTIONS

                1 for Rock
                2 for Paper
                3 for Scissor

    First to win 3 rounds is the Winner.
    
---------------------------------------------
      ''')
def Game(Pscore,Cscore,Round):
    print("\n----------------- Round -",Round,"-----------------")
    choice= int(input("Enter choice (1,2,3): "))
    choiceList = [1,2,3]
    compChoice = random.choice(choiceList)
    if choice not in choiceList:
        print("Invalid Choice")
    else:
        if choice == 1:
            print("You chose: ROCK")
            print('''
         ____________         
--------'    ________)
            (_________)
            (_________)
            (________)
--------.___(_______)
            
                  ''')
        elif choice == 2:            
            print("You chose: PAPER")
            print('''
         ____________         
--------'    ________)_____
                  _________)
                   _________)
                  ________)
--------.______________)
            
                  ''')
        elif choice == 3:
            print("You chose: SCISSOR")
            print('''
         ______        
--------'  ___ \____________
          (____/   _________)
                   _________)
            (_______)
--------.___(_______)
            
                  ''')
            
        
        if compChoice == 1:
            print("Computer chose: ROCK")
            print('''
         ____________         
--------'    ________)
            (_________)
            (_________)
            (________)
--------.___(_______)
            
                  ''')
        elif compChoice == 2:            
            print("Computer chose: PAPER")
            print('''
         ____________         
--------'    ________)_____
                  _________)
                   _________)
                  ________)
--------.______________)
            
                  ''')
        elif compChoice == 3:
            print("Computer chose: SCISSOR")
            print('''
         ______        
--------'  ___ \____________
          (____/   _________)
                   _________)
            (_______)
--------.___(_______)
            
                  ''')
            
        if (choice == 1 and compChoice == 1) or (choice == 2 and compChoice == 2) or (choice == 3 and compChoice == 3):
            print("\nDraw")
        elif (choice == 1 and compChoice == 3) or (choice == 2 and compChoice == 1) or (choice == 3 and compChoice == 2):
            Pscore=Pscore + 1
            print("\nPlayer wins round",Round)
        elif (choice == 3 and compChoice == 1) or (choice == 1 and compChoice == 2) or (choice == 2 and compChoice == 3):
            Cscore=Cscore + 1
            print("\nComputer wins round",Round)


    print('''
                  Score
            Player  :   Computer''')
    
    print("              ",Pscore,"   :    ",Cscore)
    Round=Round+1
    if Pscore == 3:
         print("\n---------------- Player Wins -----------------\n")
         again = input("Want to play again (y/n): ")
         if again == 'y' or again == 'Y':
             Game(0,0,1)
         else: 
            print("\nThanks for playing!")
    elif Cscore == 3:
         print("\n--------------- Computer Wins ----------------\n")
         again = input("Want to play again (y/n): ")
         if again == 'y' or again == 'Y':
             Game(0,0,1)
         else: 
            print("\nThanks for playing!")
    else:
        Game(Pscore,Cscore,Round)
        
Game(0,0,1)

        

