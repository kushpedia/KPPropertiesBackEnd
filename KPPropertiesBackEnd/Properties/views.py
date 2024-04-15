from django.shortcuts import render
from django.http import HttpResponse
from . models import *
from . serializer import *
from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.
# def properties(request):	
# 	data = {
# 		'Name' : "henry kuria",
# 		'Email' : "henrykuria10@gmail.com"
# 	}
# 	return HttpResponse(data['Name'])


class ReactView(APIView):
	def get(self,request):
		output = [
			{"name": output.name,
			"address": output.address,
			"description": output.description,	
			"num_of_floors": output.num_of_floors,
			"year_built": output.year_built,
			"category": output.category,
			
			} for output in Property.objects.all()
		]
		return Response(output)
	def post(self, request):
		serializer = ReactSerializer(data=request.data)
		if serializer.is_valid(raise_exception=True):
			serializer.save()
			return Response(serializer.data)