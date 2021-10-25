from django.db import models

# Create your models here.
class Topic(models.Model):
    topic_name=models.CharField(max_length=100)

    def __str__(self):
        return self.topic_name


class webpage(models.Model):
    topic_name=models.ForeignKey(Topic,on_delete=models.CASCADE)
    name=models.CharField(max_length=800)
    url=models.URLField(max_length=100)

    def __str__(self):
        return self.name
