# Generated by Django 4.2.1 on 2023-05-28 22:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ilan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domain', models.URLField()),
                ('telefon', models.CharField(max_length=15)),
                ('baslangic_tarihi', models.DateField()),
                ('bitis_tarihi', models.DateField()),
                ('aktif', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tarih', models.DateTimeField(auto_now_add=True)),
                ('miktar', models.DecimalField(decimal_places=2, max_digits=10)),
                ('ilan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='ilans.ilan')),
            ],
        ),
        migrations.CreateModel(
            name='Resim',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resim_url', models.URLField()),
                ('aktif', models.BooleanField(default=True)),
                ('ilan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resimler', to='ilans.ilan')),
            ],
        ),
    ]