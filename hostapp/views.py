from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .utils import generateCode
from .methods import DB

class GET:

	@api_view(['GET'])
	def boxes(request, code):
		result = DB.selectBoxes(code)
		
		return Response(result)


class POST:

	@api_view(['POST'])
	def newCode(request):
		code = generateCode()
		DB.createCode(code)

		return Response(status=status.HTTP_201_CREATED)

	@api_view(['POST'])
	def newLink(request, code):
		link = request.data['link']
		DB.addLink(link, code)

		return Response(status=status.HTTP_201_CREATED)