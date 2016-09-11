from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class QuestionManager(models.Manager):
    def new(self):
        return self.order_by('added_at').get()
    def popular(self):
        return self.order_by('rating')

class Question(models.Model):
    object = QuestionManager()
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User,on_delete=models.CASCADE, related_name="question")
    likes = models.ManyToManyField(User, related_name="question_like")

class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField()
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    author = models.ForeignKey(User,on_delete=models.CASCADE)