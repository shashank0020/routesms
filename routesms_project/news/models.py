from django.db import models
import datetime
from django.utils import timezone
# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):              # __unicode__ on Python 2
        return self.question_text

    def was_published_recently(self):
            return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
        
        
class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    
    def __str__(self):              # __unicode__ on Python 2
        return self.choice_text
    

class template_name(models.Model):
    template_name = models.CharField("Template Name",max_length=200,blank=False)

    def __unicode__(self) :
        return template_name
    
class comment(models.Model):
    comments = models.CharField("Comments",max_length=100,blank=False)
    template_name = models.ForeignKey(template_name)
    

    
