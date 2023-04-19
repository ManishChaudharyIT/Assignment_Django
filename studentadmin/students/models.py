from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField()
    physics_marks = models.IntegerField()
    chemistry_marks = models.IntegerField()
    maths_marks = models.IntegerField()
    cs_marks = models.IntegerField()

    def __str__(self):
        return self.name

