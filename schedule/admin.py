from django.contrib import admin
from .models import Doctor, Shift, Office, Absence
from django.utils.translation import ugettext_lazy as _

# Register your models here.

class AbsenceInline(admin.TabularInline):
    model = Absence


@admin.register(Absence)
class AbsenceAdmin(admin.ModelAdmin):
    list_display = ('doctor', 'holiday')


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phd')
    inlines =  [AbsenceInline]


@admin.register(Shift)
class RotaAdmin(admin.ModelAdmin):
    list_display = ('doctor', 'day_of_the_week', 'office', 'start_time', 'finish_time')



admin.site.register(Office)

