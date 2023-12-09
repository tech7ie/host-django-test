from django.db import connection

class DB:

    @staticmethod
    def selectIdByCode(code):
        with connection.cursor() as cursor:
            cursor.execute("SELECT id FROM links WHERE code = %s", [code])
            code_id = cursor.fetchone()[0]
        return code_id


    @staticmethod
    def selectBoxes(code):
        code_id = DB.selectIdByCode(code)
        print(code_id)
        with connection.cursor() as cursor:
            cursor.execute("SELECT link FROM box WHERE code_id = %s", [code_id])
            raw = cursor.fetchall()
        return raw


    @staticmethod
    def createCode(code):
        with connection.cursor() as cursor:
            cursor.execute("INSERT INTO links (user_id, code) VALUES (%s, %s)", [1, str(code)])
            connection.commit()


    @staticmethod
    def addLink(link, code):
        code_id = selectIdByCode(code)
        with connection.cursor() as cursor:
	        cursor.execute("INSERT INTO box (link, code_id) VALUES (%s, %s)", [link, code_id])
	        connection.commit()

        
