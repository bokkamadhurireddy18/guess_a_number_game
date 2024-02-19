import random
from art import logo
print(logo)
print("WELCOME TO THE NUMBER GUESSING GAME!")
print("I'm thinking of a number between 1 and 100.")

diff_level= input("Choose a difficulty. Type 'easy' or 'hard': ")
actual_num= random.randint(1,100)

def guess_num():
  user_num = int(input("Guess a number: "))
  if(actual_num==user_num):
    print("Wow! Your guess is right!")
    return True
  elif(actual_num > user_num):
    print("Too low.")
    return False
  elif(actual_num< user_num):
    print("Too high.")
    return False

if (diff_level.lower() == 'easy'):
  generate= 10
elif (diff_level.lower() == 'hard'):
  generate= 5
guessed= False
while generate >0 and guessed==False:
  print(f"You have {generate} attempts remaining to guess the number.")
  guessed= guess_num()
  generate-=1
  if(generate==0):
    print(f"You lost! The number is {actual_num}!")