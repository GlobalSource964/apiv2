from datetime import timedelta
from django.db import models


class Paketler(models.Model):
    adi = models.CharField(max_length=255)
    pozisyon = models.CharField(max_length=255)

    def __str__(self):
        return self.adi


class Domain(models.Model):
    adi = models.CharField(max_length=255)
    meta_title = models.CharField(max_length=255)
    meta_description = models.TextField()

    def __str__(self):
        return self.adi


class Ilan(models.Model):
    domain = models.ManyToManyField(Domain)
    paket = models.ManyToManyField(Paketler)
    telefon = models.CharField(max_length=15)
    baslangic_tarihi = models.DateField()
    bitis_tarihi = models.DateField(blank=True, null=True)
    meta_title = models.CharField(max_length=255, blank=True)
    meta_description = models.TextField(blank=True)
    aktif = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.baslangic_tarihi and not self.bitis_tarihi:
            self.bitis_tarihi = self.baslangic_tarihi + timedelta(weeks=1)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.telefon


class Resim(models.Model):
    ilan = models.ForeignKey(Ilan, related_name='resimler', on_delete=models.CASCADE)
    resim_url = models.URLField()
    aktif = models.BooleanField(default=False)

    def __str__(self):
        return self.ilan.telefon


class Transaction(models.Model):
    ilan = models.ForeignKey(Ilan, related_name='transactions', on_delete=models.CASCADE)
    tarih = models.DateTimeField(auto_now_add=True)
    miktar = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.ilan.telefon + ' ' + self.miktar.__str__() + ' TL'
