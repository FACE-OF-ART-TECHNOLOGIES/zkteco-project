# Generated by Django 4.0 on 2022-07-02 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appuser', '0002_checkinout_userinfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='hremployee',
            name='rf_id',
            field=models.CharField(default=1, max_length=100, verbose_name='RFID number'),
            preserve_default=False,
        ),
    ]
