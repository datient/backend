from datetime import datetime, timedelta

from django.db.models import Count
from rest_framework.response import Response
from rest_framework.decorators import api_view

from datient.models import Progress

COLORS = [
    '#E53935',
    '#D81B60',
    '#8E24AA',
    '#3949AB',
    '#1E88E5',
    '#00ACC1',
    '#00897B',
    '#43A047',
    '#7CB342',
    '#C0CA33',
    '#FDD835',
    '#FFB300',
    '#FB8C00',
    '#F4511E',
    '#6D4C41',
    '#757575',
    '#546E7A',
]

@api_view()
def generate_statistics(request):
    start_date = datetime.now() - timedelta(days=30)
    progress = Progress.objects.filter(created_at__range=(start_date, datetime.now()))
    stats = progress.values('diagnosis', 'has_left').annotate(total=Count('diagnosis'))
    stats = stats.exclude(has_left=False)
    count_all = stats.count()
    for index, i in enumerate(stats):
        percentage = i['total'] / count_all * 100
        i['percentage'] = round(percentage)
        i['color'] = COLORS[index]
    return Response({'data': stats, 'total': count_all})
