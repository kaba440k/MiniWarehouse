from django.urls import path

from .views import StorageList, StorageDetail

urlpatterns = [
    path('', StorageList.as_view(), name = 'storage-list-create'),
    path('<int:pk>/', StorageDetail.as_view(), name = 'storage-detail'),
]