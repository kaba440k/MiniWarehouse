
from django.urls import path, include
from .views import ProductList, ProductDetail
urlpatterns = [
    path('products/', ProductList.as_view(), name = 'product-list-create'),
    path('products/<int:pk>', ProductDetail.as_view(), name = 'product-detail'),
]