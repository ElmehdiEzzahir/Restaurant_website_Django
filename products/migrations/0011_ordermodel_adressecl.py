# Generated by Django 4.0.3 on 2022-04-18 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_ordermodel_email_ordermodel_namecl'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordermodel',
            name='adressecl',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
