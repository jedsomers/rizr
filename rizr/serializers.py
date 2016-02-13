from django.contrib.auth.models import User
from rizr.models import Video, Portfolio

from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email')
        
class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ('key', 'date_up', 'title', 'description')
        
class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        fields = ('user', 'video', 'key', 'buyDate', 'buyPx', 'currentDate', 'currentPx', 'amount', 'earnedPerc', 'earnedTot', 'timeHeldHrs')