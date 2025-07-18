from django.db import models
import auto_prefetch
import os
from django.dispatch import receiver

class CustomTemplate(models.Model):
    file = models.FileField(upload_to = 'reports/', null=False, blank=False, unique = False)
    name = models.CharField(max_length = 255, default = "User Generated")
    
    def __str__(self):
        return self.name    
    
@receiver(models.signals.post_delete, sender=CustomTemplate)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding `CustomTemplate` object is deleted.
    """
    if instance.file:
        if os.path.isfile(instance.file.path):
            os.remove(instance.file.path)