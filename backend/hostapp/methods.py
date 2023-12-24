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

    async def getLinks(self, code):
        code_id = await self.selectIdByCode(code)
        await self.__db.connect()
        links = await self.__db.fetch("SELECT * FROM box WHERE code_id = $1 ", code_id)
        await self.__db.close()
        return links

    async def createCode(self, user_id, code):
        await self.__db.connect()
        await self.__db.execute("INSERT INTO links (user_id, code) VALUES ($1, $2)", user_id, code)
        await self.__db.close()
        return

    async def checkCode(self, code):

        await self.__db.connect()
        link = await self.__db.fetch("SELECT * FROM links WHERE code = $1 ", code)
        await self.__db.close()
        return link

    # async def addLink(self, link, code):
    #     code_id = await self.selectIdByCode(code)
    #     if code_id is None or link is None:
    #         return None
    #     await self.__db.connect()
    #     await self.__db.execute("INSERT INTO box (link, code_id) VALUES ($1, $2)", link, code_id)
    #     await self.__db.close()
    #     return 201
    async def addLinks(self, links, code):
        code_id = await self.selectIdByCode(code)
        if code_id is None or not links:
            return None
        await self.__db.connect()
        values = ', '.join([f"('{link}', {code_id})" for link in links])
        await self.__db.execute(f"INSERT INTO box (link, code_id) VALUES {values}")
        await self.__db.close()
        return 201
        

    async def fetchUser(self, user_id):
        await self.__db.connect()
        user = await self.__db.fetch("SELECT * FROM users WHERE user_id = $1", user_id)
        await self.__db.close()
        return user

    async def createUser(self, user_info):
        await self.__db.connect()
        await self.__db.execute("""
            INSERT INTO users (email, given_name, family_name, picture, locale, name, verified_email, user_id) 
            VALUES ($1, $2, $3, $4, $5, $6, $7, $8)
        """, user_info.get('email'), user_info.get('given_name'), user_info.get('family_name'),
                user_info.get('picture'), user_info.get('locale'), user_info.get('name'), user_info.get('verified_email'), user_info.get('id'))
        await self.__db.close()
