from django.db import models
import uuid
# Create your models here.


class Event(models.Model):
    title = models.CharField(max_length=64)
    start_date = models.DateField()
    end_date = models.DateField()
    thumbnail = models.ImageField(upload_to='thumbnails/')

class Registration(models.Model):
    code = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE)

