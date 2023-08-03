from django.db import models
from django.urls import reverse

RATINGS = (
    ('1', 'Poor'),
    ('2', 'Alright'),
    ('3', 'Good'),
    ('4', 'Very Good'),
    ('5', 'Amazing'),
)

class Character(models.Model):
    name = models.CharField(max_length=50)
    image = models.CharField(max_length=50)
    description = models.TextField(blank=True, max_length=250)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('characters_detail', kwargs={'pk': self.id})
class Comic(models.Model):
    name = models.CharField(max_length=100)
    published = models.DateField()
    writer = models.CharField(max_length=100)
    penciler = models.CharField(max_length=100)
    cover = models.CharField(max_length=100)
    img_url = models.URLField()
    description = models.TextField(max_length=1000)
    characters = models.ManyToManyField(Character)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'comic_id': self.id })
    
class Vote(models.Model):
    date = models.DateField()
    rating = models.CharField(max_length=1, choices=RATINGS, default=RATINGS[0][0])
    comment = models.TextField(default='', max_length=200)
    comic = models.ForeignKey(Comic, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_rating_display()} on {self.date}"
    class Meta:
        ordering = ['-date']