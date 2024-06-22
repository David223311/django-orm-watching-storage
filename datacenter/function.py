from django.db import models
from django.utils import timezone
from django.utils.timezone import localtime


def visits_time(visits):
    entry_time = timezone.localtime(visits.entered_at)
    date_now = timezone.localtime(timezone.now())
    delta_time = date_now - entry_time
    return delta_time


def format_time(time):
    second = time.seconds
    hour = second // 3600
    minute = (second % 3600) // 60
    second = second % 60
    return f'{hour} ч. {minute} мин. {second} сек.'
