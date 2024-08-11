import random
Cchoice=["Rock","Paper","Scissor"]
while True:
    print("Rock Paper Scissor Game:")
    youwin,computerwin=0,0
    for i in range(1,6):
        print("Round",i,"Start:")
        print("Please Select any one option:")
        print("1.Rock","2.Paper","3.Scissor",sep="\n")
        Yourchoice=int(input())
        if Yourchoice==1:
            print("You Select Rock")
            Yourchoice="Rock"

        elif Yourchoice==2:
            print("You Select Paper")
            Yourchoice="Scissor"

        elif Yourchoice==3:
            print("You Select Scissor")   
            Yourchoice="Scissor" 

        else:
            print("Invalid Choice")
            break           

        Computerchoice=random.choice(Cchoice)
        print("Computer Select:",Computerchoice)

        if Yourchoice==Computerchoice:
            youwin+=1
            computerwin+=1
            print("This Round Is Drawn:")

        elif(Yourchoice=="Paper" and Computerchoice=="Rock") or (Yourchoice=="Rock" and Computerchoice=="Scissor") or (Yourchoice=="Scissor"and Computerchoice=="Paper"):
             youwin+=1
             print("You Win This Round")

        else:
            computerwin+=1
            print("Computer win this round")

    if youwin>computerwin:
        print("You Win The Game:")   
        print("Score is:","Your Score:",youwin,"Computer Score:",computerwin,sep=" ")

    elif computerwin>youwin:
        print("You lose the game. Computer win the game:")
        print("Score is:","Your Score:",youwin,"Computer Score:",computerwin,sep=" ")

    else:
        print("Match Drawn")    
        print("Score is:","Your Score:",youwin,"Computer Score:",computerwin,sep=" ")

    user_choice=input("Want to play again(Yes/Exit)")
    if user_choice=='yes'or user_choice=='yes'or user_choice=='yes':
        continue
    else:
        break