# Generated by Django 4.2.1 on 2023-06-14 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_remove_mainadmin_contactno_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='base',
            name='date_of_birth',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='base',
            name='date_of_joining',
            field=models.TextField(),
        ),
    ]