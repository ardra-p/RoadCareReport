from django.db import models

class Complaint(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    latitude = models.FloatField()
    longitude = models.FloatField()
    address = models.CharField(max_length=300, blank=True, null=True)
    photo = models.ImageField(upload_to='complaints/', null=True)
    created_at = models.DateTimeField(auto_now_add=True)