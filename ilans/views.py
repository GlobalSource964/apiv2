from rest_framework import generics
from apiv2 import settings
from .models import Ilan, Domain, Resim, Transaction, Blog
from .permissions import ApiKeyPermission
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from .serializers import IlanSerializer, DomainSerializer, ResimSerializer, TransactionSerializer, BlogSerializer, \
    DomainSerializerBacklink


@method_decorator(cache_page(60*60*2), name='get')  # Cache for 2 hours
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


@method_decorator(cache_page(60*60*2), name='get')  # Cache for 2 hours
class IlanDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ilan.objects.all()
    serializer_class = IlanSerializer
    permission_classes = [ApiKeyPermission]


@method_decorator(cache_page(60*60*2), name='get')  # Cache for 2 hours
class DomainList(generics.ListCreateAPIView):
    queryset = Domain.objects.all()
    serializer_class = DomainSerializer
    permission_classes = [ApiKeyPermission]


@method_decorator(cache_page(60*60*2), name='get')  # Cache for 2 hours
class DomainListbacklink(generics.ListCreateAPIView):
    queryset = Domain.objects.all()
    serializer_class = DomainSerializerBacklink
    permission_classes = [ApiKeyPermission]


@method_decorator(cache_page(60*60*2), name='get')  # Cache for 2 hours
class DomainDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Domain.objects.all()
    serializer_class = DomainSerializer
    permission_classes = [ApiKeyPermission]


@method_decorator(cache_page(60*60*2), name='get')  # Cache for 2 hours
class BlogListCreate(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


@method_decorator(cache_page(60*60*2), name='get')  # Cache for 2 hours
class BlogRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


@method_decorator(cache_page(60*60*2), name='get')  # Cache for 2 hours
class ResimList(generics.ListCreateAPIView):
    queryset = Resim.objects.all()
    serializer_class = ResimSerializer
    permission_classes = [ApiKeyPermission]


@method_decorator(cache_page(60*60*2), name='get')  # Cache for 2 hours
class ResimDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Resim.objects.all()
    serializer_class = ResimSerializer
    permission_classes = [ApiKeyPermission]


@method_decorator(cache_page(60*60*2), name='get')  # Cache for 2 hours
class TransactionList(generics.ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [ApiKeyPermission]


@method_decorator(cache_page(60*60*2), name='get')  # Cache for 2 hours
class TransactionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [ApiKeyPermission]
