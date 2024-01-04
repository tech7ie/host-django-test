# from .database import Database


# class DB:
#     def __init__(self):
#         self.__db = Database()
#         self.__db.connect()


#     async def selectIdByCode(self, code):
#         try:
#             raw = await self.__db.fetch("SELECT id FROM links WHERE code = $1", code)
#             code_id = raw[0]['id']
#         except:
#             code_id = None
#         return code_id


#     async def selectBoxes(self, code):
#         code_id = await self.selectIdByCode(code)
#         if code_id is None:
#             return None
#         raw = await self.__db.fetch("SELECT link FROM box WHERE code_id = $1", code_id)
#         return raw

#     async def getLinks(self, code):
#         code_id = await self.selectIdByCode(code)
#         links = await self.__db.fetch("SELECT * FROM box WHERE code_id = $1 ", code_id)
#         return links

#     async def createCode(self, user_id, code):
#         await self.__db.execute("INSERT INTO links (user_id, code) VALUES ($1, $2)", user_id, code)

#     async def checkCode(self, code):

#         link = await self.__db.fetch("SELECT * FROM links WHERE code = $1 ", code)
#         return link

#     # async def addLink(self, link, code):
#     #     code_id = await self.selectIdByCode(code)
#     #     if code_id is None or link is None:
#     #         return None
#     #     await self.__db.connect()
#     #     await self.__db.execute("INSERT INTO box (link, code_id) VALUES ($1, $2)", link, code_id)
#     #     await self.__db.close()
#     #     return 201
#     async def addLinks(self, links, code):
#         code_id = await self.selectIdByCode(code)
#         if code_id is None or not links:
#             return None
#         values = ', '.join([f"('{link}', {code_id})" for link in links])
#         await self.__db.execute(f"INSERT INTO box (link, code_id) VALUES {values}")
#         return 201
        

#     async def fetchUser(self, user_id):
#         user = await self.__db.fetch("SELECT * FROM users WHERE user_id = $1", user_id)
#         return user

#     async def createUser(self, user_info):
#         await self.__db.execute("""
#             INSERT INTO users (email, given_name, family_name, picture, locale, name, verified_email, user_id) 
#             VALUES ($1, $2, $3, $4, $5, $6, $7, $8)
#         """, user_info.get('email'), user_info.get('given_name'), user_info.get('family_name'),
#                 user_info.get('picture'), user_info.get('locale'), user_info.get('name'), user_info.get('verified_email'), user_info.get('id'))
# import os
# import asyncpg

# class DB:
#     def __init__(self):
#         self.db_name = os.getenv('DB_NAME')
#         self.user = os.getenv('DB_USER')
#         self.password = os.getenv('DB_PASSWORD')
#         self.host = os.getenv('DB_HOST')
#         self.port = os.getenv('DB_PORT')
#         self.conn = None

#     async def connect(self):
#         if self.conn is None:
#             self.conn = await asyncpg.connect(
#                 database=self.db_name,
#                 user=self.user,
#                 password=self.password,
#                 host=self.host,
#                 port=self.port
#             )

#     async def selectIdByCode(self, code):
#         try:
#             await self.connect()
#             raw = await self.conn.fetch("SELECT id FROM links WHERE code = $1", code)
#             code_id = raw[0]['id']
#         except:
#             code_id = None
#         return code_id

#     async def selectBoxes(self, code):
#         code_id = await self.selectIdByCode(code)
#         if code_id is None:
#             return None
#         await self.connect()
#         raw = await self.conn.fetch("SELECT link FROM box WHERE code_id = $1", code_id)
#         return raw

#     async def getLinks(self, code):
#         code_id = await self.selectIdByCode(code)
#         await self.connect()
#         links = await self.conn.fetch("SELECT * FROM box WHERE code_id = $1 ", code_id)
#         return links

#     async def createCode(self, user_id, code):
#         await self.connect()
#         await self.conn.execute("INSERT INTO links (user_id, code) VALUES ($1, $2)", user_id, code)

#     async def checkCode(self, code):
#         await self.connect()
#         link = await self.conn.fetch("SELECT * FROM links WHERE code = $1 ", code)
#         return link

#     async def addLinks(self, links, code):
#         code_id = await self.selectIdByCode(code)
#         if code_id is None or not links:
#             return None
#         values = ', '.join([f"('{link}', {code_id})" for link in links])
#         await self.connect()
#         await self.conn.execute(f"INSERT INTO box (link, code_id) VALUES {values}")
#         return 201

#     async def fetchUser(self, user_id):
#         await self.connect()
#         user = await self.conn.fetch("SELECT * FROM users WHERE user_id = $1", user_id)
#         return user

#     async def createUser(self, user_info):
#         await self.connect()
#         await self.conn.execute("""
#             INSERT INTO users (email, given_name, family_name, picture, locale, name, verified_email, user_id) 
#             VALUES ($1, $2, $3, $4, $5, $6, $7, $8)
#         """, user_info.get('email'), user_info.get('given_name'), user_info.get('family_name'),
#                 user_info.get('picture'), user_info.get('locale'), user_info.get('name'), user_info.get('verified_email'), user_info.get('id'))
from .database import Database

class DB:
    def __init__(self):
        self.db = Database()

    # Берем id кода по коду
    async def selectIdByCode(self, code):
        try:
            raw = await self.db.fetch("SELECT id FROM links WHERE code = $1", code)
            code_id = raw[0]['id'] if raw else None
        except:
            code_id = None
        return code_id

    # Берем все ссылки по коду.
    async def selectBoxes(self, code):
        code_id = await self.selectIdByCode(code)
        if code_id is None:
            return None
        raw = await self.db.fetch("SELECT link FROM box WHERE code_id = $1", code_id)
        return raw

    # а это братик-далбаеб предыдущего метода. его скорее всего оставить.
    async def getLinks(self, code):
        code_id = await self.selectIdByCode(code)
        if code_id is None:
            return None
        raw = await self.db.fetch("SELECT link FROM box WHERE code_id = $1", code_id)
        return raw

    # Создание кода ссылки
    async def createCode(self, user_id, code):
        await self.db.execute("INSERT INTO links (user_id, code) VALUES ($1, $2)", user_id, code)

    # Метод, выводящий данные кода ссылки. не используется на данный момент
    async def checkCode(self, code):
        link = await self.db.fetch("SELECT * FROM links WHERE code = $1 ", code)
        return link

    # Добавление ссылок в "коробку"
    async def addLinks(self, links, code):
        code_id = await self.selectIdByCode(code)
        if code_id is None or not links:
            return None
        values = ', '.join([f"('{link}', {code_id})" for link in links])
        await self.db.execute(f"INSERT INTO box (link, code_id) VALUES {values}")
        return 201

    # Берем запись оплозователя
    async def fetchUser(self, user_id):
        user = await self.db.fetch("SELECT * FROM users WHERE user_id = $1", user_id)
        return user

    # Создание записи пользователя
    async def createUser(self, user_info):
        await self.db.execute("""
            INSERT INTO users (email, given_name, family_name, picture, locale, name, verified_email, user_id) 
            VALUES ($1, $2, $3, $4, $5, $6, $7, $8)
        """, user_info.get('email'), user_info.get('given_name'), user_info.get('family_name'),
                user_info.get('picture'), user_info.get('locale'), user_info.get('name'), user_info.get('verified_email'), user_info.get('id'))
