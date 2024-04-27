from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect
from django.views import View
from myapp.models import Products
from django.core.paginator import Paginator
 
# Create your views here.


@method_decorator(csrf_exempt, name="dispatch")
class Index(View):
    
    def get(self, request):
        

        productos = Products.objects.all().order_by('id')

        paginator = Paginator(productos, 50)
        page_number =request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        contexto = {'productos': productos, 'page_obj' : page_obj}
    
        return render(request,'index.html', contexto)

@method_decorator(csrf_exempt, name="dispatch")
class Editor(View):

    def get(self, request, id):

        producto = Products.objects.get(id=id)

        return render(request,'edit.html', context={'producto' : producto})
    def post(self, request, id):
        id = request.POST.get('id')
        newnombre = request.POST.get('name')
        newprecio = request.POST.get('precio')
        newstock = request.POST.get('stock')
        gratuito = request.POST.get('gratuito')

        if gratuito == None:
            gratuito = False
        else:
            gratuito = True

        producto= Products.objects.get(id = id)
        producto.nombre_producto = newnombre
        producto.precio = newprecio
        producto.stock = newstock
        producto.esGratuito = gratuito
        producto.save()
        return render(request,'edit.html', context={'producto' : producto})
        
            
          

            