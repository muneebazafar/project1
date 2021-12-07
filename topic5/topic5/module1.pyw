# Challenge 9
total = float(input("Please enter your mark:"))
percentage = (total/100)*100

print("Total marks = %.2f" %total)
print("Marks Percentage = %.2f" %percentage)

if (percentage >= 90):
    print("You got an A*, well done")
elif(percentage >= 80):
    print("You get a grade B")
elif(percentage >= 70):
    print("You get a grade C")
elif(percentage >= 60):
    print("You got a grade D :/")
elif(percentage >= 40):
    print("You get an E grade :/")
else:
    print("You failed.")
