from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from profiles.models import Profile
# Create your views here.


#Fatal: Add the Profile owner mixins here!!!! (later)
class ProfileDetailView(DetailView):
    model = Profile
    
