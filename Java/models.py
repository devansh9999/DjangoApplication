from django.db import models

# Create your models here.
class AddData(models.Model):
    Question_No=models.IntegerField(unique=True)
    Type=models.TextField(max_length=20)
    Question=models.TextField(max_length=2000)
    Algorithm=models.TextField(default="-",blank=True)
    Solution=models.TextField(max_length=2000)

    def __str__(self):
        return self.Type

class Notes(models.Model):
    Topic=models.CharField(max_length=1000)
    Notes=models.TextField(max_length=10000,null=True,blank=True)
    Image=models.ImageField(upload_to="image/",null=True,blank=True)

    def __str__(self):
        return self.Topic