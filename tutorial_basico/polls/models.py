import datetime

from django.db import models
from django.utils import timezone
from django.contrib import admin

# Create your models here.

#Criando as tables da database
class Question(models.Model):
    question_text = models.CharField(max_length=200) #Diferentes tipos de Fields represantam os campos do BD
    pub_date = models.DateTimeField('date published') #Entre parênteses, pode ser especificado um nome mais fácil de ler (date published), se não tem, usa o nome da variável (pub_date)
    def __str__(self) -> str:
        return self.question_text
    @admin.display(
        boolean=True,
        ordering='pub_date',
        description='Published recently?',
    )
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) #Chave estrangeira, referenciando Question
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0) #Coloca um valor padrão
    def __str__(self) -> str:
        return self.choice_text