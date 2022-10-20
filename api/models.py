from django.db import models

# Create your models here.
class Entry(models.Model):
    created = models.DateTimeField(auto_now_add=True, blank=True)
    user = models.CharField(max_length=64)
    name = models.CharField(max_length=64)
    time = models.FloatField(default=0)
    complexity = models.FloatField(default=0)
    memory = models.FloatField(default=0)
    # <QueryDict: {'user': ['hxr'], 'function': ['mean1'], 'time': ['9488.2'], 'complexity': ['4.5']}>
