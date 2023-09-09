from django.shortcuts import render
from rest_framework import viewsets, filters
from .models import *
from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend
import datetime
# Create your views here.
class InfoView(viewsets.ModelViewSet):
    serializer_class = InfoSerializer
    queryset = Info.objects.all()
    p = Info.objects.get(id=1)
    p.current_day =datetime.datetime.now().strftime("%A")
    p.utc_time = datetime.datetime.now()
    p.save()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['slack_name', 'track']