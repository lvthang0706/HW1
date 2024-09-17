class cup:
  def __init__(self, size, quantity):
    self.size = size
    self.quantity = quantity
  
  def fill(self, milliliers):
     if self.quantity + milliliers <= self.size:
        self.quantity += milliliers
       
     else:
        self.quantity = self.quantity
  def status(self):
   return self.size - self.quantity

cup = cup(100, 50)
print(cup.status())
cup.fill(40)
cup.fill(20)
print(cup.status())