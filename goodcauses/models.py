from django.db import models

# Create your models here.
class Signin(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)
    email = models.CharField(max_length=40)

    TYPE_CHOICES = (
        ('Philanthropic', 'Philanthropic'),
        ('NGO', 'NGO')
    )
    type = models.CharField(max_length=50, choices=TYPE_CHOICES)
    
    password = models.CharField(max_length=30, default="nit-hackathon@512")
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name + ' ' + self.type

class Profile(models.Model):
    sno = models.AutoField(primary_key=True)
    orgname = models.CharField(max_length=40, default="NGO1")
    phone = models.TextField(max_length=13)
    previouswork = models.TextField()
    futuregoals = models.TextField()
    fundingneeds = models.TextField()
    files = models.FileField(upload_to='files')
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.orgname + ' ' + self.previouswork

class Funds(models.Model):
    sno = models.AutoField(primary_key=True)
    frname = models.CharField(max_length=40, default="NGO1")
    frphone = models.TextField(max_length=13)
    eventdesc = models.TextField()
    funds = models.TextField()
    documents = models.FileField(upload_to='files')
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.frname + ' ' + self.eventdesc

class Feedback(models.Model):
    sno = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=40, default="NGO1")
    femail = models.CharField(max_length=40)
    COUNTRY_CHOICES = (
        ('India', 'India'),
        ('Canada', 'Canada'),
        ('Other', 'Other')
    )
    country = models.CharField(max_length=50, choices=COUNTRY_CHOICES)
    desc = models.TextField()
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.fname + ' ' + self.desc

