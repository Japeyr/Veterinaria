from django.contrib import admin
from .models import Contacto, Producto, Compra, DetalleCompra, User

class AdminUser(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'last_name']

    class Meta:
        model = User

class AdminProducto(admin.ModelAdmin):
    list_display = ['nombre', 'categoria', 'producto', 'precio', 'cantidad_en_carrito']

    class Meta:
        model = Producto

class AdminDetalleCompra(admin.ModelAdmin):
    list_display = ['producto', 'cantidad']

    class Meta:
        model = DetalleCompra

class DetalleCompraInline(admin.TabularInline):
    model = DetalleCompra
    extra = 0  # Para no mostrar campos en blanco adicionales



class AdminCompra(admin.ModelAdmin):
    list_display = ['id', 'usuario', 'metodo_pago', 'direccion_envio', 'mostrar_productos_comprados']

    inlines = [DetalleCompraInline]  # Muestra los detalles de la compra en línea

    def mostrar_productos_comprados(self, obj):
        # Genera una lista de productos comprados en esta compra junto con las cantidades
        productos_comprados = [
            f"{detalle}"
            for detalle in obj.detalles_compra.all()
        ]
        return ', '.join(productos_comprados)

    mostrar_productos_comprados.short_description = 'Productos Comprados'  # Encabezado personalizado

    class Meta:
        model = Compra



# Register your models here
admin.site.register(Contacto)
admin.site.register(Producto, AdminProducto)
admin.site.register(Compra, AdminCompra)
admin.site.register(DetalleCompra, AdminDetalleCompra)
