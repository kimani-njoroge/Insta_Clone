from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .forms import ProfileForm
from .models import Image,Profile

# Create your views here.

def index(request):
    return render(request,'index.html')

@login_required(login_url='/accounts/login/')
def addprofile(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
    else:
        form = ProfileForm()
    return render(request, 'profile/newprofile.html', {"form":form})
