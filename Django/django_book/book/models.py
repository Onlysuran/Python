from django.db import models

# Create your models here.
class Book(models.Model):
    t_id = models.AutoField(primary_key=True)
    t_name = models.CharField(max_length=100)
    t_price=models.IntegerField()
    t_type=models.CharField(max_length=100)
    t_publisher=models.CharField(max_length=100)
    t_date=models.DateField()
    t_updown=models.CharField(max_length=100)

    class Meta:
        db_table = 't_book'