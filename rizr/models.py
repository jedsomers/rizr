from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    networth = models.DecimalField(max_digits=12, decimal_places=4)
    trades = models.IntegerField(default=0)
    admin = models.BooleanField(default=False)
    
    def __unicode__(self):
        return self.user.username
    
class Video(models.Model):
    key = models.CharField(max_length=20, unique=True)
    date_up = models.CharField(max_length=256)
    title = models.CharField(max_length=256)
    description = models.CharField(max_length=512)
    
    def __unicode__(self):
        return self.title
        
class History(models.Model):
    video = models.ForeignKey(Video)
    key = models.CharField(max_length=20, unique=True)
    datetime = models.CharField(max_length=265)
    ageHrs = models.DecimalField(max_digits=12, decimal_places=4)
    commentCount = models.IntegerField(default=0)
    likeCount = models.IntegerField(default=0)
    dislikeCount = models.IntegerField(default=0)
    favoriteCount = models.IntegerField(default=0)
    expviews = models.DecimalField(max_digits=12, decimal_places=4)
    
    def __unicode__(self):
        return self.datetime
        
        
class Txhistory(models.Model):
    user = models.ForeignKey(UserProfile)
    video = models.ForeignKey(Video)
    key = models.CharField(max_length=20)
    buyDate = models.CharField(max_length=265)
    buyPx = models.DecimalField(max_digits=12, decimal_places=4)
    sellDate = models.CharField(max_length=265)
    sellPx = models.DecimalField(max_digits=12, decimal_places=4)
    amount = models.IntegerField(default=0)
    earnedPerc = models.DecimalField(max_digits=10, decimal_places=4)
    earnedTot = models.DecimalField(max_digits=12, decimal_places=4)
    timeHeldHrs = models.DecimalField(max_digits=12, decimal_places=4)
    
    def __unicode__(self):
        return self.video.title
        
class Portfolio(models.Model):
    user = models.ForeignKey(UserProfile)
    video = models.ForeignKey(Video)
    key = models.CharField(max_length=20)
    buyDate = models.CharField(max_length=265)
    buyPx = models.DecimalField(max_digits=12, decimal_places=4)
    currentDate = models.CharField(max_length=265)
    currentPx = models.DecimalField(max_digits=12, decimal_places=4)
    amount = models.IntegerField(default=0)
    earnedPerc = models.DecimalField(max_digits=10, decimal_places=4)
    earnedTot = models.DecimalField(max_digits=12, decimal_places=4)
    timeHeldHrs = models.DecimalField(max_digits=12, decimal_places=4)
    
    def __unicode__(self):
        return self.video.title
        