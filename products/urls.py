from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('detail/', views.product_detail, name='product_detail'),
    path('products/', views.products, name='products'),
]