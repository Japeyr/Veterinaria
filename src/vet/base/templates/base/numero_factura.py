aumulado= 0
el_numero = None
class Cuenta:

    def __init__(self, numero, total):
        super().__init__(numero)
        self.numero = numero
        self.total = total

    def sumar(self):
        self.total = self.total + 1

    def __str__(self):
        return f"Nº de factura: {self.total}"

