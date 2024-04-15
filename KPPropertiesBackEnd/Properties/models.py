from django.db import models

# Create your models here.
class Property(models.Model):
	name = models.CharField(max_length=255)
	category = models.CharField(max_length=255, default="Rent")
	address = models.TextField(null=True,blank=True)
	description = models.TextField(null=True,blank=True)
	num_of_floors = models.PositiveIntegerField(null=True,blank=True)
	year_built = models.PositiveIntegerField(null=True, blank=True)

	class Meta:
		verbose_name = 'property'
		verbose_name_plural = 'properties'
	def __str__(self):
		return self.name