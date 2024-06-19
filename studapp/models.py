from django.db import models
from django.contrib.auth.models import User


# makemigration = Create changes and store in a one file
# migrate = apply the pending changes created by makemigrations
# Create your models here.
# class Registration(models.Model):
    # name = models.CharField(max_length=100)
    # email = models.CharField(max_length=100)
    # password = models.CharField(max_length=100)
    # mobile_no = models.CharField(max_length=12)
    # address = models.TextField()
    # date = models.DateField()

    # def __str__(self):
    #     return self.name

class Accommodation(models.Model):
    a_id = models.AutoField
    a_name = models.CharField(max_length=100)
    a_address = models.CharField(max_length=100)
    a_type = models.CharField(max_length=100)
    a_fecility = models.TextField()
    a_rent = models.CharField(max_length=100)
    a_photo1 = models.FileField(upload_to='static/documents/')
    # a_photo2 = models.FileField(upload_to='static/documents/')
    a_photo3 = models.FileField(upload_to='static/documents/')
    date = models.DateField()

    def __str__(self):
        return self.a_name

class Enquire(models.Model):
    e_id = models.AutoField
    e_user_id = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    e_phone = models.CharField(max_length=15)
    e_query = models.TextField()
    e_date = models.DateField()

    def __str__(self):
        return self.e_phone