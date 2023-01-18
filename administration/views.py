from django.shortcuts import render, HttpResponse
from django.http.response import JsonResponse

# Create your views here.
def vistaPrincipal(request):
    """
        REVISAR FORMATO PRINCIPAL DE UNA VISTA
            
            def nombre_vista(request, args*, kwargs**):
                ...cualquier logica que quieras hacer...
                ...cualquier logica que quieras hacer...
                ...cualquier logica que quieras hacer...    
                
                opcion 1:
                return render(request, template_name, kwargs**) PARA RETORNAR UNA VISTA HTML
                
                opcion 2:
                return HttpResponse(args*)
                return JsonResponse(args*)
                return OTRA_VISTA(request, args*, kwargs*)
    """
    return render(request,'index.html',{'dato_1':'Hola','dato_2':1})


def vistaHola(request):
    return HttpResponse('VISTA HOLA')