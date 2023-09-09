from rest_framework import serializers
from .models import *

class InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model= Info
        fields = ('slack_name', 'current_day', 'utc_time', 'track', 'github_file_url','github_repo_url', 'status_code' )