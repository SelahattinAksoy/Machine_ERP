from django.db import models

# Create your models here.

class note(models.Model):
    notehead=models.CharField(max_length=100)
    note=models.TextField()
    def __str__(self):
        return self.notehead;