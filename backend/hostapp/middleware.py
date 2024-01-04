from asgiref.sync import markcoroutinefunction
from django.utils.decorators import async_only_middleware
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

        if request.path.startswith('/api/links'):
            return await self.get_response(request)

        access_token = request.headers.get('Authorization')
        if access_token is None:
            return HttpResponse('Токен не передан', status=403)


        # async with httpx.AsyncClient() as client:
        #     res = await client.get(f'https://www.googleapis.com/oauth2/v2/userinfo?access_token={access_token}')
        
        #     if res.status_code == 401:
        #         return HttpResponse('Время жизни токена стекло или он не был передан', status=401)

        #     elif res.status_code == 200:
        #         user_info = res.json()
        #         user = await self.__db.fetchUser(user_info['id'])
        #         if not user:
        #             await self.__db.createUser(user_info)
        #             user = await self.__db.fetchUser(user_info['id'])
        #         request.user_info = user[0]
        try:
            async with httpx.AsyncClient() as client:
                res = await client.get(f'https://www.googleapis.com/oauth2/v2/userinfo?access_token={access_token}')
                res.raise_for_status()

                user_info = res.json()
                user = await self.__db.fetchUser(user_info['id'])
                if not user:
                    await self.__db.createUser(user_info)
                    user = await self.__db.fetchUser(user_info['id'])

                request.user_info = user[0]

        except httpx.HTTPStatusError:
            return HttpResponse('Время жизни токена стекло или он не был передан,а так же могли возникнуть иные проблемы', status=401)


        
        return await self.get_response(request)

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