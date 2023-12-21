from asgiref.sync import async_to_sync
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.exceptions import NotFound
from .utils import generateCode
from .methods import DB
from rest_framework.response import Response
db = DB()


class BoxesView(APIView):

    def get(self, request, code):
        result = async_to_sync(db.selectBoxes)(code)
        if result is None:
            raise NotFound("Code not found")
        return Response(result, status=status.HTTP_200_OK)


class CodeView(APIView):

    def post(self, request):
        code = generateCode()
        result = async_to_sync(db.createCode)(code)
        return Response(status=status.HTTP_201_CREATED)


class LinkView(APIView):

    def post(self, request):
        link = request.data.get('link')
        code = request.data.get('code')
        result = async_to_sync(db.addLink)(link, code)
        if result is None:
            raise NotFound("Code not found")
        return Response(status=status.HTTP_201_CREATED)
