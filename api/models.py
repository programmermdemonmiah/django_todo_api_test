from django.db import models

class User(models.Model):
    username = models.CharField(max_length=255, unique=True)
    first_name = models.CharField(max_length=50, null= True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    email = models.CharField(max_length=100, unique=True)
    phone = models.CharField(max_length=15, unique=True)
    age = models.IntegerField()
    image = models.ImageField(upload_to='users/images/', default='profile_image.png') 
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 


    def __str__(self):
        return self.username
    
    class Meta:
            db_table = 'users'