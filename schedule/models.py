from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Doctor(models.Model):
    phd = models.CharField("Tytuł naukowy", max_length=55)
    first_name = models.CharField("Imię", max_length=25)
    last_name = models.CharField("Nazwisko", max_length=40)

    def __str__(self):
        return str(self.phd) + " " + str(self.first_name) + " " + str(self.last_name)


class Office(models.Model):
    office = models.IntegerField("Gabinet")

    def __str__(self):
        return "Numer gabinetu: " + str(self.office)


class Shift(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)

    class DayOfTheWeek(models.IntegerChoices):
        MON = 1, _('Poniedziałek')
        TUE = 2, _('Wtorek')
        WED = 3, _('Środa')
        THU = 4, _('Czwartek')
        FRI = 5, _('Piątek')
        SAT = 6, _('Sobota')
        SUN = 7, _('Niedziela')

    day_of_the_week = models.IntegerField("Dzień tygodnia", choices=DayOfTheWeek.choices)

    def is_upperclass(self):
        return self.day_of_the_week

    office = models.ForeignKey(Office, on_delete=models.CASCADE)
    start_time = models.TimeField(auto_now=False, auto_now_add=False)
    finish_time = models.TimeField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return str(self.day_of_the_week)



class Absence(models.Model):
    doctor = models.OneToOneField(Doctor, on_delete=models.CASCADE)
    start_holiday = models.DateTimeField()
    finish_holiday = models.DateTimeField()
    holiday = models.BooleanField(default=False)
    absence = models.BooleanField(default=False)
    archived = models.BooleanField(default=False)

    def __str__(self):
        return str(self.doctor)



