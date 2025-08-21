user_age= int(input("Please enter your age: "))
if user_age < 18:
    print("You are a minor")
elif user_age >=18 and user_age< 65:
    print("Your are an adult")
else:
    print("You are a senior citizen")
# the code above is a python programme that ask a user to input his/age, if the users age is less than 18
#the programme will return "you are a minor". else if the user enters an age that is greater than 18 and less
#than 65, it will return "Your are an adult". else if the user enters an age greater than 65 years it will 
#output "you are a senior citizen"