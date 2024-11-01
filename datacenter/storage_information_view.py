from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils import timezone


def get_duration(visit_time):
    return timezone.localtime(timezone.now()) - visit_time


def format_duration(duration):
    duration_hours, remainder = divmod(duration.total_seconds(), 3600)
    duration_minutes = remainder // 60
    return f'{int(duration_hours)}:{int(duration_minutes)}'


def storage_information_view(request):
    visiter_now = Visit.objects.filter(leaved_at__isnull=True)[0]
    who_entered = visiter_now.passcard.owner_name
    entered_at = visiter_now.entered_at
    duration_timedelta = get_duration(entered_at)
    duration_str = format_duration(duration_timedelta)

    non_closed_visits = [
        {
            'who_entered': who_entered,
            'entered_at': entered_at,
            'duration': duration_str,
        }
    ]
    context = {
        'non_closed_visits': non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)
