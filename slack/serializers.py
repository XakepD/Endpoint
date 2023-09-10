from rest_framework import serializers
from .models import *

class InfoSerializer(serializers.Serializer):
      slack_name = serializers.CharField()
      current_day = serializers.CharField()
      utc_time = serializers.CharField()
      track = serializers.CharField()
      github_file_url=  serializers.CharField()
      github_repo_url=  serializers.CharField()
      status_code= serializers.IntegerField()
   