class Persona:     
       
    def __init__(self,nombre,documento):
        self.__nombre=nombre
        self.__documento=documento
    def datos(self):
        return f"{self.__nombre} {self.__documento}"

objeto=Persona("Clara",123)
objeto.__nombre="luz"
print(objeto.__nombre)
print(objeto.datos())

#HERENCIA EN P.O.O CON PYTHON
class Estudiante(Persona):
    def __init__(self, nombre, documento,carrera):
        super().__init__(nombre, documento)
        self.__carrera=carrera
    def datos(self):
        return super().datos()+" "+self.__carrera


e1=Estudiante("Mary",333,"Sistemas")
print(e1.datos())