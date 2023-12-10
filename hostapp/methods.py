from django.db import connection
from rest_framework import status
from rest_framework.response import Response
from .database import Database

class DB:
    def __init__(self):
        self.__db = Database()


    async def selectIdByCode(self, code):
        try:
            await self.__db.connect()
            raw = await self.__db.fetch("SELECT id FROM links WHERE code = $1", code)
            code_id = raw[0]['id']
            await self.__db.close()
        except:
            code_id = None
        return code_id


    async def selectBoxes(self, code):
        code_id = await self.selectIdByCode(code)
        if code_id is None:
            return None
        await self.__db.connect()
        raw = await self.__db.fetch("SELECT link FROM box WHERE code_id = $1", code_id)
        await self.__db.close()
        return raw


    async def createCode(self, code):
        await self.__db.connect()
        await self.__db.execute("INSERT INTO links (user_id, code) VALUES ($1, $2)", 1, code)
        await self.__db.close()


    async def addLink(self, link, code):
        code_id = await self.selectIdByCode(code)
        if code_id is None or link is None:
            return None
        await self.__db.connect()
        await self.__db.execute("INSERT INTO box (link, code_id) VALUES ($1, $2)", link, code_id)
        await self.__db.close()
        return 201
        
