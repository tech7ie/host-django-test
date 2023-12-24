import os
import asyncpg


class Database:
    def __init__(self):
        self.db_name = os.getenv('DB_NAME')
        self.user = os.getenv('DB_USER')
        self.password = os.getenv('DB_PASSWORD')
        self.host = os.getenv('DB_HOST')
        self.port = os.getenv('DB_PORT')

    async def connect(self):
        self.conn = await asyncpg.connect(
            database=self.db_name,
            user=self.user,
            password=self.password,
            host=self.host,
            port=self.port
        )


    async def execute(self, query, *args):
        if self.conn is None:
            await self.connect()
        return await self.conn.execute(query, *args)

    async def fetch(self, query, *args):
        if self.conn is None:
            await self.connect()
        return await self.conn.fetch(query, *args)

    async def close(self):
        await self.conn.close()