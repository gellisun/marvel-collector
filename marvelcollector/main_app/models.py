from django.db import models
from django.urls import reverse
class Comic(models.Model):
    name = models.CharField(max_length=100)
    published = models.DateField()
    writer = models.CharField(max_length=100)
    penciler = models.CharField(max_length=100)
    cover = models.CharField(max_length=100)
    img_url = models.URLField()
    description = models.TextField(max_length=1000)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'comic_id': self.id })