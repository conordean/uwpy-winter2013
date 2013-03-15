from django.contrib.auth.models import User
from django.db import models
from uw.models import Program

class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True, blank=True)
    programs = models.ManyToManyField(Program)

    def __unicode__(self):
      return unicode(self.user)
