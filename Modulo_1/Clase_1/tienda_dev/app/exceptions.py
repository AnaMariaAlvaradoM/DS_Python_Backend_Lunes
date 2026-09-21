class CategoriaNoEncontrada(Exception):
    def __init__(self, categoria_id: int):
        self.categoria_id = categoria_id
        super().__init__(f"La categoría con id {categoria_id} no existe")


class ProveedorNoEncontrado(Exception):
    def __init__(self, proveedor_id: int):
        self.proveedor_id = proveedor_id
        super().__init__(f"El proveedor con id {proveedor_id} no existe")