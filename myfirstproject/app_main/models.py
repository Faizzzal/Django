from django.db import models

# Create your models here.
class Students(models.Model):
  name = models.CharField(max_length=255)
  email = models.EmailField()
  roll_no=models.IntegerField()
  DOA=models.DateField(auto_now_add=True)
  
class Classroom(models.Model):
  name_of_class=models.TextField()
  class_teacher=models.TextField(max_length=20)

class Teachers(models.Model):
  name_of_teacher=models.TextField()
  sub_teacher=models.TextField()
  teacher_id=models.IntegerField(primary_key=True)

class Marks(models.Model):
  maths=models.IntegerField()
  science=models.IntegerField()
  english=models.IntegerField()
  hindi=models.IntegerField()
  computer=models.IntegerField()
    