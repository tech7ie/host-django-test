from asgiref.sync import async_to_sync
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .utils import generateCode
from .methods import DB

db = DB()

class GET:

	@api_view(['GET'])
	def boxes(request, code):
		result = async_to_sync(db.selectBoxes)(code)
		if result is None:
			return Response("Code not found", status=status.HTTP_400_BAD_REQUEST)
		
		return Response(result, status=status.HTTP_200_OK)


class POST:

	@api_view(['POST'])
	def create_code(request):
		code = generateCode()
		result = async_to_sync(db.createCode)(code)

		return Response(status=status.HTTP_201_CREATED)

	@api_view(['POST'])
	def add_link(request):
		link = request.data.get('link')
		code = request.data.get('code')
		result = async_to_sync(db.addLink)(link, code)
		if result is None:
			return Response("Code not found", status=status.HTTP_400_BAD_REQUEST)

		return Response(status=status.HTTP_201_CREATED)