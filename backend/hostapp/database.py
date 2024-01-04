# import os
# import asyncpg


# class Database:
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


#     async def execute(self, query, *args):
#         await self.connect()
#         return await self.conn.execute(query, *args)

#     async def fetch(self, query, *args):
#         await self.connect()
#         return await self.conn.fetch(query, *args)
# database.py
import os
import asyncpg

class Database:
    def __init__(self):
        self.db_name = os.getenv('DB_NAME')
        self.user = os.getenv('DB_USER')
        self.password = os.getenv('DB_PASSWORD')
        self.host = os.getenv('DB_HOST')
        self.port = os.getenv('DB_PORT')
        self.pool = None

    async def create_pool(self):
        if self.pool is None:
            self.pool = await asyncpg.create_pool(
                database=self.db_name,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port
            )

    async def fetch(self, query, *args):
        await self.create_pool()
        async with self.pool.acquire() as conn:
            return await conn.fetch(query, *args)

    async def execute(self, query, *args):
        await self.create_pool()
        async with self.pool.acquire() as conn:
            return await conn.execute(query, *args)
