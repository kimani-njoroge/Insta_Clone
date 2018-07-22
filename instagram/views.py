from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import ProfileForm,ImageForm
from .models import Image,Profile

# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    current_user = request.user
    images = Image.objects.all()
    profile = Profile.objects.all()
    user = Profile.objects.get(user=current_user)
    print(user)
    return render(request,'index.html',{"images":images,"profile":profile,"user":user})

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


@login_required(login_url='/accounts/login/')
def showprofile(request, profile_id):
    profile = Profile.objects.get(id=profile_id)
    return render(request, 'profile/profile.html',{"profile":profile})


@login_required(login_url='/accounts/login/')
def addimages(request):
    current_user = request.user
    profile = Profile.objects.all()
    for profile in profile:
        if profile.user.id == current_user.id:
            if request.method == 'POST':
                form = ImageForm(request.POST,request.FILES)
                if form.is_valid():
                    image_post = form.save(commit=False)
                    image_post.author = current_user
                    image_post.profile = profile
                    image_post.save()
                    return redirect('index')
            else:
                form = ImageForm
    return render(request, 'imagepost.html',{"image_form":form,"user":current_user})