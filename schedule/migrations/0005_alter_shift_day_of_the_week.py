# Generated by Django 3.2.6 on 2021-08-21 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0004_auto_20210820_2027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shift',
            name='day_of_the_week',
            field=models.CharField(choices=[(1, 'Poniedziałek'), (2, 'Wtorek'), (3, 'Środa'), (4, 'Czwartek'), (5, 'Piątek'), (6, 'Sobota'), (7, 'Niedziela')], max_length=15, verbose_name='Dzień tygodnia'),
        ),
    ]