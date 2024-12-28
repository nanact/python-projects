class IOString:
    def __init__(self):
        self.srt1 = ""
    def get_String(self):
        self.str1 = input("Enter you string: ")
        
    def print_(self):
        print("Your result: ", self.str1.upper())
        
str1 = IOString()

str1.get_String()

str1.print_()
