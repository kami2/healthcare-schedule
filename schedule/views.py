from django.shortcuts import render
from .models import Shift
from datetime import datetime
# Create your views here.


def daily(request):
    number_of_the_day = datetime.today().isoweekday()
    shift = Shift.objects.filter(day_of_the_week = number_of_the_day)
    weekday = Shift.objects.filter(day_of_the_week = number_of_the_day).first()
    date = datetime.today().strftime('%d-%m-%Y')
    content = {
        'shift': shift,
        'date': date,
        'weekday': weekday
    }
    return render(request, "schedule/index.html", content)