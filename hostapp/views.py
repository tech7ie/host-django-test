from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.db import connection


class Messages:

	@api_view(['GET'])
	def getHello(request):
		return Response({"message": "Hello, World!"})



class CRUD:

	@api_view(['GET'])
	def getUsers(request):
	    with connection.cursor() as cursor:
	        cursor.execute("SELECT * FROM users")
	        rows = cursor.fetchall()

	    return Response({"users": rows})
