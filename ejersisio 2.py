listaNotas = [(30,40),(20,40,20),(50,40,20,10,5)]
acum=0
long=0
for notas in listaNotas:
    parcial=0
    print(notas,end=" ")
    for nota in notas:
        print(nota)
        long=long+1
        acum = acum + nota
        parcial += nota
    promParcial = parcial/len(notas)
    print("Notas Parciales={} Promedio Parcial={}".format(promParcial))
prom = acum/long
print("Total notas={} - Notas={}: Promedio={} ".format(acum,long,prom))


