from django.db import models

# Create your models here.

class Student(models.Model):
    t_id = models.AutoField(primary_key=True)
    t_name = models.CharField(max_length=100)
    t_age = models.IntegerField()
    t_sex = models.CharField(max_length=100)
    t_address = models.CharField(max_length=100)
    t_hobby = models.CharField(max_length=100)
    t_date = models.DateField()
    class Meta:
        db_table = 't_student'
