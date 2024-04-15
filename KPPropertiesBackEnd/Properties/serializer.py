from rest_framework import serializers
from . models import *

class ReactSerializer(serializers.ModelSerializer):
	class Meta:
		model = Property
		fields = ['name', 'address','description','num_of_floors','year_built','category']