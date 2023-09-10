users = [
    (0, "Bob", "passwd"),
    (1, "Ganga", "abc@1"),
    (2, "Sneka", "npoe2"),
    (3, "Mathu", "12wer")
]

# dict comprehension
user_mapping = {user[1]: user for user in users}
# print(user_mapping)
# print(user_mapping["Sneka"])

user_name  = input("enter uname")
passwd_ip  = input("enter passwd")

_, username, passwd = user_mapping[user_name]

if passwd_ip == passwd:
    print("correct")
else:
    print("incorrect")


