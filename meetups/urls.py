from operator import index
from django.urls import path
from . import views

urlpatterns = [
    path('meetups/', views.index, name='meetups.index'),
    path('meetups/<slug:meetup_slug>', views.show, name='meetups.show')
]
