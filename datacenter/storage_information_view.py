from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from .function import format_time, visits_time
from django.utils.timezone import localtime


def storage_information_view(request):
    visits = Visit.objects.filter(leaved_at=None)
    non_closed_visits = []
    for visit in visits:
        visit_time = visits_time(visit)
        entry_time = localtime(visit.entered_at)
        inside = format_time(visit_time)
        name_visit = visit.passcard
        non_closed_visits.append({
            'who_entered': name_visit,
            'entered_at': entry_time,
            'duration': inside,
        })
    context = {
        'non_closed_visits': non_closed_visits, 
    }
    return render(request, 'storage_information.html', context)
