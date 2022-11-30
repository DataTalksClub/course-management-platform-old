
# from email.policy import default
from django.db import models
from users.models import User

# Create your models here.

class Course(models.Model):
    id = models.AutoField(primary_key=True, editable=False, unique=True)
    title = models.CharField(max_length=200)
    image = models.ImageField(null=True, blank=True, default="default.svg")
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
    description = models.TextField(null=True, blank=True) 
    course = models.ForeignKey(Course, on_delete=models.PROTECT)
    hidden = models.BooleanField(default=False)
    status = models.CharField(max_length=8, choices=HW_STATUS)
    due_date = models.DateTimeField(null=False, blank=False)
    # hw_questions = models.()

    def __str__(self):
        return self.title

class Question(models.Model):
    TYPE = (
        ('text', 'text'),
        ('radio', 'radio'),
        ('links', 'links')
    )
    id = models.AutoField(primary_key=True, editable=False, unique=True)
    hw = models.ForeignKey(Homework, on_delete=models.PROTECT )
   
    type = models.CharField(max_length=5, choices=TYPE)
    question = models.TextField(max_length=1000)
    options = models.JSONField(blank=True, null=True)
    correct_answer = models.JSONField(blank=True, null=True)
    
    def __str__(self):
        return self.question


class Leaderboard(models.Model):
    id = models.AutoField(primary_key=True, editable=False, unique=True)
    # student = models.
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    email_hash = models.CharField(max_length=40, null=False, blank=False)
    scores = models.JSONField()
    total_score = models.IntegerField(default=0, null=True, blank=True)

class Submission(models.Model):
    id = models.AutoField(primary_key=True, editable=False, unique=True)
    homework = models.ForeignKey(Homework, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    answer = models.JSONField(blank=True, null=True)
    status = models.CharField(max_length=255)


class Enrolment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True, editable=False, unique=True)



    

    



    




