# from django.db import models
# from django.contrib.auth.models import User
# from django.urls import reverse
#
#
# class Question(models.Model):
#     title = models.CharField(max_length=255)
#     text = models.TextField()
#     added_at = models.DateTimeField(auto_now_add=True)
#     rating = models.IntegerField(default=0)
#     author = models.ForeignKey(User)
#     likes = models.ManyToManyField(User, related_name='likes_users')
#
#     def get_url(self):
#         return reverse('question', kwargs={'id': self.pk})
#
#     def __unicode__(self):
#         return self.title
#
#     def __str__(self):
#         return self.title
#
# class Answer(models.Model):
#     text = models.TextField()
#     added_at = models.DateTimeField(auto_now_add=True)
#     question = models.ForeignKey(Question)
#     author = models.ForeignKey(User)
