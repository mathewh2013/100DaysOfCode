import random 

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
choices = [rock, paper, scissors]


user_choice = int(input("What do you shoose? Press 0 for rock, 1 for paper, 2 for scissors.\n"))

if user_choice >=3 or user_choice < 0:
    print("Incorrect input")
    
else:
    print(choices[user_choice])

    computer_choice = random.randint(0, 2)
    print("computer chose: ")
    print(choices[computer_choice])


    if user_choice == 0 and computer_choice == 2:
        print("You Win!")
    elif computer_choice == 0 and user_choice == 2:
        print("You Lose!")
    elif computer_choice > user_choice:
        print("You Lose!")
    elif user_choice > computer_choice:
        print("You Lose!")
    elif user_choice == computer_choice:
        print("Its a draw!")
