from django.contrib.auth import authenticate, login
from django.contrib.auth import logout  # Importa la función de cierre de sesión
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from .Carrito import CarritoCompras
from .forms import ContactoForm, RegistroForm, CompraForm
from .models import Producto, DetalleCompra, Compra
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from django.db import transaction


@login_required
def profile(request):
    # Aquí puedes mostrar la información del usuario
    return render(request, 'perfil.html')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirigir a la página deseada después del inicio de sesión (por ejemplo, 'index')
                return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'base/HTML5/doc/login/doc/login.html', {'form': form})

def vista_de_salida(request):
    # Cierra la sesión del usuario
    logout(request)

    # Redirige al usuario a la página de inicio o a donde desees
    return redirect('login')

class Registro(FormView):
    template_name = "base/HTML5/doc/login/doc/registro.html"
    form_class = RegistroForm
    success_url = reverse_lazy('ofertas')

    def form_valid(self, form):
        usuario = form.save()
        if usuario is not None:
            login(self.request, usuario)
        return super(Registro, self).form_valid(form)

def index(request):
    return render(request, 'base/HTML5/index.html')

def info(request):
    return render(request, 'base/HTML5/doc/Info/doc/info.html')

def info1(request):
    return render(request, 'base/HTML5/doc/Info/doc/info1.html')


def info2(request):
    return render(request, 'base/HTML5/doc/Info/doc/info2.html')


def info3(request):
    return render(request, 'base/HTML5/doc/Info/doc/info3.html')


def info4(request):
    return render(request, 'base/HTML5/doc/Info/doc/info4.html')


def consejos(request):
    return render(request, 'base/HTML5/doc/Consejos/doc/Consejos.html')


def consejo1(request):
    return render(request, 'base/HTML5/doc/Consejos/doc/Consejo1.html')


def consejo2(request):
    return render(request, 'base/HTML5/doc/Consejos/doc/Consejo2.html')


def consejo3(request):
    return render(request, 'base/HTML5/doc/Consejos/doc/Consejo3.html')


def consejo4(request):
    return render(request, 'base/HTML5/doc/Consejos/doc/Consejo4.html')


def consejo5(request):
    return render(request, 'base/HTML5/doc/Consejos/doc/Consejo5.html')


def consejo6(request):
    return render(request, 'base/HTML5/doc/Consejos/doc/Consejo6.html')


def consejo7(request):
    return render(request, 'base/HTML5/doc/Consejos/doc/Consejo7.html')


def consejo8(request):
    return render(request, 'base/HTML5/doc/Consejos/doc/Consejo8.html')

def ofertas(request):
    return render(request, 'base/HTML5/doc/ofertas/doc/ofertas.html')

def contacto(request):
    data = {
        'form': ContactoForm()
    }

    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            data["mensaje"] = "Mensaje Enviado"
        else:
            data["form"] = form

    return render(request, 'base/HTML5/doc/formulario/doc/formulario.html', data)


def tienda(request):
    productos = Producto.objects.all()
    return render(request, "perfil", {'productos': productos})

def ofertas1(request):
    productos = Producto.objects.all()
    return render(request, 'base/HTML5/doc/ofertas/doc/OFERTAS1.HTML', {'productos': productos})

def ofertas2(request):
    productos = Producto.objects.all()
    return render(request, 'base/HTML5/doc/ofertas/doc/OFERTAS2.HTML', {'productos': productos})

def ofertas3(request):
    productos = Producto.objects.all()
    return render(request, 'base/HTML5/doc/ofertas/doc/OFERTAS3.HTML', {'productos': productos})

def ofertas4(request):
    productos = Producto.objects.all()
    return render(request, 'base/HTML5/doc/ofertas/doc/OFERTAS4.HTML', {'productos': productos})

def alimentogatos(request):
    return render(request, 'base/HTML5/doc/alimentogatos/doc/ALIMENTOGATOS.HTML')

def alimentogatos1(request):
    productos = Producto.objects.all()
    return render(request, 'base/HTML5/doc/alimentogatos/doc/ALIMENTOGATOS1.HTML', {'productos': productos})

def alimentogatos2(request):
    productos = Producto.objects.all()
    return render(request, 'base/HTML5/doc/alimentogatos/doc/ALIMENTOGATOS2.html', {'productos': productos})

def alimentogatos3(request):
    productos = Producto.objects.all()
    return render(request, 'base/HTML5/doc/alimentogatos/doc/ALIMENTOGATOS3.html', {'productos': productos})

def alimentogatos4(request):
    productos = Producto.objects.all()
    return render(request, 'base/HTML5/doc/alimentogatos/doc/ALIMENTOGATOS4.html', {'productos': productos})

def alimentoperros(request):
    return render(request, 'base/HTML5/doc/alimentoperros/doc/ALIMENTOPERROS.HTML')

def alimentoperros1(request):
    productos = Producto.objects.all()
    return render(request, 'base/HTML5/doc/alimentoperros/doc/ALIMENTOPERROS1.HTML', {'productos': productos})

def alimentoperros2(request):
    productos = Producto.objects.all()
    return render(request, 'base/HTML5/doc/alimentoperros/doc/ALIMENTOPERROS2.HTML', {'productos': productos})

def alimentoperros3(request):
    productos = Producto.objects.all()
    return render(request, 'base/HTML5/doc/alimentoperros/doc/ALIMENTOPERROS3.HTML', {'productos': productos})

def alimentoperros4(request):
    productos = Producto.objects.all()
    return render(request, 'base/HTML5/doc/alimentoperros/doc/ALIMENTOPERROS4.HTML', {'productos': productos})

def bocaditos(request):
    return render(request, 'base/HTML5/doc/bocaditos/doc/BOCADITOS.HTML')

def bocaditos1(request):
    productos = Producto.objects.all()
    return render(request, 'base/HTML5/doc/bocaditos/doc/BOCADITOS1.HTML', {'productos': productos})

def bocaditos2(request):
    productos = Producto.objects.all()
    return render(request, 'base/HTML5/doc/bocaditos/doc/BOCADITOS2.HTML', {'productos': productos})

def bocaditos3(request):
    productos = Producto.objects.all()
    return render(request, 'base/HTML5/doc/bocaditos/doc/BOCADITOS3.HTML', {'productos': productos})

def bocaditos4(request):
    productos = Producto.objects.all()
    return render(request, 'base/HTML5/doc/bocaditos/doc/BOCADITOS4.HTML', {'productos': productos})

def accesorios(request):
    return render(request, 'base/HTML5/doc/accesorios/doc/ACCESORIOS.HTML')

def accesorios1(request):
    productos = Producto.objects.all()
    return render(request, 'base/HTML5/doc/accesorios/doc/ACCESORIO1.HTML', {'productos': productos})

def accesorios2(request):
    productos = Producto.objects.all()
    return render(request, 'base/HTML5/doc/accesorios/doc/ACCESORIO2.html', {'productos': productos})

def accesorios3(request):
    productos = Producto.objects.all()
    return render(request, 'base/HTML5/doc/accesorios/doc/ACCESORIO3.HTML', {'productos': productos})

def accesorios4(request):
    productos = Producto.objects.all()
    return render(request, 'base/HTML5/doc/accesorios/doc/ACCESORIO4.html', {'productos': productos})

def perfil(request):
    return render(request, 'base/perfil.html')

def agregar_producto(request, producto_id):
    carrito = CarritoCompras(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.agregar(producto)
    return redirect("perfil")


def eliminar_producto(request, producto_id):
    carrito = CarritoCompras(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.eliminar(producto)
    return redirect("perfil")


def restar_producto(request, producto_id):
    carrito = CarritoCompras(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.restar(producto)
    return redirect("perfil")


def limpiar_carrito(request):
    carrito = CarritoCompras(request)
    carrito.limpiar()
    return redirect("perfil")

@login_required
def pago(request):
    carrito = CarritoCompras(request)

    if request.method == 'POST':
        compra_form = CompraForm(request.POST)
        if compra_form.is_valid():
            # Obtener los datos del formulario de compra
            usuario = request.user
            metodo_pago = compra_form.cleaned_data['metodo_pago']
            direccion_envio = compra_form.cleaned_data['direccion_envio']

            # Obtener los productos seleccionados del carrito junto con sus cantidades
            productos_seleccionados = []
            for producto_id, producto_info in carrito.carrito.items():
                producto = Producto.objects.get(id=producto_id)
                cantidad = producto_info['cantidad']
                productos_seleccionados.append((producto, cantidad))

            # Realizar la transacción de compra dentro de una transacción de base de datos
            with transaction.atomic():
                compra = Compra.objects.create(
                    usuario=usuario,
                    metodo_pago=metodo_pago,
                    direccion_envio=direccion_envio,
                    monto_total=carrito.total_carrito()
                )

                for producto, cantidad in productos_seleccionados:
                    DetalleCompra.objects.create(
                        compra=compra,
                        producto=producto,
                        cantidad=cantidad  # Guardar la cantidad en el detalle de compra
                    )

                    # Actualizar la cantidad en el modelo Producto
                    producto.cantidad_en_carrito -= cantidad
                    producto.save()

                # Limpiar el carrito después de completar la compra
                carrito.limpiar()

            return render(request, 'compra_exitosa.html')
    else:
        compra_form = CompraForm()

    return render(request, 'pago.html', {'compra_form': compra_form, 'carrito': carrito})


def compra_exitosa(request):
    # Puedes realizar cualquier lógica adicional aquí, como enviar correos electrónicos de confirmación, etc.
    # Por ejemplo, si deseas mostrar los detalles de la compra en la página de confirmación, puedes obtener la información de la compra desde la sesión o la base de datos.

    # Luego, renderiza la página de confirmación
    return render(request, 'compra_exitosa.html')

# Inicializa el contador en 1 al inicio de la aplicación
contador_facturas = 1

def generar_numero_factura():
    global contador_facturas
    numero_factura = contador_facturas
    contador_facturas += 1
    return numero_factura

@login_required
def factura(request):
    # Obtener la compra más reciente del usuario
    usuario = request.user

    try:
        compra = Compra.objects.filter(usuario=usuario).latest('fecha_compra')
        # Obtener los detalles de la compra
        detalles_compra = DetalleCompra.objects.filter(compra=compra)

        # Obtener los productos correspondientes a los detalles de la compra
        productos_comprados = [(detalle.producto, detalle.cantidad) for detalle in detalles_compra]
    except Compra.DoesNotExist:
        return HttpResponse("No tienes compras recientes.")

    # Crear un objeto HttpResponse
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="factura.pdf"'

    # Crear el objeto PDF con ReportLab
    p = canvas.Canvas(response)
    w, h = A4

    # Generar un número de factura único
    numero_factura = generar_numero_factura()
    numero_factura_str = str(numero_factura).zfill(8)
    # Crear el objeto PDF con ReportLab
    p = canvas.Canvas(response)
    w, h = A4


    p.setFont("Helvetica", 12)
    p.drawString(263, 822, "ORIGINAL")
    p.drawString(10, 790, "TIENDA DE MASCOTAS - PERROS Y GATOS")
    p.drawString(420, 790, "Factura A")
    p.drawString(100, 740, "San Juan 531 - Rosario")
    p.drawString(392, 760, f"Nº 0001-{numero_factura_str}")
    p.drawString(100, 725, "Santa Fe - Argentina")
    p.drawString(20, 700, "Condición frente al iva: Responsable Monotributo")
    p.drawString(392, 745, "Fecha Emisión: 21/09/2023")
    p.drawString(392, 720, "Cuit: 25-16945277-3")
    p.drawString(392, 705, "Ing. Brutos: 902-7232632")
    p.drawString(392, 690, "Inicio de Actividad: 25/04/2005")
    # Datos del cliente en la factura
    p.drawString(20, 635, "Cuit:")
    p.drawString(200, 635, f'Nombre y Apellido/ Razón Social: {usuario.first_name} {usuario.last_name}')
    p.drawString(20, 615, "Condición frente al IVA: Consumidor Final")
    p.drawString(300, 605, f'Domicilio: {compra.direccion_envio}')
    p.drawString(20, 595, "Condición de venta: Contado")

    # Primera Linea
    x = 0
    y = h - 30

    p.line(x, y, x + 596, y)
    p.drawString(290, 790, "C")

    # Segunda Linea
    y = h - 180
    p.line(x, y, x + 596, y)

    # Tercera Linea
    y = h - 300
    x = 10
    p.line(x, y, x + 575, y)

    # Rectángulo tipo de factura.

    p.rect(280, h - 61, 30, 30)

    # Rectangulo cuerpo factura
    p.rect(10, h - 800, 575, 530)

    # Linea vertical
    x1 = 298
    y1 = h - 61
    p.line(x1, y1, x1 + 0, 662)

    # Dibuja los encabezados de la tabla para Unidades, Descripción, Precio e Importe
    p.drawString(20, 555, "Unidades")
    p.drawString(170, 555, "Descripción")
    p.drawString(380, 555, "Precio")
    p.drawString(490, 555, "Importe")

    # Dibuja la lista de productos comprados
    y_posicion = 530  # Ajusta la posición y inicial según sea necesario

    for producto, cantidad in productos_comprados:
        nombre = producto.nombre
        precio = producto.precio
        acumulado = precio * cantidad

        # Dibuja los datos en las celdas de la tabla
        p.drawString(20, y_posicion, str(cantidad))
        p.drawString(50, y_posicion, nombre)
        p.drawString(380, y_posicion, str(precio))
        p.drawString(490, y_posicion, str(acumulado))

        # Actualiza la posición Y para la próxima fila
        y_posicion -= 20  # Puedes ajustar el espaciado según sea necesario

    # Dibuja el total
    total = compra.monto_total
    p.drawString(370, y_posicion - 20, "Total:")
    p.drawString(480, y_posicion - 20, str(total))

    # Cierra la sesión del usuario después de descargar la factura
    logout(request)

    # Finalizar y guardar el PDF
    p.showPage()
    p.save()

    return response

