
class Cliente:
    def __init__(self, nombre, apellido, correo_electrónico):
        self.nombre = nombre
        self.apellido = apellido
        self.correo_electrónico = correo_electrónico
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Usuario(Cliente):
    def __init__(self, nombre: str, apellido: str, correo_electrónico: str) -> None:
        super().__init__(nombre, apellido, correo_electrónico)
    
    def __str__(self) -> str:
        return f"{self.nombre}, {self.apellido}"
    
    def __repr__(self) -> str:
        return f"{self.nombre}, {self.apellido}"


