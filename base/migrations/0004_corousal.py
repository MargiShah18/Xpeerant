# Generated by Django 4.0.4 on 2022-06-01 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_contact_delete_contactus'),
    ]

    operations = [
        migrations.CreateModel(
            name='corousal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('corousal_name', models.CharField(max_length=50)),
                ('desc', models.CharField(max_length=300)),
                ('image', models.ImageField(default='', upload_to='base/images')),
            ],
        ),
    ]
