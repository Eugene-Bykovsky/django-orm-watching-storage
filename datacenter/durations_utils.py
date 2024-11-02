from django.utils import timezone


def format_duration(duration):
    duration_hours, remainder = divmod(duration.total_seconds(), 3600)
    duration_minutes = remainder // 60
    return f'{int(duration_hours)}:{int(duration_minutes)}'


def get_duration(visit_time):
    return timezone.localtime(timezone.now()) - visit_time


def calculate_duration(entered_at, leaved_at=None):
    if leaved_at:
        return leaved_at - entered_at
    return timezone.localtime(timezone.now()) - entered_at
