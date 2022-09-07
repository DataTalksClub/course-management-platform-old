from django.db import models

# Create your models here.

class Course(models.Model):
    id = models.AutoField(primary_key=True, editable=False, unique=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True) 
    # course_link = models.Charfield(max_length=2000, null=True, blank=True)
    # projects = 
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title

class Homework(models.Model):
    HW_STATUS = (
        ('active', 'active'),
        ('inactive', 'inactive'),
        ('finished', 'finished')
    )
    id = models.AutoField(primary_key=True, editable=False, unique=True)
    title = models.CharField(max_length=200)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL)
    status = models.CharField(max_length=8, choices=HW_STATUS)
    due_date = models.DateTimeField(null=False, blank=False)
    hw_questions = models.JSONField()

    def __str__(self):
        return self.title



    



    




