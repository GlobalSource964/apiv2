from rest_framework import generics

from apiv2 import settings
from .models import Ilan, Domain, Resim, Transaction, Blog
from .permissions import ApiKeyPermission
from .serializers import IlanSerializer, DomainSerializer, ResimSerializer, TransactionSerializer, BlogSerializer


class IlanList(generics.ListCreateAPIView):
    serializer_class = IlanSerializer
    permission_classes = [ApiKeyPermission]

    def get_queryset(self):
        domain = self.request.GET.get('domain', None)
        print(domain)
        api_key = self.request.META.get('HTTP_AUTHORIZATION', '').split(' ')[-1]
        if api_key == settings.API_KEY or domain == '172.29.153.241':  # API key doğru dveya IP adresi belirli bir değerse
            return Ilan.objects.filter(aktif=True)  # Tüm aktif ilanları döndür
        else:  # API anahtar yanlış veya yoksa
            alanlar = Domain.objects.filter(adi=domain)  # Alanları çek
            if alanlar.exists():
                return Ilan.objects.filter(domain__in=alanlar, aktif=True)  # Sadece bu siteye ait ve aktif olan ilanları döndür
            else:
                return Ilan.objects.none()  # Eğer bu domain yoksa, hiç ilan döndürme

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


class BlogListCreate(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class BlogRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

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
