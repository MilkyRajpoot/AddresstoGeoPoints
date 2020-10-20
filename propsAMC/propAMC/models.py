from django.db import models
from geolocation_fields.models import fields
from .validators import validate_file_extension

# Create your models here.

class UserFile(models.Model):
	username = models.CharField(max_length=255) 
	file = models.FileField(upload_to='files/',validators=[validate_file_extension])
	created_at = models.DateField(auto_now_add=True)
	updated_at = models.DateField(auto_now=True)

	class Meta:
		ordering = ('created_at',)

	def __str__(self):
		return str(self.username)
