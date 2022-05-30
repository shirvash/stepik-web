from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class QuestionManager(models.Manager):
    def new(self):
        return self.order_by('-added_at')

    def popular(self):
        return self.order_by('-rating')


class Question(models.Model):
    objects = QuestionManager()
    title = models.CharField(max_length=512)
    text = models.TextField()
    added_ad = models.DateTimeField(auto_now=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User, on_delete=models.deletion.CASCADE)
    likes = models.ManyToManyField(User, related_name='for_likes', blank=True)

    def get_absolute_url(self):
        return reverse('question', args=[str(self.id)])

    def __unicode__(self):
        return u'%s: %s' % (self.author, self.title)

    def __str__(self):
        return u'%s: %s' % (self.author, self.title)


class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    question = models.ForeignKey(Question, on_delete=models.deletion.CASCADE)
    author = models.ForeignKey(User, on_delete=models.deletion.CASCADE)
