# simple python script to play rock paper and scissors
import random

while True:
  points = 0
  user_choice = input("Enter a choice (rock,paper,scissors): ")
  all_choices = ["rock","paper","scissors"]
  computer_choice = random.choice(all_choices)
  
  print("You chose {0} and computer chose {1}\n".format(user_choice,computer_choice))
  
  if user_choice == computer_choice:
      print("Same choice {0} selected by both. It's a tie\n".format(user_choice))
      
  elif user_choice == "rock":
      if computer_choice == "scissors":
          print("Rock beats scissors. You get a point.\n")
          points = points + 1
      else :
          print("Paper covers rock. You lose a point.\n")
          points = points -1
  elif user_choice == "paper":
        if computer_choice == "rock":
            print("Paper covers rock! You win a point.\n")
            points = points + 1
        else:
            print("Scissors cuts paper! You lose a point.\n")
            points = points - 1
  elif user_choice == "scissors":
        if computer_choice == "paper":
            print("Scissors cuts paper! You win a point. \n")
            points = points + 1
        else:
            print("Rock beats scissors! You lose a point.\n")
            points = points - 1
  play_again = input("Play again? (y/n): ")
  if play_again.lower() != "y":
      print("You scored {0} points\n".format(points))
      break
