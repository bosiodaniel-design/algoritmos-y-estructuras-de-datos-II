# Materia: Algoritmos y Estructuras de Datos II
# Alumno/a: Daniel Bosio
# TP N°: 1 | Ejercicio N°: X
# Fecha de entrega: 15/04/2026
class Figura():
    def __init__(self,color):
        self.color=color
        
    def area(self):
        return 0
    
    def describir(self):
        print(f"el color es : {self.color} , y el area es : {self.area()}")
    
class Rectangulo(Figura):
    def __init__(self,color,base,altura):
         super().__init__(color)

         self.base=base
         self.altura=altura
    
    def area(self):
        ar_area=self.base*self.altura
        return ar_area


class Circulo(Figura):
    def __init__(self,color,radio):
         super().__init__(color)
         self.radio=radio

    def area(self):
        ar_area= 3.1415*self.radio**2
        return ar_area

rectangulo=Rectangulo("azul",10,45)
circulo=Circulo("rojo",15)

geo=[rectangulo,circulo]

for i in range (len(geo)):
    geo[i].describir()
       
