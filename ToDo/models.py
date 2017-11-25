from django.db import models

# Create your models here.
class ToDo(models.Model):
    aToDo = models.CharField(max_length=10000)
    Done = models.BooleanField()
    def __str__(self):
        return str(self.aToDo) 