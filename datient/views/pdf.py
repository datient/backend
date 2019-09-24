from django.conf import settings
from django.http import FileResponse, HttpResponse
from django.template.loader import render_to_string
from django.shortcuts import render
from weasyprint import CSS, HTML

from datient.models import ComplementaryStudy, Patient, Progress

def filter_evolutions(evolutions):
    res = []
    for i in evolutions:
        if i.income == True:
            res.append(i)
            break
        else:
            res.append(i)
    return res

def generate_pdf(request, dni):
    patient = Patient.objects.get(dni=dni)
    studies = ComplementaryStudy.objects.filter(patient__dni=dni)
    evolutions = Progress.objects.filter(patient__dni=dni).order_by('-created_at')
    evolution = filter_evolutions(evolutions)
    ctx = {
        'full_url': request.build_absolute_uri(settings.MEDIA_URL),
        'patient': patient,
        'evolution': evolution,
        'studies': studies,
    }
    rendered_html = render_to_string('pdf.html', ctx)
    response = HttpResponse(content_type='application/pdf')
    stylesheets = [CSS(settings.STATIC_ROOT + 'pdf/style.css')]
    pdf = HTML(string=rendered_html).write_pdf(response, stylesheets, presentational_hints=True)
    return response
