class Product:
    """Класс описания продуктов."""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int):
        """Передаются одноименные переменные, для дальнейшего использования как отдельно, так и в Category"""
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
