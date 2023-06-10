# Uygulamanın adı 'ilanlar' varsayılmıştır. Uygulamanızın adına göre bu dosyayı oluşturun veya değiştirin.
# ilanlar/management/commands/pasif_ilanlar.py
from django.core.management.base import BaseCommand
from django.utils import timezone
from ilans.models import Ilan

class Command(BaseCommand):
    help = 'Süresi geçmiş olan ilanları pasif hale getirir'

    def handle(self, *args, **kwargs):
        # Şimdiki zamanı al
        now = timezone.now()
        # Süresi geçmiş olan ve hala aktif olan ilanları bul
        expired_ilanlar = Ilan.objects.filter(bitis_tarihi__lt=now, aktif=True)
        # Bu ilanları pasif hale getir
        expired_ilanlar.update(aktif=False)
        self.stdout.write(self.style.SUCCESS(f'{expired_ilanlar.count()} ilan pasif hale getirildi.'))



# python manage.py pasif_ilanlar