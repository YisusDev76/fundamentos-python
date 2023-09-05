'''
“Tijera corta a papel, 
papel tapa a piedra, 
piedra aplasta a lagarto, 
lagarto envenena a Spock, 
Spock rompe a tijera, 
tijera decapita a lagarto, 
lagarto devora a papel, 
papel desautoriza a Spock, 
Spock vaporiza a piedra, 
y como siempre, piedra aplasta a tijera”
'''

user_option = 'spock'  # User
computer_option = input(
    ' Computer''\n''piedra, papel, tijera, lagarto o spock => ')
'''
Tijera corta a papel
y como siempre, piedra aplasta a tijera”

tijera decapita a lagarto
Spock rompe a tijera

papel tapa a piedra
lagarto devora a papel

papel desautoriza a Spock
piedra aplasta a lagarto
Spock vaporiza a piedra
'''


if user_option == computer_option:
    print('Empate!')
elif user_option == 'piedra':
    if computer_option == 'papel':
        print('Papel cubra piedra''\n''Computer gana!')
    if computer_option == 'lagarto':
        print('Piedra aplasta a lagarto''\n''User gana!')
    if computer_option == 'spock':
        print('Spock pulperiza piedra''\n''Computer gana!')
    if computer_option == 'tijera':
        print('Piedra rompe tijera''\n''User gana!')
elif user_option == 'papel':
    if computer_option == 'tijera':
        print('Tijera rompe papel''\n''Computer gana!')
    if computer_option == 'lagarto':
        print('Lagarto devora papel''\n''Computer gana!')
    if computer_option == 'spock':
        print('Papel desautoriza a Spock''\n''User gana!')
    if computer_option == 'piedra':
        print('Papel envuelve piedra''\n''User gana!')
elif user_option == 'tijera':
    if computer_option == 'piedra':
        print('Piedra rompe tijera''\n''Computer gana!')
    if computer_option == 'papel':
        print('Tijera rompe papel''\n''User gana!')
    if computer_option == 'spock':
        print('Spock rompe tijeras''\n''Computer gana!')
    if computer_option == 'lagarto':
        print('Tijera decapita lagarto''\n''User gana!')
elif user_option == 'lagarto':
    if computer_option == 'piedra':
        print('Piedra aplasta lagarto''\n''Computer gana!')
    if computer_option == 'papel':
        print('Lagarto como papel''\n''User gana!')
    if computer_option == 'tijera':
        print('Tijera decapita lagarto''\n''Computer gana!')
    if computer_option == 'spock':
        print('Lagarto envenena spock''\n''User gana!')
elif user_option == 'spock':
    if computer_option == 'piedra':
        print('Spock vaporiza a piedra''\n''User gana!')
    if computer_option == 'papel':
        print('Papel dezautoriza a Spock''\n''Computer gana!')
    if computer_option == 'tijera':
        print('Spock rompe tijera''\n''User gana!')
    if computer_option == 'lagarto':
        print('Lagarto envenena a Spock''\n''Computer gana!')


        # ------------------------Version 2----------------------------------------
        import random


print(""" 
      English Description:
      Welcome to "Rock, paper, scissors, lizard, Spock"
      🥌 📋 ✂ 🦎 🖖
      Rules:
      
      *Scissors cut paper
      *Paper covers stone
      *Rock crushes lizard
      *Lizard poisons Spock
      *Spock breaks scissors
      *Scissors decapitates lizard
      *Lizard devours paper
      *Paper overrules Spock
      *Spock vaporizes stone
      *And as always, rock breaks scissor
      ---------------------------------------------------
      Descripciónen Español
      
      Bienvenidos a "Piedra, papel, tijera, lagarto, Spock"
🥌 📋 ✂ 🦎 🖖
      Reglas:
      
       *Tijeras cortan papel
       *Papel cubre piedra
       *Piedra aplasta lagarto
       *Lagarto envenena a Spock
       *Spock rompe tijeras
       *Tijeras decapitan lagarto
       *Lagarto devora papel
       *El papel desautoriza a Spock
       *Spock vaporiza piedra
       *Y como siempre, piedra rompe tijera
      ---------------------------------------------------
      """)

user_name = input("Enter your name => ")
user_option = input("Choose an option: Rock, paper, scissors, lizard or Spock => ").lower()
options = ["rock", "paper", "scissors", "lizard", "spock"]

# validate user input with while
while(not (user_option in options)):
            print("wrong option")
            user_option = input("Choose an option: Rock, Paper, Scissors, Lizard or Spock => ").lower()


#other ways to validate user input with while
"""
while user_option != "rock"and user_option != "paper" and user_option !="scissors"and user_option!= "lizard"and user_option!= "spock":
    print(f"{user_name} enter a valid option")
    user_option= input("Choose an option: Rock, paper, scissors, lizard or Spock => ").lower()


while(True):
      if user_option in options:
            break
      else:
            print("wrong option")
            user_option = input("Choose an option: Rock, Paper, Scissors, Lizard or Spock => ").lower()

"""
    
print(f"{user_name} you have selected: {user_option} \n")
print("Now it's the computer's turn")

"""
1 =rock 2=paper 3=scissors 4=lizard 5=spock
"""
#random option assignment from option list
computer_option = options[random.randint(0, 4)]

#print computer option
if computer_option == "rock":
    print(f"the computer has chosen: {options[0]}")
elif computer_option == "paper":
    print(f"the computer has chosen: {options[1]}")
elif computer_option == "scissors":
    print(f"the computer has chosen: {options[2]}") 
elif computer_option == "lizard":
    print(f"the computer has chosen: {options[3]}")
elif computer_option == "spock":
    print(f"the computer has chosen: {options[4]}")

print("---------------------------------------")

#combat
if user_option == computer_option:
    print(f"This is a draw!")
elif user_option == "rock":
    if computer_option == "scissors":
        print("rock breaks scissor, you win!")
    elif computer_option == "lizard":
        print("Rock crushes lizard, you win")
    else:
        print("Computer win, you lose :( !")
elif user_option == "paper":
    if computer_option == "rock" :
        print("Paper covers stone, you win!")
    elif computer_option == "spock":
        print("Paper overrules Spock, you win")
    else:
        print("Computer win, you lose :( !")
elif user_option == "scissors":
    if computer_option == "paper":
        print("Scissors cut paper, you win!")
    elif computer_option == "lizard":
        print("Scissors decapitates lizard, you win")
    else:
        print("Computer win, you lose :( !")
elif user_option == "lizard":
    if computer_option == "paper":
        print("Lizard devours paper, you win!")
    elif computer_option == "spock":
        print("Lizard poisons Spock, you win")
    else:
        print("Computer win, you lose :( !")
elif user_option == "spock":
    if computer_option == "scissors":
        print("Spock breaks scissors, you win!")
    elif computer_option == "rock":
        print("Spock vaporizes rock, you win")
    else:
        print("Computer win, you lose :( !")
