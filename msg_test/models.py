from django.db import models

# Create your models here.

class msg_test(models.Model):
    msg=models.CharField(max_length=400,null=False)
    
    def __str__(self):
        return self.msg
