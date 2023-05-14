from django.shortcuts import render

# Create your views here.

def index(request):

    meetups = [
        { 
            'title': 'First Meetup', 
            'location': 'New York', 
            'slug': 'first-meetup'
        },
        {
            'title': 'Second Meetup', 
            'location': 'Paris', 
            'slug': 'second-meetup'
        },
    ]

    return render(request, 'meetups/index.html', {
        'meetups': meetups
    })

def show(request, meetup_slug):
    meetup = {
        'title': 'Some Title',
        'desc': 'Some desc'
    }
    return render(request, 'meetups/show.html', {
        'meetup': meetup
    })
