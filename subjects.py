print("Enter months in four subjects")

english = int(input("English:  "))

maths = int(input("Maths: "))

science = int(input("Science: "))

Career_Tech = int(input("Career Tech: "))

all_subjects = english+maths+science+Career_Tech

perc = (all_subjects/400)*100

print("the total is",all_subjects,"The percentage is",perc)