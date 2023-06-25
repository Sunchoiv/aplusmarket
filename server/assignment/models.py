from django.db import models

# Create your models here.
class Assignment(models.Model):
    major = models.CharField(max_length=20)
    subject = models.CharField(max_length=20)
    professorname = models.CharField(max_length=20)
    assignmentname = models.CharField(max_length=20)
    grade = models.CharField(max_length=20)

    def __str__(self):
        return self.assignmentname
