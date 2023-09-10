user_input=int(input("Guess the spl number.. = "))

# if user_input == 11 :
#     print("Correct..!")
# elif user_input < 11 :
#     print("Guess is too small number..!")
# else :
#     print("Guess is too big number..!")
    
if user_input == 11 :
    print("Correct..!")
elif user_input in (12,10) :
    print("Guess is almost near..!")
else :
    print("Guess is too big number..!")