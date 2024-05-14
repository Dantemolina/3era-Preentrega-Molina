
class Articulo:
    def __init__(self,producto, precio, descripcion) -> None:
        self.producto = producto
        self.precio = precio
        self.descripcion = descripcion
        
    def __str__(self) -> str:
        return f"{self.nombre}: ${self.precio}"

    def __repr__(self) -> str:
        return f"{self.nombre}: ${self.precio}"

class Pedido():
    def __init__(self, producto: str, precio: float, descripción: str) -> None:
        super().__init__(producto, precio, descripción)
    def __str__(self) -> str:
         return f"{self.producto}, {self.precio}, {self.descripcion}"
    def __repr__(self) -> str:
        return f"{self.producto}, {self.precio}, {self.descripcion}"

