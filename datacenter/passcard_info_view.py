from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render, get_object_or_404

from datacenter.durations_utils import format_duration, calculate_duration


def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode=passcode)
    visits = Visit.objects.filter(passcard=passcard)
    this_passcard_visits = []

    for visit in visits:
        duration = calculate_duration(visit.entered_at, visit.leaved_at)

        is_strange = duration.total_seconds() > 3600

        this_passcard_visits.append({
            'entered_at': visit.entered_at,
            'duration': format_duration(duration),
            'is_strange': is_strange
        })

    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
