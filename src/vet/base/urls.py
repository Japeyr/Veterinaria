from django.urls import path
from django.contrib.auth.views import LoginView
from . import views
from .views import index, info, consejos, info1, info2, info3, info4, consejo1, consejo2, consejo3, consejo4, \
    consejo5, consejo6, consejo7, consejo8, ofertas, ofertas1, ofertas2, ofertas3, ofertas4, alimentogatos, \
    alimentogatos1, alimentogatos2, alimentogatos3, alimentogatos4, alimentoperros, alimentoperros1, alimentoperros2, \
    alimentoperros3, alimentoperros4, bocaditos, bocaditos1, bocaditos2, bocaditos3, bocaditos4, accesorios, \
    accesorios1, accesorios2, accesorios3, accesorios4, Registro
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', index, name='index'),  # Ruta para la vista index
    path('doc/Info/doc/info.html', info, name="info"),  # Ruta para la vista informacion
    path('doc/Info/doc/info1.html', info1, name="info1"),
    path('doc/Info/doc/info2.html', info2, name="info2"),
    path('doc/Info/doc/info3.html', info3, name="info3"),
    path('doc/Info/doc/info4.html', info4, name="info4"),
    path('doc/Consejos/doc/Consejos.html', consejos, name="consejos"),  # Ruta para la vista consejos
    path('doc/Consejos/doc/Consejo1.html', consejo1, name="consejo1"),
    path('doc/Consejos/doc/Consejo2.html', consejo2, name="consejo2"),
    path('doc/Consejos/doc/Consejo3.html', consejo3, name="consejo3"),
    path('doc/Consejos/doc/Consejo4.html', consejo4, name="consejo4"),
    path('doc/Consejos/doc/Consejo5.html', consejo5, name="consejo5"),
    path('doc/Consejos/doc/Consejo6.html', consejo6, name="consejo6"),
    path('doc/Consejos/doc/Consejo7.html', consejo7, name="consejo7"),
    path('doc/Consejos/doc/Consejo8.html', consejo8, name="consejo8"),
    path('doc/formulario/doc/formulario.html', views.contacto, name="contacto"),  # Ruta para la vista del formulario
    path('tienda/', views.tienda, name='tienda'),
    path('agregar/<int:producto_id>/', views.agregar_producto, name='agregar_producto'),
    path('eliminar/<int:producto_id>/', views.eliminar_producto, name='eliminar_producto'),
    path('restar/<int:producto_id>/', views.restar_producto, name='restar_producto'),
    path('limpiar/', views.limpiar_carrito, name='limpiar_carrito'),
    path('doc/ofertas/doc/ofertas.html', ofertas, name="ofertas"),
    path('doc/ofertas/doc/OFERTAS1.HTML', ofertas1, name="ofertas1"),
    path('doc/ofertas/doc/OFERTAS2.HTML', ofertas2, name="ofertas2"),
    path('doc/ofertas/doc/OFERTAS3.HTML', ofertas3, name="ofertas3"),
    path('doc/ofertas/doc/OFERTAS4.HTML', ofertas4, name="ofertas4"),
    path('doc/alimentogatos/doc/ALIMENTOGATOS.HTML', alimentogatos, name="alimentogatos"),  # Ruta para la vista alimento gatos
    path('doc/alimentogatos/doc/ALIMENTOGATOS1.HTML', alimentogatos1, name="alimentogatos1"),
    path('doc/alimentogatos/doc/ALIMENTOGATOS2.html', alimentogatos2, name="alimentogatos2"),
    path('doc/alimentogatos/doc/ALIMENTOGATOS3.html', alimentogatos3, name="alimentogatos3"),
    path('doc/alimentogatos/doc/ALIMENTOGATOS4.html', alimentogatos4, name="alimentogatos4"),
    path('doc/alimentoperros/doc/ALIMENTOPERROS.HTML', alimentoperros, name="alimentoperros"),  # Ruta para la vista alimento perros
    path('doc/alimentoperros/doc/ALIMENTOPERROS1.HTML', alimentoperros1, name="alimentoperros1"),
    path('doc/alimentoperros/doc/ALIMENTOPERROS2.html', alimentoperros2, name="alimentoperros2"),
    path('doc/alimentoperros/doc/ALIMENTOPERROS3.html', alimentoperros3, name="alimentoperros3"),
    path('doc/alimentoperros/doc/ALIMENTOPERROS4.html', alimentoperros4, name="alimentoperros4"),
    path('doc/bocaditos/doc/BOCADITOS.HTML', bocaditos, name="bocaditos"),  # Ruta para la vista bocadito
    path('doc/bocaditos/doc/BOCADITOS1.HTML', bocaditos1, name="bocaditos1"),
    path('doc/bocaditos/doc/BOCADITOS2.HTML', bocaditos2, name="bocaditos2"),
    path('doc/bocaditos/doc/BOCADITOS3.HTML', bocaditos3, name="bocaditos3"),
    path('doc/bocaditos/doc/BOCADITOS4.HTML', bocaditos4, name="bocaditos4"),
    path('doc/accesorios/doc/ACCESORIOS.HTML', accesorios, name="accesorios"),  # Ruta para la vista accesorios
    path('doc/accesorios/doc/ACCESORIO1.HTML', accesorios1, name="accesorio1"),
    path('doc/accesorios/doc/ACCESORIO2.html', accesorios2, name="accesorio2"),
    path('doc/accesorios/doc/ACCESORIO3.HTML', accesorios3, name="accesorio3"),
    path('doc/accesorios/doc/ACCESORIO4.html', accesorios4, name="accesorio4"),
    path('perfil/', views.profile, name='perfil'),  # Ruta para la vista de perfil personalizada
    # Ruta para la vista de inicio de sesión
    path('doc/login/doc/login.html', LoginView.as_view(template_name='base/HTML5/doc/login/doc/login.html'), name='login'),
    path('doc/login/doc/registro.html', Registro.as_view(), name='registro'),
    # Ruta para la vista de cierre de sesión
    path('cerrar-sesion/', views.vista_de_salida, name='cerrar_sesion'),  # Nueva ruta para cerrar sesión
    path('compra_exitosa.html', views.compra_exitosa, name='compra_exitosa'),
    path('pago/', views.pago, name='pago'),
    path('factura/', views.factura, name='factura'),
    ]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

