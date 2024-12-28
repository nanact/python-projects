class Employee:
    def __init__ (self):
        print("Employee created")
        
    def __del__(self):
        print("destructed called")
        
def Create_obj():
    print("Making Obj")
    obj = Employee()
    print("function end")
    return obj

print("calling Create obj ...")

obj = Create_obj()

print("Program ended ...")