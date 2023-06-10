from django.core.management.base import BaseCommand
from ilans.models import Ilan, Resim


class Command(BaseCommand):
    help = 'Removes duplicate Ilan and Resim objects'

    def handle(self, *args, **options):
        # For Ilan model
        for telefon in Ilan.objects.values_list('telefon', flat=True).distinct():
            ilan_objects = Ilan.objects.filter(telefon=telefon)
            if ilan_objects.count() > 1:
                ilan_objects.exclude(id=ilan_objects.first().id).delete()
                self.stdout.write(self.style.SUCCESS(f'Duplicates removed for Ilan with telefon: {telefon}'))

        # For Resim model
        for resim_url in Resim.objects.values_list('resim_url', flat=True).distinct():
            resim_objects = Resim.objects.filter(resim_url=resim_url)
            if resim_objects.count() > 1:
                resim_objects.exclude(id=resim_objects.first().id).delete()
                self.stdout.write(self.style.SUCCESS(f'Duplicates removed for Resim with resim_url: {resim_url}'))
