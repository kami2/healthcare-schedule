from django.shortcuts import render
from .models import Shift
from datetime import datetime

# Create your views here.


def daily(request):
    shift = Shift.objects.all()
    weekday = datetime.today().isoweekday()

    date = datetime.today().strftime('%d-%m-%Y')
    content = {
        'shift': shift,
        'weekday': weekday,
        'date': date,
    }
    return render(request, "schedule/index.html", content)