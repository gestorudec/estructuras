class Persona:     
       
    def __init__(self,nombre,documento):
        self._nombre=nombre
        self._documento=documento
    def datos(self):
        return f"{self.nombre} {self.documento}"

objeto=Persona("Clara",123)
objeto.nombre="luz"
print(objeto.nombre)