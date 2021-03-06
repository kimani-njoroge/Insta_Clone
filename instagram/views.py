from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from friendship.exceptions import AlreadyExistsError

from .forms import ProfileForm,ImageForm,CommentForm
from .models import Image,Profile, Comment
from friendship.models import Friend, Follow,Block

# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    images = Image.objects.all()
    profile = Profile.objects.all()
    form = CommentForm()
    comments = Comment.objects.all()
    return render(request,'index.html',{"images":images,"profile":profile,"form":form,"comments":comments})

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
                form = ImageForm()
    return render(request, 'imagepost.html',{"image_form":form,"user":current_user})


@login_required(login_url='/accounts/login/')
def showdetails(request,profile_id):
    try:
        images = Image.objects.get(id=profile_id)
        print(images)
    except DoesNotExist:
        raise Http404()
    return render(request,'imagedetails.html',{"images":images})

@login_required(login_url='/accounts/login/')
def search_results(request):
    if 'query' in request.GET and request.GET['query']:
        query = request.GET.get("query")
        search_term = Profile.profile_search(query)
        return render(request,'search.html',{"search_term":search_term})
    else:
        return render(request,'search.html')

@login_required(login_url='/accounts/login/')
def addcomment(request,image_id):
    current_user = request.user
    if request.method == 'POST':
        image = get_object_or_404(Image, pk=image_id)
        form = CommentForm(request.POST,request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = current_user
            comment.image = image
            comment.save()
            return redirect('index')
    else:
        form = CommentForm()

    return render(request, 'index.html',{"form":form})

