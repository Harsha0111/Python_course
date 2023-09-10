num = 7
# user_input =input("Would you like to play(Y/n): ")

# while user_input != "n":
#     user_number=(int(input("Please enter any number: ")))
#     if user_number == num:
#         print("Your Guess is Correct...")
#     elif abs(user_number - num) == 1:
#         print("Your Guess is off by one...")
#     else:
#         print("Your Guess is Wrong...")

while True:
    user_input = input("Would you like to play(Y/n): ")

    if user_input == "n":
        break

    user_number = (int(input("Please enter any number: ")))
    if user_number == num:
        print("Your Guess is Correct...")

    elif user_number - num in  (1, -1):
        print("Your Guess is off by one...")
    
    else:
        print("Your Guess is Wrong...")
