from django.urls import path
from .views import IlanList, IlanDetail, DomainList, DomainDetail, ResimList, ResimDetail, TransactionList, TransactionDetail

urlpatterns = [
    path('ilanlar', IlanList.as_view(), name='ilan-list'),
    path('ilanlar/<int:pk>', IlanDetail.as_view(), name='ilan-detail'),
    path('domain', DomainList.as_view(), name='domain-list'),
    path('domain/<int:pk>', DomainDetail.as_view(), name='domain-detail'),
    path('resim', ResimList.as_view(), name='resim-list'),
    path('resim/<int:pk>', ResimDetail.as_view(), name='resim-detail'),
    path('transaction', TransactionList.as_view(), name='transaction-list'),
    path('transaction/<int:pk>', TransactionDetail.as_view(), name='transaction-detail'),
]
