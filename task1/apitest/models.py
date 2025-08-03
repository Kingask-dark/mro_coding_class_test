from django.db import models

# Create your models here.
class LessionList(models.Model):
    lession = models.CharField(max_length=50)
    lession_details = models.CharField(max_length=250)
    title = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class meta:
        verbose_name = "Lession List"
        verbose_name_plural = "Lession List's"
    
    def __str__(self):
        return self.title
    