from django.db import models

# Create your models here.



class Student(models.Model):
    firstName = models.CharField(max_length=128, unique = True)
    lastName = models.CharField(max_length = 128)
    numberOfCats = models.IntegerField(default = 0)
    
    
    def __str__(self):
        return self.firstName
    



class cat (models.Model):
    catName = models.CharField(max_length=128)
    studentName = models.ForeignKey(Student, on_delete = models.CASCADE)
    
    def __str__(self):
        return self.catName
    
