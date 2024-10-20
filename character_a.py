string = input("Enter your word: ")

char = input("please enter your own charater: ")

count=0

i = 0

while i < len(string):
    if (string[i]==char):
        count += 1
    i = i + 1

print("Count is ",count)
