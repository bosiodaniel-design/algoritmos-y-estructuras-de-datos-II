# Materia: Algoritmos y Estructuras de Datos II
# Alumno/a: Daniel Bosio
# TP N°: 1 | Ejercicio N°: 1
# Fecha de entrega: 15/04/2026

class Vehiculo():
    def __init__(self,marca,velocidad_max ):
        self.marca=marca
        self.velocidad_max=velocidad_max

    def describir(self):
        print(f"la marca es : {self.marca}  y su velocidad maxima es de : {self.velocidad_max} km/h")

        
class Auto(Vehiculo):
    def __init__(self,marca,velocidad_max):
        super().__init__(marca,velocidad_max)


    def describir(self):
        print(f"la marca del auto es : {self.marca}  y su velocidad maxima es de : {self.velocidad_max} km/h")

    
class Moto(Vehiculo):
    def __init__(self,marca,velocidad_max):
        super().__init__(marca,velocidad_max)

    def describir(self):
        print(f"la marca de la moto es : {self.marca}  y su velocidad maxima es de : {self.velocidad_max} km/h")

        


auto=Vehiculo("ford","180")
auto.describir()
auto=Auto("fiat","100")
auto.describir()
moto=Vehiculo("honda","250")
moto.describir()
moto=Moto("zanella","250")
moto.describir()


lista=[auto,moto]
print(lista)
for i in range(len(lista)):
    lista[i].describir()
    
