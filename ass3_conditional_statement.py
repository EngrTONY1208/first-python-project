from http.cookiejar import uppercase_escaped_char
from string import ascii_lowercase
score = int(input("please enter your score: "))
if score >=70:
    print("Grade A")
elif score >=60:
    print("Grade B")
elif score >= 50:
    print("Grade C")
elif score >= 45:
    print("Grade D")
elif score >=40:
    print("Grade E")
else:
    print("You have a carryover")
    
user_name = input("please enter your user name: ")
password = input("please enter your password: ")
print(user_name)
print(password)
special_char="!@#$%^&*()"
if password==user_name.upper() and password==user_name.lower() and password==special_char:
    print("you can have access")
else:

    print("re-enter your password")
if len(user_name)>=8:

    print("Welcome to the platform")
elif len(user_name) !=8:
    print("please renter your username")
else:
    print("please try again")