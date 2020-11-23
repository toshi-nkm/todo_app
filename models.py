from django.db import models

# Create your models here.
PRIORTY = (('danger','heiht'),('info','normal'),('success','low'))
class TodoModel(models.Model):
    title = models.CharField(max_length=100)
    memo = models.TextField()
    priority = models.CharField(
        max_length = 50,
        choices = PRIORTY,
    )
    deudate = models.DateField()
    def __str__(self):
        return self.title