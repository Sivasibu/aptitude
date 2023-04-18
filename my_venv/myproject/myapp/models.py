from django.db import models

# Create your models here.
class Exam(models.Model):
    id = models.AutoField(primary_key=True)
    department = models.CharField(max_length=50)
    role = models.CharField(max_length=50)
    topic = models.CharField(max_length=100)
    question = models.TextField()
    answeroption = models.CharField(max_length=50)
    a = models.CharField(max_length=100)
    b = models.CharField(max_length=100)
    c = models.CharField(max_length=100)
    d = models.CharField(max_length=100)

    def __str__(self):
        return self.department
