from django.shortcuts import render
from .forms import ProfileForm
from .models import Image,Profile

# Create your views here.

def index(request):
    return render(request,'index.html')


def profile(request):

    return render(request,'profile.html')
