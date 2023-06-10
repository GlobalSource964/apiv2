from django.contrib import admin
from .models import Ilan, Resim, Transaction, Domain, Paketler
# Ilan modelini admin paneline ekleyin


class PaketAdmin(admin.ModelAdmin):
    list_display = ['id', 'adi', 'pozisyon']


admin.site.register(Paketler, PaketAdmin)


class DomainAdmin(admin.ModelAdmin):
    list_display = ['id', 'adi']
    search_fields = ['adi']


admin.site.register(Domain, DomainAdmin)


class IlanAdmin(admin.ModelAdmin):
    list_display = ['id', 'telefon', 'baslangic_tarihi', 'bitis_tarihi', 'aktif']
    list_filter = ['aktif']
    search_fields = ['telefon']


admin.site.register(Ilan, IlanAdmin)


# Resim modelini admin paneline ekleyin
class ResimAdmin(admin.ModelAdmin):
    list_display = ['id', 'ilan', 'resim_url', 'aktif']
    list_filter = ['aktif', 'ilan']
    search_fields = ['ilan__telefon']


admin.site.register(Resim, ResimAdmin)


# Transaction modelini admin paneline ekleyin
class TransactionAdmin(admin.ModelAdmin):
    list_display = ['id', 'ilan', 'tarih', 'miktar']
    list_filter = ['ilan']
    search_fields = ['ilan']


admin.site.register(Transaction, TransactionAdmin)
