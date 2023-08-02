from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Comic
from .forms import VoteForm

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def comics_index(request):
    comics = Comic.objects.all()
    return render(request, 'comics/index.html', {'comics': comics})

def comics_detail(request, comic_id):
    comic = Comic.objects.get(id=comic_id)
    vote_form = VoteForm()
    return render(request, 'comics/detail.html', {'comic': comic, 'vote_form': vote_form})

def add_vote(request, comic_id):
    form = VoteForm(request.POST)
    if form.is_valid():
        new_vote = form.save(commit=False)
        new_vote.comic_id = comic_id
        new_vote.save()
    return redirect('detail', comic_id=comic_id)

class ComicCreate(CreateView):
    model = Comic
    fields = '__all__'

class ComicUpdate(UpdateView):
    model = Comic
    fields = '__all__'

class ComicDelete(DeleteView):
    model = Comic
    success_url = '/comics'
