# Generated by Django 3.2.6 on 2021-08-20 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0003_auto_20210819_2026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='first_name',
            field=models.CharField(max_length=25, verbose_name='Imię'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='last_name',
            field=models.CharField(max_length=40, verbose_name='Nazwisko'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='phd',
            field=models.CharField(max_length=55, verbose_name='Tytuł naukowy'),
        ),
        migrations.AlterField(
            model_name='office',
            name='office',
            field=models.IntegerField(verbose_name='Gabinet'),
        ),
        migrations.AlterField(
            model_name='shift',
            name='day_of_the_week',
            field=models.CharField(choices=[('MONDAY', 'Poniedziałek'), ('TUESDAY', 'Wtorek'), ('WEDNESDAY', 'Środa'), ('THURSDAY', 'Czwartek'), ('FRIDAY', 'Piątek'), ('SATURDAY', 'Sobota'), ('SUNDAY', 'Niedziela')], max_length=15, verbose_name='Dzień tygodnia'),
        ),
    ]
