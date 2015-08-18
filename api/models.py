from django.db import models
from django.contrib.auth.models import User


class Quest(models.Model):
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=256)
    master = models.ForeignKey(User)
    
    def __unicode__(self):
        return "Quest: %s" % self.name
    