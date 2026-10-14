from django.db import models

# Create your models here.

class Student(models.Model):

    COURSES=[
        ('PFS','Python Full Stack'),
        ('JFS','Java Full Stack'),
        ('MERN','MERN Stack')
    ]

    profile_pic = models.ImageField(blank=True)
    name = models.CharField(max_length=100)
    roll_no = models.IntegerField()
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=14)
    course = models.CharField(max_length=100 , choices=COURSES)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.name

