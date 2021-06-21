class For:
    def __init__(self):
        pass

    def usoFor(self): 
        datos=["Miguel",20,True]
        numeros=(2,5.6,4,1)
        docente={'nombre': 'Miguel','edad':20,'fac':'faci'}
        listaNotas=[(20,50),(40,40),(50,50)]
        listaAlumno=[{"nombre":"Erick","final":70},{"nombre":"Paola","final":80},{"nombre":"Janina","final":100}]
        # for i in range(5):
        #     print("i={}".format(i))
        # for i in range(2,10):
        #     print("i={}".format(i))   
        # for i in range(4,10,2):
        #     print("i={}".format(i),end=" ") 
        # for i in range(12,3,-3):
        #     print("i={}".format(i),end=" ")   
            
        #longitud = len(datos)    
        #     print(datos[0]) 
        #     print(datos[1])
        #     print(datos[2])
            # j=0
            # while j < longitud:
            #     print("while",datos[j])
            #     j=j+1
        # for i in range(longitud-1,-1,-1):
        #     print("for",datos[i])
        
        #for i,datos in enumerate(numeros):
        #    print("for",i,datos)

        #for datos in numeros:
        #    print(datos)    
        
        # print("\nDiccionario de notas")
        #  for alumno in listaAlumno:
        #         print(clave,":",valor,end=" ")
        
        # for alumno in listaAlumno:
        #     for clave,valor in alumno.items():
        #         print(clave,":",valor,end=" ")

        # listaNotas = [(30,40),(20,40,20),(50,40,20,10,5)]
        # acum=0
        # long=0
        # for notas in listaNotas:
        #     parcial=0
        #     print(notas,end=" ")
        #     for nota in notas:
        #       print(nota)
        #       long=long+1
        #       acum = acum + nota
        #       parcial += nota
        # promParcial = parcial/len(notas)
        # print("Notas Parciales={} Promedio Parcial={}".format(promParcial))
        # prom = acum/long
        # print("Total notas={} - Notas={}: Promedio={} ".format(acum,long,prom))        
            
        listaAlumno=[{"nombre":"Erick","final":70},{"nombre":"Paola","final":80},{"nombre":"Janina","final":100}]
        for alumno in listaAlumno:
             for clave,valor in alumno.items():
                 print(clave,":",valor,end=" ")    


bucle1= For() 
bucle1.usoFor()


             