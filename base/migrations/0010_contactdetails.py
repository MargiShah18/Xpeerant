# Generated by Django 4.0.4 on 2022-06-03 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_speciality_link_color'),
    ]

    operations = [
        migrations.CreateModel(
            name='contactdetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cd_con1', models.CharField(max_length=10)),
                ('cd_con2', models.CharField(max_length=10)),
                ('cd_ceoname', models.CharField(max_length=50)),
                ('cd_ceocon1', models.CharField(max_length=10)),
                ('cd_ceocon2', models.CharField(max_length=10)),
                ('cd_ext', models.CharField(max_length=5)),
                ('cd_email', models.EmailField(max_length=50)),
            ],
        ),
    ]
