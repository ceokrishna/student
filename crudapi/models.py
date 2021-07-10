from django.db import models

# Create your models here.

class Student1(models.Model):
    stud_no=models.IntegerField()
    stud_name=models.CharField(max_length=200)
    stud_dob=models.DateField()
    stud_doj=models.DateField()

    def __str__(self):
        return self.title  #this line is used for admin pannel show only title
