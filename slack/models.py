from django.db import models

# Create your models here.
class Info(models.Model):
  slack_name = models.CharField(max_length=200)
  current_day = models.CharField(max_length=20)
  utc_time = models.CharField(max_length=100)
  track = models.CharField(max_length=100)
  github_file_url=  models.CharField(max_length=200)
  github_repo_url=  models.CharField(max_length=200)
  status_code= models.PositiveIntegerField(default=200)
  def __str__(self):
    return self.slack_name