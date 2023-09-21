from re import search
from django.shortcuts import render, redirect
from django.http import HttpResponse
from . forms import writeblogform, TAG_CHOICES, blogcommentsform
from . models import blogs as blogsmodels, blogcomments as blogcommentsmodels
from accounts.models import UserProfileInfo

# Create your views here.

def blogs(request):
    contents = blogsmodels.objects.all()
    user = request.user
    taglist = []
    for i in TAG_CHOICES:
        taglist.append(i[0])
    search_input = request.GET.get('search-area') or ''
    tag_input = request.GET.get('filter_tags') or ''
    if tag_input and tag_input != 'All':
        contents = contents.filter(tag__icontains = tag_input)
    if search_input:
        contents = contents.filter(blogtopic__istartswith = search_input)
    return render(request, 'blogs.html', {'contents' : contents, 'user' : user, 'search_input' : search_input, 'taglist' : taglist, 'tag_input' : tag_input})

def writeblogs(request):
    if request.POST:
        form = writeblogform(request.POST)
        if form.is_valid():
            fs = form.save(commit=False)
            fs.author = request.user
            fs.save()
        return redirect(blogs)
    else:
        form = writeblogform()
    return render(request, 'writeblogs.html', {'form' : form}) 

def editblogs(request, pk):
    blog = blogsmodels.objects.get(id = pk)
    
    if request.POST:
        form = writeblogform(request.POST, instance = blog)
        if form.is_valid():
            form.save()
        return redirect('../../../accounts/profile')
    else:
        form = writeblogform(instance = blog)

    return render(request, 'writeblogs.html', {'form' : form})

def deleteblogs(request, pk):
    blog = blogsmodels.objects.get(id = pk)
    
    if request.POST:
        blog.delete()
        return redirect('../../../accounts/profile')

    return render(request, 'deleteblogs.html', {'blog' : blog})

def readblogs(request, pk):
    blog = blogsmodels.objects.get(id = pk)
    if request.POST:
        form = blogcommentsform(request.POST)
        if form.is_valid():
            fs = form.save(commit=False)
            fs.commentauthor = request.user
            fs.blog = blog
            fs.save()
        return redirect(blogs)
    else:
        form = blogcommentsform()
    return render(request, 'readblogs.html', {'content' : blog, 'form' : form})
