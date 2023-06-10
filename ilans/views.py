from rest_framework import generics

from apiv2 import settings
from .models import Ilan, Domain, Resim, Transaction
from .permissions import ApiKeyPermission
from .serializers import IlanSerializer, DomainSerializer, ResimSerializer, TransactionSerializer


class IlanList(generics.ListCreateAPIView):
    serializer_class = IlanSerializer
    permission_classes = [ApiKeyPermission]

    def get_queryset(self):
        if self.request.META['HTTP_HOST'] == '25.70.54.23':
            return Ilan.objects.filter(aktif=True)
        else:
            domain = self.request.META['HTTP_HOST']
        api_key = self.request.META.get('HTTP_AUTHORIZATION', '').split(' ')[-1]
        if api_key == settings.API_KEY:  # API anahtar doğruysa
            return Ilan.objects.filter(aktif=True)  # Tüm aktif ilanları döndür
        else:  # API anahtar yanlış veya yoksa
            alan = Domain.objects.filter(adi=domain)
            return Ilan.objects.filter(domain=alan.adi, aktif=True)  # Sadece bu siteye ait ilanları döndür


class IlanDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ilan.objects.all()
    serializer_class = IlanSerializer
    permission_classes = [ApiKeyPermission]


class DomainList(generics.ListCreateAPIView):
    queryset = Domain.objects.all()
    serializer_class = DomainSerializer
    permission_classes = [ApiKeyPermission]


class DomainDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Domain.objects.all()
    serializer_class = DomainSerializer
    permission_classes = [ApiKeyPermission]


class ResimList(generics.ListCreateAPIView):
    queryset = Resim.objects.all()
    serializer_class = ResimSerializer
    permission_classes = [ApiKeyPermission]


class ResimDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Resim.objects.all()
    serializer_class = ResimSerializer
    permission_classes = [ApiKeyPermission]


class TransactionList(generics.ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [ApiKeyPermission]


class TransactionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [ApiKeyPermission]
