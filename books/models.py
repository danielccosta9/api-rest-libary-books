import uuid
from django.db import models

# Create your models here.

def upload_image_book(instance, filename):
    return f'{instance.id_book}/{filename}'

class Books(models.Model):
    id_book = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    edition = models.CharField(max_length=255)
    release_year = models.IntegerField()
    state = models.CharField(max_length=255)
    pages = models.IntegerField()
    publish_company = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='books/', blank=True, null=True)
    