# Generated by Django 4.0.4 on 2022-06-03 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_ac'),
    ]

    operations = [
        migrations.CreateModel(
            name='speciality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sp_image', models.ImageField(default='', upload_to='base/images')),
                ('sp_title', models.CharField(max_length=50)),
                ('sp_desc_p1', models.CharField(max_length=200)),
                ('sp_link', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='ac',
            name='ac_desc_p1',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='ac',
            name='ac_desc_p2',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='ac',
            name='ac_link',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='crousal',
            name='desc',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='crousal',
            name='link',
            field=models.CharField(max_length=200),
        ),
    ]
