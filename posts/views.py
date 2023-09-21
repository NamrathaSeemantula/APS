from django.shortcuts import render
from .forms import postsForm
from . models import posts as postsModels
 
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from APS_Project2 import settings

def posts(request):
    contents = postsModels.objects.all()
    user = request.user

    return render(request, 'posts.html', {'contents' : contents, 'user' : user,})

def uploadpost(request):

    if request.method == 'POST':
        form = postsForm(data=request.POST)

        if form.is_valid():
            fs = form.save(commit=False)
            fs.author = request.user

            if 'postimage' in request.FILES:
                fs.postimage = request.FILES['postimage']

            fs.save()
            return HttpResponseRedirect(reverse('posts:posts'))
        else:
            print(form.errors)
    else:
        form = postsForm()
        
    return render(request, 'uploadpost.html', {'form':form})

def editpost(request, pk):
    post = postsModels.objects.get(id = pk)
    
    if request.POST:
        form = postsForm(request.POST, instance = post)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse('accounts:profile'))
    else:
        form = postsForm(instance = post)

    return render(request, 'uploadpost.html', {'form' : form})

def deletepost(request, pk):
    post = postsModels.objects.get(id = pk)
    
    if request.POST:
        post.delete()
        return HttpResponseRedirect(reverse('accounts:profile'))

    return render(request, 'deleteposts.html', {'post' : post})