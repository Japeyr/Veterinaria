from django.db import models
from django.contrib.auth.models import User  # Importa el modelo de usuario de Django

class Contacto(models.Model):
    name = models.CharField(max_length=50)
    telefono = models.IntegerField()
    email = models.EmailField()
    descripcion = models.TextField()

    def __str__(self):

        return self.name

class Producto(models.Model):
    nombre = models.CharField(max_length=64)
    categoria = models.CharField(max_length=50)
    producto = models.CharField(max_length=50)
    precio = models.IntegerField()
    imagen = models.ImageField(upload_to='images/', null=True)
    cantidad_en_carrito = models.PositiveIntegerField(default=0)  # Campo para rastrear la cantidad en el carrito

    def __str__(self):
        return f'{self.nombre} => {self.precio}'

class DetalleCompra(models.Model):
    compra = models.ForeignKey('Compra', on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=0)  # Campo para rastrear la cantidad de cada producto en la compra

    def __str__(self):
        return f"DetalleCompra: {self.id}, Compra: {self.compra.id}, Producto: {self.producto.nombre}, Cantidad: {self.cantidad}"

class Compra(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_compra = models.DateTimeField(auto_now_add=True)
    metodo_pago = models.CharField(max_length=100)
    direccion_envio = models.TextField()
    monto_total = models.DecimalField(max_digits=10, decimal_places=2)

    # Relación ManyToMany a través de DetalleCompra para rastrear los productos comprados
    detalles_compra = models.ManyToManyField(Producto, through=DetalleCompra)

    def __str__(self):
        return f'Compra de {self.usuario.username} el {self.fecha_compra}'


class Factura(models.Model):
    numero_factura = models.IntegerField(unique=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_emision = models.DateTimeField(auto_now_add=True)
    # Otros campos de la factura (metodo_pago, direccion_envio, monto_total, etc.)

    def __str__(self):
        return f'Factura #{self.numero_factura}'

