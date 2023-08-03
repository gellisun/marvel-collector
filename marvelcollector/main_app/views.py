from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Comic, Character
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
    id_list = comic.characters.all().values_list('id')
    characters_comic_doesnt_have = Character.objects.exclude(id__in=id_list)

    vote_form = VoteForm()
    return render(request, 'comics/detail.html', {'comic': comic, 'vote_form': vote_form, 'characters': characters_comic_doesnt_have})

def add_vote(request, comic_id):
    form = VoteForm(request.POST)
    if form.is_valid():
        new_vote = form.save(commit=False)
        new_vote.comic_id = comic_id
        new_vote.save()
    return redirect('detail', comic_id=comic_id)

class ComicCreate(CreateView):
    model = Comic
    fields = ['name', 'published', 'writer', 'penciler', 'cover', 'img_url', 'description']

class ComicUpdate(UpdateView):
    model = Comic
    fields = '__all__'

class ComicDelete(DeleteView):
    model = Comic
    success_url = '/comics'

class CharacterList(ListView):
  model = Character

class CharacterDetail(DetailView):
  model = Character

class CharacterCreate(CreateView):
  model = Character
  fields = '__all__'

class CharacterUpdate(UpdateView):
  model = Character
  fields = ['name', 'image', 'description']

class CharacterDelete(DeleteView):
  model = Character
  success_url = '/characters'

def assoc_character(request, comic_id, character_id):
   Comic.objects.get(id=comic_id).characters.add(character_id)
   return redirect('detail', comic_id=comic_id)

def unassoc_character(request, comic_id, character_id):
   Comic.objects.get(id=comic_id).characters.remove(character_id)
   return redirect('detail', comic_id=comic_id)