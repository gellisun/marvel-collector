from django.forms import ModelForm
from .models import Vote

class VoteForm(ModelForm):
  class Meta:
    model = Vote
    fields = ['date', 'rating', 'comment']