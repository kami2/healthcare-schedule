from django.contrib import admin
from .models import Doctor, Shift, Office, Absence
from django import forms
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
# Register your models here.

class AbsenceInline(admin.TabularInline):
    model = Absence



@admin.register(Shift)
class ShiftAdmin(admin.ModelAdmin):
    list_display = ('doctor', 'day_of_the_week', 'office', 'start_time', 'finish_time')
    list_filter = ('day_of_the_week', 'office')

class ShiftAdminForm(forms.ModelForm):
    model = Shift



@admin.register(Absence)
class AbsenceAdmin(admin.ModelAdmin):
    list_display = ('doctor', 'start_holiday', 'finish_holiday', 'holiday', 'absence', 'archived')


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phd')
    inlines =  [AbsenceInline]






admin.site.register(Office)

