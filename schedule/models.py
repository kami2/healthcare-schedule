from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from django.utils.safestring import mark_safe
from django.urls import reverse
from datetime import date
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
    office = models.IntegerField("Gabinet", unique=True)


    class Meta:
        verbose_name = _("Gabinet")
        verbose_name_plural = _("Gabinety")


    def validate_unique(self, exclude=None):
        try:
            super(Office, self).validate_unique()
        except ValidationError as e:
            raise ValidationError('Istnieje już gabinet o takim numerze')


    def __str__(self):
        return "Gabinet numer " + str(self.office)




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
        unique_together = [("doctor", "day_of_the_week")]
        verbose_name = _("Zmiana")
        verbose_name_plural = _("Zmiany")


    def get_admin_url(self):
        return reverse("admin:%s_%s_change" % (self._meta.app_label, self._meta.model_name), args=(self.pk,))


    def get_hyperlink(self):
        doctor_in_day_of_the_week = Shift.objects.filter(day_of_the_week=self.day_of_the_week).filter(doctor=self.doctor).get()
        return  "<a href='%s'>TUTAJ</a>" % doctor_in_day_of_the_week.get_admin_url()


    def validate_unique(self, exclude=None):
        try:
            super(Shift, self).validate_unique()
        except ValidationError as e:
            raise ValidationError(
                (_(mark_safe(str(self.doctor) + " jest już zapisany na ten dzień tygodnia. Aby przejść do wpisu kliknij " + self.get_hyperlink())))
            )


    def __str__(self):
        return "Wpis numer: " + str(self.id)




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

    def clean(self):
        if self.start_holiday.date() > self.finish_holiday.date():
            raise ValidationError('Nie można dodać urlopu z datą rozpoczęcia późniejszą niż data zakończenia urlopu')

    def get_admin_url(self):
        return reverse("admin:%s_%s_change" % (self._meta.app_label, self._meta.model_name), args=(self.pk,))


    def get_hyperlink(self):
        doctor_on_holiday = Absence.objects.       filter(doctor=self.doctor).get()
        return  "<a href='%s'>TUTAJ</a>" % doctor_on_holiday.get_admin_url()


    def validate_unique(self, exclude=None):
        try:
            super(Absence, self).validate_unique()
        except ValidationError as e:
            raise ValidationError(
                (_(mark_safe(
                    str(self.doctor) + " jest już zapisany na urlop. Aby przejść do wpisu, kliknij " + self.get_hyperlink())))
            )

    def __str__(self):
        return str(self.doctor)



