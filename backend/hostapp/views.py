from asgiref.sync import async_to_sync
from adrf.views import APIView
from rest_framework import status
from rest_framework.exceptions import NotFound
from .utils import generateCode
from .methods import DB
from rest_framework.response import Response
db = DB()


class BoxesView(APIView):

    # Отдает все ссылки по коду.
    async def get(self, request):
        code = request.GET.get('code', '')
        result = await db.getLinks(code)
        if result is None:
            raise NotFound("Code not found")
        return Response(result, status=status.HTTP_200_OK)


class CodeView(APIView):

    # Это дитятко-ошибка. по шизе сделал, но его скорее всего и оставить.
    async def get(self, request):
        code = request.GET.get('code', '')
        result = await db.getLinks(code)
        return Response(result, status=status.HTTP_200_OK)

    # Создание нового кода ссылки
    async def post(self, request):
        user_id = request.user_info['id']
        code = generateCode()
        result = await db.createCode(user_id, code)
        return Response(code, status=status.HTTP_201_CREATED)


class LinkView(APIView):

    # Добавление ссылок с привязкой к коду ссылки.
    async def post(self, request):
        link = request.data.get('links')
        code = request.data.get('code')
        check = await db.getLinks(code)
        if check:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        result = await db.addLinks(link, code)
        if result is None:
            raise NotFound("Code not found")
        return Response(check, status=status.HTTP_201_CREATED)




# from asgiref.sync import async_to_sync
# from rest_framework.views import APIView
# from rest_framework import status
# from rest_framework.exceptions import NotFound
# from .utils import generateCode
# from .methods import DB
# from rest_framework.response import Response
# db = DB()


# class BoxesView(APIView):

#     # Отдает все ссылки по коду.
#     def get(self, request):
#         code = request.GET.get('code', '')
#         result = async_to_sync(db.getLinks)(code)
#         if result is None:
#             raise NotFound("Code not found")
#         return Response(result, status=status.HTTP_200_OK)


# class CodeView(APIView):

#     # Это дитятко-ошибка. по шизе сделал, но его скорее всего и оставить.
#     def get(self, request):
#         code = request.GET.get('code', '')
#         result = async_to_sync(db.getLinks)(code)
#         return Response(result, status=status.HTTP_200_OK)

#     # Создание нового кода ссылки
#     def post(self, request):
#         user_id = request.user_info['id']
#         code = generateCode()
#         result = async_to_sync(db.createCode)(user_id, code)
#         return Response(code, status=status.HTTP_201_CREATED)


# class LinkView(APIView):

#     # Добавление ссылок с привязкой к коду ссылки.
#     def post(self, request):
#         link = request.data.get('links')
#         code = request.data.get('code')
#         check = async_to_sync(db.getLinks)(code)
#         if check:
#             return Response(status=status.HTTP_400_BAD_REQUEST)
#         result = async_to_sync(db.addLinks)(link, code)
#         if result is None:
#             raise NotFound("Code not found")
#         return Response(check, status=status.HTTP_201_CREATED)


        
# from asgiref.sync import async_to_sync
# from rest_framework.views import APIView
# from rest_framework import status
# from rest_framework.exceptions import NotFound
# from .utils import generateCode
# from .methods import DB
# from rest_framework.response import Response
# from adrf.decorators import api_view
# db = DB()


# class BoxesView:

#     # Отдает все ссылки по коду.
#     @api_view(['GET'])
#     async def get(request):
#         code = request.GET.get('code', '')
#         result = await db.getLinks(code)
#         if result is None:
#             raise NotFound("Code not found")
#         return Response(result, status=status.HTTP_200_OK)


# class CodeView:

#     # Это дитятко-ошибка. по шизе сделал, но его скорее всего и оставить.
#     @api_view(['GET'])
#     async def get(request):
#         code = request.GET.get('code', '')
#         result = await db.getLinks(code)
#         return Response(result, status=status.HTTP_200_OK)

#     # Создание нового кода ссылки
#     @api_view(['POST'])
#     async def post(request):
#         user_id = request.user_info['id']
#         code = generateCode()
#         result = await db.createCode(user_id, code)
#         return Response(code, status=status.HTTP_201_CREATED)


# class LinkView:

#     # Добавление ссылок с привязкой к коду ссылки.
#     @api_view(['POST'])
#     async def post(request):
#         link = request.data.get('links')
#         code = request.data.get('code')
#         check = await db.getLinks(code)
#         if check:
#             return Response(status=status.HTTP_400_BAD_REQUEST)
#         result = await db.addLinks(link, code)
#         if result is None:
#             raise NotFound("Code not found")
#         return Response(check, status=status.HTTP_201_CREATED)