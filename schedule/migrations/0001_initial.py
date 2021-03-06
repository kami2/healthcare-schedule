# Generated by Django 3.2.6 on 2021-08-19 19:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phd', models.CharField(max_length=55)),
                ('first_name', models.CharField(max_length=25)),
                ('last_name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Office',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('office', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Rota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_of_the_week', models.CharField(choices=[('MONDAY', 'Poniedziałek'), ('TUESDAY', 'Wtorek'), ('WEDNESDAY', 'Środa'), ('THURSDAY', 'Czwartek'), ('FRIDAY', 'Piątek'), ('SATURDAY', 'Sobota'), ('SUNDAY', 'Niedziela')], max_length=15)),
                ('start_time', models.TimeField()),
                ('finish_time', models.TimeField()),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedule.doctor')),
                ('office', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedule.office')),
            ],
        ),
        migrations.CreateModel(
            name='Absence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_holiday', models.DateTimeField()),
                ('finish_holiday', models.DateTimeField()),
                ('holiday', models.BooleanField(default='false')),
                ('absence', models.BooleanField(default='false')),
                ('archived', models.BooleanField(default='false')),
                ('doctor', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='schedule.doctor')),
            ],
        ),
    ]
