import datetime

from django.utils import timezone
from django.db import models

class QuestionTuple(models.Model):
    tuple_name = models.CharField(max_length=100)
    # questions = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.tuple_name

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    def get_id(self):
        return self.id

class Question(models.Model):
    tuple = models.ForeignKey(QuestionTuple, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=200)
    type = models.CharField(max_length=10)
    # 1 for radio; 2 for checkbox

    def __str__(self):
        return self.question_text

    def get_id(self):
        return self.id

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    status = models.CharField(max_length=10)
    # 1 for show; 2 for hide

    def __str__(self):
        return self.choice_text

class User(models.Model):
    account = models.CharField(max_length=30)
    name = models.CharField(max_length=30, default='')

    def __str__(self):
        return self.account + ": " + self.name

    def get_account(self):
        return self.account

    def get_name(self):
        return self.name



