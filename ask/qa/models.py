from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
import random, datetime

# Create your models here.

#class User(models.Model):
#    username = models.CharField(max_length=255,unique=True)
#    password = models.CharField(max_length=255)
#    email = models.EmailField()
#    def __unicode__(self):
#        return self.username


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
        return 'http://0.0.0.0/question/' + str(self.id) + '/'

class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    question = models.ForeignKey(Question)
    author = models.ForeignKey(User, db_constraint=False)
    def __unicode__(self):
        return self.text



class Session(models.Model):
    key = models.CharField(max_length=255, unique=True)
    user = models.ForeignKey(User)
    expires = models.DateTimeField()


def do_login(username, password):
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return None
    hashed_pass = password
    if user.password != hashed_pass:
        return None
    session = Session()
    session.key = generate_long_random_key()
    session.user = user
    session.expires = datetime.date.today() + datetime.timedelta(days=5)
    session.save()
    return session

def generate_long_random_key():
    return random.random()*100000000000000