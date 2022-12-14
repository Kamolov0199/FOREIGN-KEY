# Generated by Django 4.1.4 on 2022-12-08 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TopPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Turi: ')),
                ('content', models.TextField(verbose_name="Ma'lumot: ")),
                ('use', models.CharField(max_length=20, verbose_name='Nomi: ')),
                ('categories', models.CharField(max_length=50)),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Sana: ')),
                ('img', models.CharField(max_length=255, verbose_name='Rasm: ')),
            ],
        ),
    ]