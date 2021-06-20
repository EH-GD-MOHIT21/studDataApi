from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class ApiPermissions(models.Model):
    index = models.OneToOneField(User,on_delete=models.CASCADE)
    get_api_permission = models.BooleanField(default=False)
    post_api_permission = models.BooleanField(default=False)
    put_api_permission = models.BooleanField(default=False)
    patch_api_permission = models.BooleanField(default=False)
    delete_api_permission = models.BooleanField(default=False)

class SubscriptionType(models.Model):
    index = models.OneToOneField(User,on_delete=models.CASCADE)
    free_plan = models.BooleanField(default=True)
    silver_plan = models.BooleanField(default=False)
    gold_plan = models.BooleanField(default=False)
    diamond_plan = models.BooleanField(default=False)

class CustomUserModel(models.Model):
    index = models.OneToOneField(User,on_delete=models.CASCADE)
    api_key = models.CharField(max_length=100)
    limit = models.CharField(max_length=10,default="50")

class UserData(models.Model):
    name_of_student = models.CharField(max_length=40)
    college_name = models.CharField(max_length=50)
    year_of_study = models.IntegerField()
    father_name = models.CharField(max_length=50)
    course_enrolled = models.CharField(max_length=50)
    age = models.IntegerField()
    email = models.EmailField()
    address = models.CharField(max_length=200)
    phone_no = models.CharField(max_length=12)
    # set data limit 10 in views
    def __str__(self):
        return self.name_of_student
