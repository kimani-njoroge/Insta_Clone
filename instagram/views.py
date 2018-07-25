from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import render, redirect
from friendship.exceptions import AlreadyExistsError

from .forms import ProfileForm,ImageForm
from .models import Image,Profile
from friendship.models import Friend, Follow,Block

# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    # current_user = request.user
    images = Image.objects.all()
    profile = Profile.objects.all()
    # user = Profile.objects.get(user=current_user)
    # print(user)
    return render(request,'index.html',{"images":images,"profile":profile})

@login_required(login_url='/accounts/login/')
def addprofile(request):
    current_user = request.user
    # profile = Profile.objects.filter(user_id=current_user)
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
def showprofile(request, user_id):
    users = User.objects.get(id=user_id)
    profile = Profile.objects.get(user=users)
    followers = len(Follow.objects.followers(users))
    following = len(Follow.objects.following(users))
    images = Image.objects.filter(author=users)
    print("showing")
    return render(request, 'profile/profile.html',{"profile":users,"user":profile,"followers":followers,"following":following,"follow":follow,"images":images})


@login_required(login_url='/accounts/login/')
def follow(request,user_id):
    users = User.objects.get(id=user_id)
    try:
        follow = Follow.objects.add_follower(request.user, users)
    except AlreadyExistsError:
        return Http404
    # print("followed")
    return redirect('/showprofile/'+user_id)


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


@login_required(login_url='/accounts/login/')
def showdetails(request,profile_id):
    try:
        images = Image.objects.get(id=profile_id)
        print(images)
    except DoesNotExist:
        raise Http404()
    return render(request,'imagedetails.html',{"images":images})

# @login_required(login_url='/accounts/login/')
# def search_results(request):
#     if 'query' in request.GET and request.GET['query']:
#         query = request.GET.get("query")
#         user = Profile.profile_search(query)
#         return render(request,'search.html',{"user":user})
#     else:
#         return render(request,'search.html')