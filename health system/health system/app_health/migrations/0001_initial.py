# Generated by Django 4.1.7 on 2023-04-24 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=50)),
                ('username', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=50)),
                ('profilepic', models.FileField(default='anonymous.jpg', upload_to='media/')),
            ],
        ),
    ]
