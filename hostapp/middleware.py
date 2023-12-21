from asgiref.sync import markcoroutinefunction
from django.utils.decorators import async_only_middleware
import requests
import httpx
from django.http import HttpResponse
from .database import Database
from .methods import DB


@async_only_middleware
class TokenValidationMiddleware:
    
    def __init__(self, get_response):
        self.get_response = get_response
        self.__db = DB()
        markcoroutinefunction(self)

    
    async def __call__(self, request):
        access_token = request.COOKIES.get('access_token')
        
        if access_token is None:
            return HttpResponse('Токен не передан', status=401)


        async with httpx.AsyncClient() as client:
            res = await client.get(f'https://www.googleapis.com/oauth2/v2/userinfo?access_token={access_token}')
        
        if res.status_code == 401:
            return HttpResponse('Время жизни токена стекло', status=401)

        elif res.status_code == 200:
            user_info = res.json()
            request.user_info = user_info
            user_exist = await self.__db.checkUser(user_info['id'])
            if user_exist is False:
                await self.__db.createUser(user_info)

        response = await self.get_response(request)
        
        return response

# import requests
# from rest_framework.response import Response
# from .database import Database
# from .methods import DB



# class TokenValidationMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response
#         self.db = DB()

#     def __call__(self, request):
#         access_token = request.COOKIES.get('access_token')

#         if access_token:
#             response = requests.get(f'https://www.googleapis.com/oauth2/v2/userinfo?access_token={access_token}')

#             if response.status_code == 401:
#                 return Response('Действие токена истекло', status=status.HTTP_401_UNAUTHORIZED)

#             elif response.status_code == 200:
#                 user_info = response.json()
#                 request.user = response.json()
#                 print(request.user_info)
#                 # await self.db.createUser(user_info)

#         response = self.get_response(request)

#         return response

# request.user_info = {
#     'id': user_info.get('id'),
#     'email': user_info.get('email'),
#     'given_name': user_info.get('given_name'),
#     'family_name': user_info.get('family_name'),
#     'picture': user_info.get('picture'),
#     'locale': user_info.get('locale'),
#     'name': user_info.get('name'),
#     'verified_email': user_info.get('verified_email'),
# }