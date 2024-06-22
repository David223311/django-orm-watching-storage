from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from .function import format_time, visits_time
from django.utils.timezone import localtime
from django.shortcuts import get_object_or_404


def passcard_info_view(request, passcode): 
    passcard = get_object_or_404(Passcard, passcode=passcode)
    visits = Visit.objects.filter(passcard=passcard)
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
        'passcard': passcard, 
        'this_passcard_visits': non_closed_visits
    }
    return render(request, 'passcard_info.html', context)
