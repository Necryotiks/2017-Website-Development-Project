"""
Definition of views.
"""

from django.shortcuts import render
from django.http.response import HttpResponse
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from .models import Record

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'Record_Keeper/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'Record_Keeper/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'Record_Keeper/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )
def index(request):
    all_records = Record.objects.all()
    html=''
    return HttpResponse(html)