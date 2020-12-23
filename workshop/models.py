from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.core.files.storage import default_storage as storage
from django.utils import timezone


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='profile_pics')
    bio = models.CharField(max_length=30,null=True, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


        img = Image.open(self.image)

     

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

class Workshop(models.Model):
    branches=(
        ('CSE','CSE'),
        ('ECE','ECE'),
        ('IT','IT'),
        ('MECHANICAL','MECHANICAL'),
        ('EEE','EEE')
    )
    Name_of_workshop=models.CharField(max_length=30)     
    Organized_by =models.CharField(max_length=30,choices=branches)
    Any_queeries=models.EmailField(default=False)
    Date_of_published=models.DateTimeField(auto_now_add=True,null=True)  
    Date_of_conduction=models.DateTimeField()
    Information=models.CharField(max_length=60) 
       

    def __str__(self):
        return self.Name_of_workshop
