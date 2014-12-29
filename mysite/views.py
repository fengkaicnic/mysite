from django.http import Http404, HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response
import datetime


def hello(request):
    return HttpResponse("Hello x")

def current_time(request):
    now = datetime.datetime.now()
    return HttpResponse('It is now %s' % now)

def display(request):
    values = request.META.items()
    values.sort()
    html = []
    for k, v in values:
        html.append('%s : %s<br>' % (k, v))
    return HttpResponse(''.join(html))

def current(request):
    now = datetime.datetime.now()
    return render_to_response('current_time.html', {'current_date': now, 'person_name': 'Dog', 'company': 'IBM'})

def current_datetime(request):
    now = datetime.datetime.now()
    t = get_template('current_time.html')
    html = t.render(Context({'current_date': now, 'person_name': 'Dog', 'company': 'IBM'}))
    return HttpResponse(html)

def hours_ahead(request, offset):
    try:
	offset = int(offset)
    except ValueError:
	raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)  
    return HttpResponse('In %s hour it will be %s' % (offset, dt))
