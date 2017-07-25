from django.db import models
from django.contrib.auth.models import User


 
class EmailConfirmation(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE, primary_key=True,)
    status = models.CharField(max_length=30, default='sent')
 
#u = User.objects.get(username='fsmith')
#freds_department = u.employee.department