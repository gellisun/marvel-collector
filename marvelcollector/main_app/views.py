import uuid
import boto3
import os
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Comic, Character, ComicPhoto, CharacterPhoto
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
    fields = ['name', 'published', 'writer', 'penciler', 'cover', 'description']

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
  fields = ['name', 'description']

class CharacterDelete(DeleteView):
  model = Character
  success_url = '/characters'

def assoc_character(request, comic_id, character_id):
   Comic.objects.get(id=comic_id).characters.add(character_id)
   return redirect('detail', comic_id=comic_id)

def unassoc_character(request, comic_id, character_id):
   Comic.objects.get(id=comic_id).characters.remove(character_id)
   return redirect('detail', comic_id=comic_id)

def add_comic_photo(request, comic_id):
    # photo-file will be the "name" attribute on the <input type="file">
    comic_photo_file = request.FILES.get('comic_photo-file', None)
    if comic_photo_file:
        s3 = boto3.client('s3')
        # need a unique "key" for S3 / needs image file extension too
        key = uuid.uuid4().hex[:6] + comic_photo_file.name[comic_photo_file.name.rfind('.'):]
        # just in case something goes wrong
        try:
            bucket = os.environ['S3_BUCKET']
            s3.upload_fileobj(comic_photo_file, bucket, key)
            # build the full url string
            url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
            # we can assign to cat_id or cat (if you have a cat object)
            ComicPhoto.objects.create(url=url, comic_id=comic_id)
        except Exception as e:
            print('An error occurred uploading file to S3')
            print(e)
    return redirect('detail', comic_id=comic_id)

def add_character_photo(request, character_id):
    # photo-file will be the "name" attribute on the <input type="file">
    character_photo_file = request.FILES.get('character_photo_file', None)
    if character_photo_file:
        s3 = boto3.client('s3')
        # need a unique "key" for S3 / needs image file extension too
        key = uuid.uuid4().hex[:6] + character_photo_file.name[character_photo_file.name.rfind('.'):]
        # just in case something goes wrong
        try:
            bucket = os.environ['S3_BUCKET']
            s3.upload_fileobj(character_photo_file, bucket, key)
            # build the full url string
            url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
            # we can assign to cat_id or cat (if you have a cat object)
            CharacterPhoto.objects.create(url=url, character_id=character_id)
        except Exception as e:
            print('An error occurred uploading file to S3')
            print(e)
    return redirect('characters_detail', pk=character_id)