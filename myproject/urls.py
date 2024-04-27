from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Index.as_view(), name='index'),
    path('edit/<int:id>/', views.Editor.as_view(), name='editor'),
    path('delete/<int:id>/', views.DeleteProduct.as_view(), name='delete_product'),
    path('create/', views.CreateProduct.as_view(), name='delete_product'),
    
]
