from django.db import models
from django.contrib.auth.hashers import make_password
class User(models.Model):
    USER=   'user'
    ADMIN='admin'
    ROLE_CHOICES=[
        (USER,'User'),(ADMIN,'admin'),

    ]

    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    username=models.CharField(max_length=100,unique=True)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=250)
    joined_date= models.DateTimeField(auto_now_add=True)
    is_active= models.BooleanField(default=True)
    is_verified=models.BooleanField(default=False)
    role=models.CharField(max_length=10,choices=ROLE_CHOICES,default=USER)
    profile_photo =models.ImageField(upload_to='profile_photos/', blank=True, null=True)

    def save(self,*args,**kwargs):
        if self.password:
            self.password=make_password(self.password)
        super().save(*args,**kwargs)
    def __str__(self):
        return self.username
class Otp(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    otp_code=models.CharField(max_length=6)
    otp_expire_at=models.DateTimeField()
    def __str__(self):
        return f"OTP {self.otp_code} for {self.user.username}"
