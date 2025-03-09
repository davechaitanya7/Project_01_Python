# Rock PaperSciessor Game using Python
import random


def Get_Choices_Game():
    
    Player_choice1= input("Enter a Choice(Rock,Paper,Scissor: ")
    Options = ["Rock", "Paper", "Scissors"]
    Computer_choice =random.choice(Options)
    Choices ={
        "Player":Player_choice1,
        "Computer":Computer_choice
    }
    return Choices

def cheak_win(Player,Computer):
    print("You Chose " + Player + "  Computer Chose  " + Computer)
    if Player==Computer:
        # print("BothWinner and tie")
        return "Both winner And tie"
    elif Player == "Rock":
        if Computer == "Scissor":
            return "You winner"
        else:
            return "Computer is winner"
    elif Player == "Paper":
        if Computer == "Rock":
            return "You winner"
        else:
            return "Computer is winner"
    elif Player == "Scissor":
        if Computer == "Paper":
            return "You winner"
        else:
            return "Computer is winner"
     
Choices = Get_Choices_Game()   
Result = cheak_win(Choices["Player"],Choices["Computer"])

print("Final Result : ")
print(Result)
print("I added this Project to My File ")
