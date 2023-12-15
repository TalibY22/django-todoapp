from django.db import models
from django.contrib.auth.models import User


#create table Todo
class todo(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="Todo",null=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
#Create model item 
class item(models.Model):
    todolist = models.ForeignKey(todo,on_delete=models.CASCADE)
    text=models.CharField(max_length=200)
    complete = models.BooleanField()

    def __str__(self):
        return self.text