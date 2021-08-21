from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Doctor(models.Model):
    phd = models.CharField("Tytuł naukowy", max_length=55)
    first_name = models.CharField("Imię", max_length=25)
    last_name = models.CharField("Nazwisko", max_length=40)

    class Meta:
        verbose_name = _("Lekarz")
        verbose_name_plural = _("Lekarze")

    def __str__(self):
        return str(self.phd) + " " + str(self.first_name) + " " + str(self.last_name)


class Office(models.Model):
    office = models.IntegerField("Gabinet")

    class Meta:
        verbose_name = _("Gabinet")
        verbose_name_plural = _("Gabinety")

    def __str__(self):
        return "Numer gabinetu: " + str(self.office)


class Shift(models.Model):
    doctor = models.ForeignKey(Doctor, verbose_name="Lekarz", on_delete=models.CASCADE)

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

    office = models.ForeignKey(Office, verbose_name="Gabinet" , on_delete=models.CASCADE)
    start_time = models.TimeField(verbose_name="Czas rozpoczęcia", auto_now=False, auto_now_add=False)
    finish_time = models.TimeField(verbose_name="Czas zakończenia", auto_now=False, auto_now_add=False)

    class Meta:
        verbose_name = _("Zmiana")
        verbose_name_plural = _("Zmiany")

    def __str__(self):
        return str(self.day_of_the_week)



class Absence(models.Model):
    doctor = models.OneToOneField(Doctor, verbose_name="Lekarz", on_delete=models.CASCADE)
    start_holiday = models.DateTimeField(verbose_name= "Czas rozpoczęcia")
    finish_holiday = models.DateTimeField(verbose_name= "Czas zakończenia")
    holiday = models.BooleanField(verbose_name= "Urlop", default=False)
    absence = models.BooleanField(verbose_name= "Nieobecny", default=False)
    archived = models.BooleanField(verbose_name= "Zarchiwizowany", default=False)

    class Meta:
        verbose_name = _("Urlop / Nieobecność")
        verbose_name_plural = _("Urlopy / Nieobecności")

    def __str__(self):
        return str(self.doctor)



