from django.shortcuts import render
from .forms import eventsForm
from . models import events as eventsModels
 
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from APS_Project2 import settings

def events(request):
    contents = eventsModels.objects.all()
    user = request.user

    return render(request, 'events.html', {'contents' : contents, 'user' : user,})

def uploadevent(request):

    if request.method == 'POST':
        form = eventsForm(data=request.POST)

        if form.is_valid():
            fs = form.save(commit=False)
            fs.author = request.user

            if 'eventImg' in request.FILES:
                fs.eventImg = request.FILES['eventImg']

            fs.save()
            return HttpResponseRedirect(reverse('events:events'))
        else:
            print(form.errors)
    else:
        form = eventsForm()
        
    return render(request, 'uploadevent.html', {'form':form})

# def editpost(request, pk):
#     post = postsModels.objects.get(id = pk)
    
#     if request.POST:
#         form = postsForm(request.POST, instance = post)
#         if form.is_valid():
#             form.save()
#         return HttpResponseRedirect(reverse('accounts:profile'))
#     else:
#         form = postsForm(instance = post)

#     return render(request, 'uploadpost.html', {'form' : form})

# def deletepost(request, pk):
#     post = postsModels.objects.get(id = pk)
    
#     if request.POST:
#         post.delete()
#         return HttpResponseRedirect(reverse('accounts:profile'))

#     return render(request, 'deleteposts.html', {'post' : post})