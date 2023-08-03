from django.contrib import admin
# import your models here
from .models import Comic, Vote, Character

# Register your models here
admin.site.register(Comic)
admin.site.register(Vote)
admin.site.register(Character)
