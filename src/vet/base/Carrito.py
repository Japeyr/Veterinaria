class CarritoCompras:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("carrito")
        if not carrito:
            self.session["carrito"] = {}
            self.carrito = self.session["carrito"]
        else:
            self.carrito = carrito


    def agregar(self, producto):
        id = str(producto.id)
        if id not in self.carrito.keys():
            self.carrito[id] = {
                "producto_id": producto.id,
                "nombre": producto.nombre,
                "precio": producto.precio,
                "acumulado": producto.precio,
                "cantidad": 1,
                "imagen": producto.imagen.url,
            }
            producto.cantidad_en_carrito = 1
            producto.save()  # Actualizar la cantidad en el modelo Producto
        else:
            self.carrito[id]["cantidad"] += 1
            self.carrito[id]["precio"] = producto.precio
            self.carrito[id]["acumulado"] += producto.precio
            producto.cantidad_en_carrito += 1
            producto.save()  # Actualizar la cantidad en el modelo Producto
        self.guardar_carrito()

    def guardar_carrito(self):
        self.session['carrito'] = self.carrito
        self.session.modified = True

    def eliminar(self, producto):
        id = str(producto.id)
        if id in self.carrito:
            del self.carrito[id]
            self.guardar_carrito()


    def restar(self, producto):
        id = str(producto.id)
        if id in self.carrito.keys():
            if self.carrito[id]["cantidad"] > 1:
                self.carrito[id]["cantidad"] -= 1
                self.carrito[id]["acumulado"] -= producto.precio
            else:
                self.eliminar(producto)
            self.guardar_carrito()

    def limpiar(self):
        self.session['carrito'] = {}
        self.session.modified = True

    def total_carrito(self):
        total = 0
        if self.request.user.is_authenticated:
            if self.carrito:
                for item in self.carrito.values():
                    total += item['acumulado']
        return total
