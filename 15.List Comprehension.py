numbers = [1,2,3,4,5]
# doubled=[]

# To avoid this loop when can use below method
# for num in numbers:
#     doubled.append(num * 2)  

doubled=[num * 2 for num in numbers]

print(doubled)

# eg:2

friends = ["Sri", "Leka", "Babu", "Sneka","Bhanu" ,"sam"]
# starts_s=[]

# for friend in friends:
#     if friend.startswith("S"):
#     # if friend.upper().startswith("S"):
#         starts_s.append(friend)
# print (starts_s)

# replacing the for loop in single line
starts_s = [friend for friend in friends if friend.startswith("S")]
# starts_s = [friend for friend in friends if friend.upper().startswith("S")]
print (starts_s)