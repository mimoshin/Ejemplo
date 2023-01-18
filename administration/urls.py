from django.urls import path
from .views import vistaPrincipal, vistaHola

urlpatterns = [
    path('', vistaPrincipal, name='vista_principal'),
    path('hola', vistaHola, name='saludar'),
    
]


"""
        REVISAR FORMATO DE URLS
            path('url_name', vista_utlizada, name='tag_name' )
"""