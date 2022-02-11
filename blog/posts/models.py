from django.db import models
from datetime import datetime
# Create your models here.
class Posts(models.Model):
    title=models.CharField(max_length=50)
    text=models.CharField(max_length=100)
    created=models.DateTimeField(default=datetime.now,blank=True)
