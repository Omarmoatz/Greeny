# Generated by Django 4.2.7 on 2023-11-24 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('logo', models.ImageField(upload_to='CompanyLogo/', verbose_name='Logo')),
                ('call_us', models.CharField(max_length=50, verbose_name='Call_us')),
                ('email_us', models.EmailField(max_length=254, verbose_name='Email')),
                ('subtitle', models.TextField(max_length=500, verbose_name='Subtitle')),
                ('face_link', models.URLField(blank=True, null=True, verbose_name='Facebook_link')),
                ('insta_link', models.URLField(blank=True, null=True, verbose_name='Instegrame_link')),
                ('linkedIn_link', models.URLField(blank=True, null=True, verbose_name='LinkedIn_link')),
                ('twet_link', models.URLField(blank=True, null=True, verbose_name='Twettir_link')),
                ('emails', models.TextField(max_length=200, verbose_name='Emails')),
                ('phones', models.TextField(max_length=200, verbose_name='Phones')),
                ('address', models.TextField(max_length=200, verbose_name='Location')),
            ],
        ),
    ]
