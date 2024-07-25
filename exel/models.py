from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import os

def validate_file_extension(value):
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.xlsx', '.xls']  # Add your valid extensions here
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension. Allowed extensions are: ' + ', '.join(valid_extensions))


class ReportsModel(models.Model):
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    sent_at = models.DateTimeField(null=True, blank=True)
    file = models.FileField(upload_to='reports/', validators=[validate_file_extension])
    title = models.CharField(max_length=255, null=True, blank=True)
    import_id = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return str(self.id)
