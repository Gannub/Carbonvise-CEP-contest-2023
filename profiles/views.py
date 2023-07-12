from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView, FormView
from profiles.models import Profile
# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from profiles.forms import ProfileForm
from dealer.forms import DealerCreationForm

#Fatal: Add the Profile owner mixins here!!!! (later)
# class ProfileDetailView(DetailView):
    # model = Profile
    #make separate profile page 

# I am trying to use Function based views to make a separate profile page


def profile_page(request, slug):
    if request.user.is_authenticated:
        profile_slug = Profile.objects.get(slug=slug)

    else:
        return redirect('account_login')
    
    ctx = {'req_profile':profile_slug, }

    return render (request,'profiles/profile_detail.html',ctx)

# def dealersignup_page(request):
#     req_slug = request.user.profile.slug
#     req_profile = get_object_or_404(Profile,slug=req_slug)
    
#     if request.method == 'POST':

#         form = DealerCreationForm(request.POST, instance=req_profile)

#         if form.is_valid():
            
#             dealer_form = form.save(commit=False)
            
#             print(dealer_form.image,'test')

#             dealer_form.save() #add to the database
#             return redirect('index')

#     else: 
#         form = DealerCreationForm(instance=req_profile)
#     print("im here")
    
#     return render (request,'profiles/sign_up_dealer.html', {'form':form})

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile

    form_class = ProfileForm

class DealerForm(LoginRequiredMixin, CreateView):
    template_name = 'profiles/dealer_form.html'
    model = Profile

    form_class = DealerCreationForm
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


