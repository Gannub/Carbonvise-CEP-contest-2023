from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from profiles.models import Profile
# Create your views here.
from django.shortcuts import redirect


#Fatal: Add the Profile owner mixins here!!!! (later)
# class ProfileDetailView(DetailView):
    # model = Profile
    #make separate profile page 

# I am trying to use Function based views to make a separate profile page


def profile_page(request, slug):


    if request.user.is_authenticated:
        profile = Profile.objects.get(slug=slug)

    else:
        return redirect('account_login')
    
    ctx = {'req_profile':profile, }

    return render (request,'profiles/profile_detail.html',ctx)
