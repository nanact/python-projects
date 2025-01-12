
class A():
  def __init__(self, a):
    self.a = a  
  def __lt__(self, others):
    if self.a < others.a:
        return "ob1 is less than ob2"
    else:
        return "ob2 is less than ob1"
  def __eq__(self, others):
    if self.a == others.a:
        return "they are equal"
    else:
        return "They are not the same"
    
ob1 = A(3)
ob2 = A(4)

print("Value Passed: ", ob1.a, ob2.a)

print(ob1 > ob2)

ob3 = A(8)

ob4 = A(8)

print("Value Passed: ", ob3.a, ob4.a)

print(ob3 == ob4)