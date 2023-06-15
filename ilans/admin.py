from django.contrib import admin
from .models import Ilan, Resim, Transaction, Domain, Paketler, Blog
from dynamic_raw_id.admin import DynamicRawIDMixin

# Ilan modelini admin paneline ekleyin




class BlogAdmin(DynamicRawIDMixin, admin.ModelAdmin):
    pass

class DomainAdmin(admin.ModelAdmin):
    list_display = ['id', 'adi']
    search_fields = ['adi']


class IlanAdmin(admin.ModelAdmin):
    list_display = ['id', 'telefon', 'baslangic_tarihi', 'bitis_tarihi', 'display_domain', 'aktif']
    list_filter = ['aktif','domain']
    search_fields = ['telefon', 'domain__adi']

    def display_domain(self, obj):
        return ", ".join([d.adi for d in obj.domain.all()])

    display_domain.short_description = 'domain'

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "ilan":
            kwargs["queryset"] = Ilan.objects.filter(domain__in=request.domain)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(Blog, BlogAdmin)


class PaketAdmin(admin.ModelAdmin):
    list_display = ['id', 'adi', 'pozisyon']


admin.site.register(Paketler, PaketAdmin)




admin.site.register(Domain, DomainAdmin)

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
