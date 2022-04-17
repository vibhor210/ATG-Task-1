from django.db import models
# Create your models here.
class Profile(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    username = models.CharField(max_length=64)
    image = models.ImageField(upload_to="images")
    email = models.EmailField(max_length=62)
    
    def __str__(self):
        return self.username