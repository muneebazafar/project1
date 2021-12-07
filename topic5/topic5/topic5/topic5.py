
# Challenge 7
#EVE - artificial intelligence - ask questions - analyse possible answers
#to respond to the user with predefiened possible answers

print("hello i am E.V.E")
age=int(input("how old are you?"))
Relation=int(input("How many people are in your family(in total)"))
if age<18:
  print("you are still a teenager")
elif age>=18:
  print("you are an adult")
else:
  print("please answer in numbers")
if Relation>=5:
  print("wow! you have alot of family")
elif Relation<=4:
  print("That is a good size family")
else:
  print("please answer in numbers")