# Generated by Django 4.0.4 on 2022-06-01 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactus',
            old_name='email',
            new_name='emailH',
        ),
        migrations.RenameField(
            model_name='contactus',
            old_name='name',
            new_name='nameH',
        ),
        migrations.RenameField(
            model_name='contactus',
            old_name='phone',
            new_name='phoneH',
        ),
        migrations.AddField(
            model_name='contactus',
            name='inquH',
            field=models.CharField(default='', max_length=110),
        ),
    ]
