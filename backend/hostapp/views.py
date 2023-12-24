from asgiref.sync import async_to_sync
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.exceptions import NotFound
from .utils import generateCode
from .methods import DB
from rest_framework.response import Response
db = DB()


class BoxesView(APIView):

    def get(self, request):
        code = request.GET.get('code', '')
        result = async_to_sync(db.selectBoxes)(code)
        if result is None:
            raise NotFound("Code not found")
        return Response(result, status=status.HTTP_200_OK)


class CodeView(APIView):

    def get(self, request):
        code = request.GET.get('code', '')
        result = async_to_sync(db.getLinks)(code)
        # if result:
        return Response(result, status=status.HTTP_200_OK)
        #return Response(status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        user_id = request.user_info['id']
        code = generateCode()
        result = async_to_sync(db.createCode)(user_id, code)
        return Response(code, status=status.HTTP_201_CREATED)


class LinkView(APIView):

    def post(self, request):
        link = request.data.get('links')
        code = request.data.get('code')
        check = async_to_sync(db.getLinks)(code)
        if check:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        result = async_to_sync(db.addLinks)(link, code)
        if result is None:
            raise NotFound("Code not found")
        return Response(check, status=status.HTTP_201_CREATED)
