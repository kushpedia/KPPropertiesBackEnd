from django.http import JsonResponse

def getRoutes(request):
	routes = [
		{'GET' : '/properties'},
		{'GET' : '/properties/id'},
		{'DELETE' : '/properties/id'},
		    ]
	return JsonResponse(routes,safe=False)