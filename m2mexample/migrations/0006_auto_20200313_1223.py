# Generated by Django 3.0.4 on 2020-03-13 12:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('m2mexample', '0005_auto_20200313_1201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='heresearcharea',
            name='hecategory',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='m2mexample.HEResearchCategory'),
            preserve_default=False,
        ),
    ]