from django.db import models

# Create your models here.
class JD(models.Model):
    title = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    industry = models.CharField(max_length=50)
    description = models.TextField()
    
    class Meta:
        verbose_name = 'Job'
        verbose_name_plural = 'Jobs'

    def __str__(self):
        return self.title