# import random
# #get guessed
# def get_guess():
#     return list(input("What is your guess"))
#
# #generate computer code (3 digit)
# def generate_code():
#     digits = [str(num) for num in range(10)]
#     #shuffle the digits
#     random.shuffle(digits)
#     #then grab the first three
#     return digits[:3]
#
# #generate the clues
# def generate_clues(code, user_guess):
#     if user_guess == code:
#         return "CODE CRACKED"
#
#     clues = []
#
#     for ind, num in enumerate(user_guess):
#         if num == code[ind]:
#             clues.append("Match")
#         elif num in code:
#             clues.append("Close")
#     if clues == []:
#         return{'Nope'}
#     else:
#         return clues
#
# #run game logic
# print("Welcome code breaker!")
#
# secret_code = generate_code()
# clue_report = []
#
# while clue_report != "CODE CRACKED":
#     guess = get_guess()
#     clue_report = generate_clues(guess, secret_code)
#     print("Here is the result of your guess")
#     for clue in clue_report:
#         print(clue)

# Another way of doing it
import random
snum = str(random.randint(100,999))
guess = input("What is your guess? ")
while (guess != snum):
    print("Match" if (guess[0] == snum[0] or guess[1] == snum[1] or guess[2] == snum[2]) else "No Match")
    guess = input("What is your guess? ")
print("You guessed it right!")
