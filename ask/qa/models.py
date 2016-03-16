from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User, db_constraint=False)
    likes = models.ManyToManyField(User, related_name='likes_set')
    def __unicode__(self):
        return self.title

    def get_url(self):
        return reverse('question_details', self.id)

class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    question = models.ForeignKey(Question)
    author = models.ForeignKey(User, db_constraint=False)
    def __unicode__(self):
        return self.text

