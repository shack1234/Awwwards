from django.db import models
import datetime as dt
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from pyuploadcare.dj.models import ImageField
from django.db.models.signals import post_save
from django.dispatch import receiver

from django.db import models
from django.contrib.auth.models import User
import datetime as dt
from tinymce.models import HTMLField
from django.db.models.signals import post_save
from django.dispatch import receiver
import numpy as np

# Create your models here.
class Profile(models.Model):
  '''
  class that contains user Profile properties
  '''
  profile_pic = models.ImageField(upload_to='images/',null=True, blank=True)
  bio = models.TextField()
  contact = models.IntegerField(blank=True, null=True,)
  user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

  def __str__(self):
    return self.bio


  @receiver(post_save, sender=User)
  def create_user_profile(sender, instance, created, **kwargs):
          if created:
                  Profile.objects.create(user=instance)

  @receiver(post_save, sender=User)
  def save_user_profile(sender, instance, **kwargs):
          instance.profile.save()

  post_save.connect(save_user_profile, sender=User)

  def save_profile(self):
    self.save()

  def update_profile(self):
    self.update()

  def delete_profile(self):
    self.delete()

  @classmethod
  def get_profile(cls):
      profile = Profile.objects.all()
      return profile

  @classmethod
  def get_profile_by_id(cls, id):
      user_profile = Profile.objects.get(user=id)
      return user_profile

  @classmethod
  def get_profile_by_username(cls, user):
      profile_info = cls.objects.filter(user__contains=user)
      return profile_info

  @classmethod
  def filter_by_id(cls, id):
      profile = Profile.objects.filter(user = id).first()
      return profile



class Project(models.Model):
  '''
  class that contains Project properties
  '''
  title = models.CharField(max_length=40,null=True, blank=True)
  image = models.ImageField(upload_to='images/', null=True,blank=True)
  posted_on = models.DateTimeField(auto_now_add=True)
  description = models.TextField()
  link = models.URLField(max_length=70)
  user = models.ForeignKey(User,on_delete=models.CASCADE,default="",blank=True,null=True)
  profile = models.ForeignKey(Profile,on_delete=models.CASCADE,default="",blank=True,null=True)
  rating = models.TextField()

  def save_project(self):
    self.save()

  def update_project(self):
    self.update()

  def delete_project(self):
    self.delete()
    
  class Meta:
    ordering = ['posted_on']

  @classmethod
  def search_project(cls,title):
    project =  cls.objects.filter(title__icontains=title)
    return project

  @classmethod
  def get_posted_projects(cls):
    projects = Project.objects.all()
    return projects

  @classmethod
  def get_projects_on_profile(cls,profile):
      projects = Project.objects.filter(profile__pk = profile)
      return projects

  @classmethod
  def get_project_by_id(cls, id):
          project = Project.objects.filter(user_id=id).all()
          return project

  def average_design(self):
    total_ratings = list(map(lambda x: x.rating, self.designrating_set.all()))
    return np.mean(total_ratings)

  def average_usability(self):
        total_ratings = list(map(lambda x: x.rating, self.usabilityrating_set.all()))
        return np.mean(total_ratings)

  def average_content(self):
        total_ratings = list(map(lambda x: x.rating, self.contentrating_set.all()))
        return np.mean(total_ratings)


  def __str__(self):
    return self.title

class DesignRating(models.Model):
    CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
        (9, '9'),
        (10, '10')
    )
    project = models.ForeignKey(Project)
    pub_date = models.DateTimeField(auto_now_add=True)
    profile = models.ForeignKey(Profile)
    comment = models.CharField(max_length=200)
    rating = models.IntegerField(choices=CHOICES, default=0)


class UsabilityRating(models.Model):
    CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
        (9, '9'),
        (10, '10')
    )
    project = models.ForeignKey(Project)
    pub_date = models.DateTimeField(auto_now_add=True)
    profile = models.ForeignKey(Profile)
    comment = models.CharField(max_length=200)
    rating = models.IntegerField(choices=CHOICES, default=0)


class ContentRating(models.Model):
    CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
        (9, '9'),
        (10, '10')
    )
    project = models.ForeignKey(Project)
    pub_date = models.DateTimeField(auto_now_add=True,)
    profile = models.ForeignKey(Profile)
    comment = models.CharField(max_length=200)
    rating = models.IntegerField(choices=CHOICES, default=0)
