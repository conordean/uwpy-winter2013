from django.db import models
from django.contrib.auth.models import User


#class UserProfile(models.Model):
#    user = models.OneToOneField(User, primary_key=True, blank=True, related_name='profile')
#    about_me = models.TextField(blank=True, null=True)
#    date_created = models.DateTimeField(auto_now_add=True)
#    gender = models.CharField(max_length=1, choices=(
#        ('m', 'Male'), ('f', 'Female')), blank=True, null=True)
#    date_of_birth = models.DateField(blank=True, null=True)
#
#    def __unicode__(self):
#      return unicode(self.user)


class Activity(models.Model):
    """An event which is apart of a program that a user can register for."""

    class Meta:
        verbose_name = ('Activity')
        verbose_name_plural = ('Activities')

    author = models.ForeignKey(User, null=True, blank=True)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
      return unicode(self.content)


class ActivitySchedule(models.Model):
    """Time slot for the Activity."""

    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    notes = models.TextField()

    def __unicode__(self):
      return unicode(self.start_time)


class Program(models.Model):
    """A Program is a collection of activities."""

    name = models.CharField(max_length=32)
    activity = models.ManyToManyField(Activity)
    description = models.TextField()
    visible = models.IntegerField(default=1)

    def __unicode__(self):
      return unicode(self.name)

