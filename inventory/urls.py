from inventory.views import InventoryList, InventoryDetail
from django.urls import path

urlpatterns = (
    path('', InventoryList.as_view(), name = 'inventory-list-create'),
    path('<int:pk>/', InventoryDetail.as_view(), name = 'inventory-detail'),
)