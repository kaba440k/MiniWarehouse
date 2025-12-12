from django.urls import path

from products.views import ProductList


from .views import TransactionList, TransactionDetail

urlpatterns = [
    path('', TransactionList.as_view(), name = 'transaction-list-create'),
    path('<int:pk>/', TransactionDetail.as_view(), name = 'transaction-detail'),
]