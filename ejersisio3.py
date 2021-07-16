class Sintaxis:
    instancia=0

    def __init__(self, dato="inicializacion"):
      self.frase=dato

    def usoVariable(self):
        edad, _peso = 20, 80.40
        nombre = 'Miguel Pico'
        Tipo_sexo = 'M' 
        civil = True   
        usuario=('mpicos','2324','mpicos2@gmail.com',True)
        materias = ['C++','PHP','POO']
        materias[1]="python"
        materias.append("Go")
        alumno = {'nombre':'Miguel','edad': 20,'fac':'faci'}

ejer1 = Sintaxis()
ejer1.usoVariable()
print(ejer1.frase)
