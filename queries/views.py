from django.shortcuts import render, redirect
from django.http import HttpResponse
from . forms import queryform, answersform, TAG_CHOICES
from . models import queries as queriesmodels, answers as answersmodels

# Create your views here.

def queries(request):
    contents = queriesmodels.objects.all()
    user = request.user
    taglist = []
    for i in TAG_CHOICES:
        taglist.append(i[0])
    search_input = request.GET.get('search-area') or ''
    tag_input = request.GET.get('filter_tags') or ''
    if tag_input and tag_input != 'All':
        contents = contents.filter(tag__icontains = tag_input)
    if search_input:
        contents = contents.filter(query__icontains = search_input)
    return render(request, 'queries.html', {'contents' : contents, 'user' : user, 'search_input' : search_input, 'taglist' : taglist, 'tag_input' : tag_input})

def postquery(request):
    if request.POST:
        form = queryform(request.POST)
        if form.is_valid():
            fs = form.save(commit=False)
            fs.author = request.user
            fs.save()
        return redirect(queries)
    else:
        form = queryform()
    return render(request, 'postquery.html', {'form' : form}) 

def deletequery(request, pk):
    query = queriesmodels.objects.get(id = pk)
    
    if request.POST:
        query.delete()
        return redirect('../../../accounts/profile')

    return render(request, 'deletequery.html', {'query' : query})

def readanswers(request, pk):
    query = queriesmodels.objects.get(id = pk)
    if request.POST:
        form = answersform(request.POST)
        if form.is_valid():
            fs = form.save(commit=False)
            fs.answerauthor = request.user
            fs.query = query
            fs.save()
        return redirect(queries)
    else:
        form = answersform()
    return render(request, 'readanswers.html', {'content' : query, 'form' : form})
