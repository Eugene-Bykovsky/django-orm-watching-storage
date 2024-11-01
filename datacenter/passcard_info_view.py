from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render, get_object_or_404
from django.utils import timezone


def format_duration(duration):
    duration_hours, remainder = divmod(duration.total_seconds(), 3600)
    duration_minutes = remainder // 60
    return f'{int(duration_hours)}:{int(duration_minutes)}'


def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode=passcode)
    visits = Visit.objects.filter(passcard=passcard)
    this_passcard_visits = []

    for visit in visits:
        if visit.leaved_at:
            duration = visit.leaved_at - visit.entered_at
        else:
            duration = timezone.localtime(timezone.now()) - visit.entered_at

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
