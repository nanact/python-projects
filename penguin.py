class bird:
   def __init__(self):
        print("Bird is ready")
       
   def whoisthis(self):
        print("Bird")
   def Swim(self):
       print("swim faster")
       
class penguin(bird):
    def __init__(self):
        print("penguin is ready")
        bird.__init__(self)
    def whoisthis(self):
        print("penguin")
        
    def run(self):
        print("run faster")
        
pen = penguin()
        
pen.whoisthis() 

pen.run()

pen.Swim()
