from django.db import connection
from rest_framework import status
from rest_framework.response import Response
from .database import Database



class DB:


    @staticmethod
    async def selectIdByCode(code):
        try:
            db = Database()
            await db.connect()
            raw = await db.fetch("SELECT id FROM links WHERE code = $1", code)
            code_id = raw[0]['id']
            await db.close()
        except:
            code_id = None
        return code_id


    @staticmethod
    async def selectBoxes(code):
        code_id = await DB.selectIdByCode(code)
        if code_id is None:
            return None

        db = Database()
        await db.connect()
        raw = await db.fetch("SELECT link FROM box WHERE code_id = $1", code_id)
        await db.close()
        return raw


    @staticmethod
    async def createCode(code):
        db = Database()
        await db.connect()
        await db.execute("INSERT INTO links (user_id, code) VALUES ($1, $2)", 1, code)
        await db.close()


    @staticmethod
    async def addLink(link, code):
        code_id = await DB.selectIdByCode(code)
        if code_id is None:
            return None

        db = Database()
        await db.connect()
        await db.execute("INSERT INTO box (link, code_id) VALUES ($1, $2)", link, code_id)
        await db.close()
        return 201
        
