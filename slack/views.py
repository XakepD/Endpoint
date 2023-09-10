from django.shortcuts import render
from rest_framework import views, response
from .models import *
from .serializers import *
import datetime
from django.utils import timezone
import pytz
# Create your views here.
class InfoView(views.APIView):
    def get(self,request):
        cDay =datetime.datetime.now().strftime("%A")
        
        d1 = datetime.datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
        d2 = datetime.datetime.strptime(d1,"%Y-%m-%dT%H:%M:%S.%fZ")
        utime = d2.strftime("%Y-%m-%dT%H:%M:%SZ")
        sn = request.GET.get('slack_name')
        trk = request.GET.get('track')
        infos = {'slack_name':sn, 
                 'current_day':cDay, 
                 'utc_time':utime, 
                 'track':trk, 'github_file_url':"https://github.com/XakepD/Endpoint/blob/main/slack/views.py" ,
                 'github_repo_url': "https://github.com/XakepD/Endpoint.git", 'status_code': 200}
        outpt = InfoSerializer(infos, many=False).data
        return response.Response(outpt)
    