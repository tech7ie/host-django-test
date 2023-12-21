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
        

    async def checkUser(self, user_id):
        await self.__db.connect()
        user = await self.__db.fetch("SELECT id FROM users WHERE user_id = $1", user_id)
        await self.__db.close()
        return True# if user else False

    async def createUser(self, user_info):
        await self.__db.connect()
        await self.__db.execute("""
            INSERT INTO users (email, given_name, family_name, picture, locale, name, verified_email) 
            VALUES ($1, $2, $3, $4, $5, $6, $7)
        """, user_info['email'], user_info['given_name'], user_info['family_name'],
                user_info['picture'], user_info['locale'], user_info['name'], user_info['verified_email'])
        await self.__db.close()