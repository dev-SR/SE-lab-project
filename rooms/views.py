from django.shortcuts import render

# Create your views here.


def rooms(request):
    return render(request, "rooms/index.html", {'value': 'Hello World'})
