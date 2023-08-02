from django.contrib import admin
# import your models here
from .models import Comic, Vote

# Register your models here
admin.site.register(Comic)
admin.site.register(Vote)
