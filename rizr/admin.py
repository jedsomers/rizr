from django.contrib import admin
from rizr.models import UserProfile, Video, History, Txhistory, Portfolio

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Video)
admin.site.register(History)
admin.site.register(Txhistory)
admin.site.register(Portfolio)
