from django.shortcuts import render
from django.views.generic import ListView, DetailView, View, UpdateView, FormView
from .models import Room
# Create your views here.


class HomeView(ListView):

    """ HomeView Definition """

    model = Room
    paginate_by = 12
    paginate_orphans = 5
    ordering = "created_at"
    context_object_name = "rooms"
