# Generated by Django 3.0.4 on 2020-03-13 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('m2mexample', '0006_auto_20200313_1223'),
    ]

    operations = [
        migrations.AddField(
            model_name='heresearchcategory',
            name='strapline',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]
