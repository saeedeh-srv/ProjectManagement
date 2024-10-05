from django.db import models
from django.contrib.auth.models import User



class Project(models.Model):
    COLOR_CHOICES = (
        ('red', 'red'),
        ('black', 'black'),
        ('blue', 'blue'),
        ('green', 'green'),
        ('gray', 'gray'),
        ('pink', 'pink'),
        ('yellow', 'yellow'),
    )
    title=models.CharField(max_length=50 )
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    description=models.TextField()
    color=models.CharField(max_length=6,choices=COLOR_CHOICES)
    image=models.ImageField(upload_to='projects/projects',default='projects/default/project_d.png')
    start_date=models.DateField(null=True,blank=True)
    end_date=models.DateField(null=True,blank=True)
    status=models.BooleanField(default=False)
    bujet=models.PositiveBigIntegerField(null=True,blank=True)

    def __str__(self):
        return self.user.username


# Create your models here.
