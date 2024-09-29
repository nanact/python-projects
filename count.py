amount = float(input("Enter the amount to withdraw: "))

note_1 = amount//100

note_2 = (amount%100)//50

note_3 = ((amount%100)%50)//10

print("note of 100 ruber:",note_1)

print("note of 50 ruber:",note_2)

print("note of 10 ruber:",note_3)