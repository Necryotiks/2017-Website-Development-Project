"""
Definition of urls for KRUW_Website.
"""

from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views

from Record_Keeper import forms
import Record_Keeper.views

# Uncomment the next lines to enable the admin:
from django.conf.urls import include
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    # Examples:
    url(r'^$', Record_Keeper.views.home, name='home'),
    url(r'^contact$', Record_Keeper.views.contact, name='contact'),
    url(r'^about', Record_Keeper.views.about, name='about'),
    url(r'^login/$',
        django.contrib.auth.views.login,
        {
            'template_name': 'Record_Keeper/login.html',
            'authentication_form': Record_Keeper.forms.BootstrapAuthenticationForm,
            'extra_context':
            {
                'title': 'Log in',
                'year': datetime.now().year,
            }
        },
        name='login'),
    url(r'^logout$',
        django.contrib.auth.views.logout,
        {
            'next_page': '/',
        },
        name='logout'),

    # Uncomment the admin/doc line below to enable admin documentation:
     url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
]
