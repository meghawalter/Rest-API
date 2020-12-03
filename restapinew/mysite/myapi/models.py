from django.db import models

class Student(models.Model):
    name=models.CharField(max_length=100)
    rollno=models.IntegerField()
    ranking=models.FloatField()

    def __str__(self):
        return f"{self.name} - {self.rollno}"