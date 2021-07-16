class Ciclo:
   def __init__(self,num1=5):
       self.numero1=num1

   def usoWhile(self):
        car = input("ingrese vocal: ")
        car=car.lower()
        while car not in('a','e','i','o','u'):
            car = input("Ingrese vocal: ").lower()
        print("felicidades el caracter:{} es una vocal".format(car))

ciclo1 = Ciclo()
ciclo1.usoWhile()
