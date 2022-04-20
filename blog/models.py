from django.db import models
from django.contrib.auth.models import User
# Create your models here.

cat_choice = (
    ("MH","Mental Health"),
    ("HD","Heart Disease"),
    ("C-19","Covid-19"),
    ("Imu","Immunization"),
)

class blog(models.Model):
    title = models.TextField()
    image = models.ImageField(upload_to="blog/images")
    category = models.CharField(max_length=20,choices=cat_choice,default="Mental Health")
    author = models.ForeignKey(User, on_delete= models.CASCADE)
    draft = models.BooleanField(default=False)
    summary = models.TextField()
    content = models.TextField()

    def __str__(self):
        return self.title