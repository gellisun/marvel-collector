from django.contrib import admin
# import your models here
from .models import Comic, Vote, Character, ComicPhoto, CharacterPhoto

# Register your models here
admin.site.register(Comic)
admin.site.register(Vote)
admin.site.register(Character)
admin.site.register(ComicPhoto)
admin.site.register(CharacterPhoto)