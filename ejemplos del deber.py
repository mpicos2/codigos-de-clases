class Ejersisios:
    def __init__(self):
        pass
    
    #EJEMPLO 1.
    def calcpi(self):
        Re = float(input("Ingresar radio del circulo: "))
        pi = 3.1416
        s = pi*Re**2
        print("La superficie del circulo es:{} ".format(s))

    #EJEMPLO 2.
    def descuento(self):
        To = float(input("Ingrese total de compras: "))
        d = To*0.15
        Fc = To-d
        print("Total a cancelar es: {} ".format(Fc))

    #EJEMPLO 3.
    def ventas(self):
            Sa = float(input("Ingrese su salario: "))
            v1 = float(input("Igrese el valor de mi primer venta: "))
            v2 = float(input("Ingrese el segundo valor de la venta: "))
            v3 = float(input("Ingrese el tercer valor de la venta: "))
            To = v1+v2+v3
            Co = To*0.1
            Tv = round(To+Co,2) 
            print("El total a recibir por comicion es:{} ".format(Tv))

    #EJEMPLO 4.
    def algoritmo(self):
        cali = float(input("Ingresar calificacion: "))
        if cali >= 7:
            print("has pasado")
        
    #EJEMPLO 5.
    def algoritmo2(self):
        calif = float(input("Ingresar calificacion: "))
        if calif >= 7:
            print("Has pasado ")
        else:
            print("Has reprobado ")

    #EJEMPLO 6.
    def sueldo(self):
        s = float(input("Ingrese su sueldo: "))
        if s < 600:
            n = s+s*0.1
            print("Su nuevo sueldo es {}".format(n))
        else:
            print("Su sueldo sigue siendo de {}".format(s))

    #EJEMPLO 7. 
    def dinero(self):
        H = int(input("Ingrese el numero de horas trabjadas: "))
        P = float(input("Ingrese el valor a pagar por hora: "))
        if H > 48:
            t = H - 48
            d = 8
            s = 40*P + d*P*2 + t*P*3
            print("Total a pagar por las horas trabajadas es : {}".format(s))
        elif H < 40:
            d = H-40
            s = 40*P + d*P*2
            print("Total a pagar por las horas trabajadas es : {}".format(s))
        else:
            s = H*P
            print("Total a pagar por las horas trabajadas es : {}".format(s))
           
    #EJEMPLO 8.
    def diff(self):
        n = []
        for i in range(3):
            num = float(input("Introduce el número #{}: ".format(i + 1)))
            n.append(num)
        m = n[0]
        for num in n:
            if num > m:
                m = num
        print("El numero mayor es : {}".format(m))

    #EJEMPLO 9.
    def var(self):
        v = float(input("Ingresar valor de V: "))
        num = float(input("Ingresar valor de num: "))
        if num == 1:
            r = 100*v
        elif num == 2:
            r = 100^v
        elif num == 3:
            r = 100/v
        else:
            r = 0
        print("El resultado es {}".format(r)) 

    #EJEMPLO 10.
    def exa(self):
        C1 =float(input("Ingrese la primera nota: "))
        C2 = float(input("Ingrese la segunda nota: "))
        if C1 >= 80 and C2 >= 80:
            print("A sido aceptado")
        else:
            print("A sido rechazado")    

    #EJEMPLO 11.
    def cuadrados(self):
        S = 0
        i = 1
        for i  in range(101):
            S = S + i
            i = i + 1
        print(S)

    #EJEMPLO 12.
    def nume(self):
        i = 0
        while i<100:   
            i = i + 1
            print(i)
    #EJEMPLO 13.
    def buc(self):
        su = 0
        p = 1
        n = "y"
        while n != "n"and n != "N":
            num = int(input("Ingresar N: "))
            su = su + num
            p = p*num
            n = input("Desea continuar(S/N)" )

        print("Total de la suma es :{}".format(p))
        print("total del producto es :{}".format(su))

    #EJEMPLO 14.
    def calc(self):
        sum = 0
        p = 1
        n = int(input("Ingrese N: "))
        while n != -1:
            sum = sum + 1
            p = p*n            
        print("Total de la suma es :{}".format(p))
        print("total del producto es :{}".format(sum))

    #EJEMPLO 15.
    def pri(self):
        pr = "True"
        div = 2
        r = float(input("Ingresar numero: "))
        while div < r and pr == "True":
            res = r % div
            if res == 0:
                pr = "False"
                div = div+1
        if pr == "True":
            print("Su numero {} es primo " .format(r))
        else:
            print("Su numero {} no es primo".format(r))

    #EJEMPLO 16.
    def metodo(self):
        from fractions import Fraction
        serie = 0
        I = 1
        r = float(input("Ingrese un numero entero: "))
        b = "T"
        # while I>r:
        for x in range (r):
            if b == "T":
                serie = serie + Fraction(1,I)
                b ="F"               
            else:
                serie = serie - Fraction(1,I)
                b = "T"
            I += 1           
        print(serie) 

    #EJEMPLO 17.
    def fac(self):
        num = float(input('Rango: '))
        for i in range(1,num+1):
            m = int(input('Numero: '))
            fctal = 1
        for j in range(1,m+1):
            fctal = fctal * j
            print(f'El factorial del numero es: {fctal}')

    #EJEMPLO 18.
    def vector(self):
        import random as rd
        promed = []
        cali = [[rd.randint(0,10)for e in range(6)]for e in range(30)]
        for i in range(30):
            sum = 0
            for j in range(6):
                sum = sum + cali[i][j]
                pd = round(sum/6,2)
            promed.append(pd)
            print(f'promedio del alumno: {i+1} : {round(sum/6,2)}')
        promed.sort(reverse=True)
        print(f'La mayor nota es: {promed[0]}')


cal1 = Ejersisios()
cal1.vector()
