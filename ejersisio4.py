class Condicion:
   contador=0

   def __init__(self,num1=0,num2=1):
       self.numero1=num1
       self.numero2=num2 
 
   def usoIf(self):
    if self.numero1 == self.numero2:
        print("numero1:{}, numero2{}: son iguales".format(self.numero1,self.numero2))


cond1 = Condicion()
print(cond1.numero1)
print(cond1.numero2)

cond2 = Condicion()
print(cond2.numero1)
print(cond2.numero2)


