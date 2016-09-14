from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

# Create your models here.
class QuestionManager(models.Manager):
    def new_question(self):
        return self.order_by('-added_at')
    def popular_question(self):
        return self.order_by('-rating')

class Question(models.Model):
    objects = QuestionManager()
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User,on_delete=models.CASCADE, related_name="question")
    likes = models.ManyToManyField(User, related_name="question_like")
    def __unicode__(self):
        return self.title
    def get_url(self):
        return reverse('question', kwargs={'id': self.pk})

class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    author = models.ForeignKey(User,on_delete=models.CASCADE)