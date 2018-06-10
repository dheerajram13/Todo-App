from django.db import models

# Create your models here.
class Todo(models.Model):
    todo_id = models.AutoField(primary_key=True)  #id for the todo for accesing the elements
    todo_heading = models.CharField(max_length=200) #todo heading with character field
    todo_body = models.TextField()                  #todo body with text field