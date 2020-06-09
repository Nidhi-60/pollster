from django.db import models
from datetime import datetime
from django.utils.text import slugify


# Create your models here.
# question model
class Questions(models.Model):
    question = models.TextField()
    slug = models.SlugField(null=True, blank=True)
    pub_date = models.DateTimeField(default=datetime.now())

    def save(self, *args, **kwargs):
        self.slug = slugify(self.question)
        super(Questions, self).save(*args, **kwargs)

    def __str__(self):
        return self.question


# choice model
class QuestionChoice(models.Model):
    question_id = models.ForeignKey(Questions, on_delete=models.CASCADE)
    choice = models.CharField(max_length=50)
    votes = models.IntegerField(default=0)



