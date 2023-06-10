from rest_framework import serializers
from .models import Ilan, Resim, Transaction, Domain, Paketler


class PaketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paketler
        fields = ['adi','pozisyon']


class DomainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Domain
        fields = ['adi']


class ResimSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resim
        fields = ['ilan', 'resim_url']


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['ilan', 'tarih', 'miktar']


class IlanSerializer(serializers.ModelSerializer):
    resimler = ResimSerializer(many=True)
    transactions = TransactionSerializer(many=True)
    domain = DomainSerializer(many=True)
    paket = PaketSerializer(many=True)

    class Meta:
        model = Ilan
        fields = ['domain', 'telefon', 'meta_title', 'meta_description', 'paket', 'baslangic_tarihi', 'bitis_tarihi', 'resimler', 'transactions', 'aktif']
