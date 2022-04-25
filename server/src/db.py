import pymysql.cursors

class Db():
    connection = None
    hostname = "flask-db"
    port = "3366"
    username = "root"
    password = "root"
    database = "pets"

    def connect(self, hostname=None, port=None, username=None, password=None, database=None):
        if self.connection is not None:
            return
        if hostname is not None:
            self.hostname = hostname
        if port is not None:
            self.port = port
        if username is not None:
            self.username = username
        if password is not None:
            self.password = password
        if database is not None:
            self.database = database
        # we can connect to the database
        self.connection = pymysql.connect(
            host=self.hostname,
            user=self.username,
            password=self.password,
            database=self.database,
            cursorclass=pymysql.cursors.DictCursor
        )

    def cursor(self):
        return self.connection.cursor()

    def query(self, sql, bind):
        with self.cursor() as cursor:
            cursor.execute(sql, bind)
        print(sql)
        return cursor

    def fetchone(self, sql, bind):
        cursor = self.query(sql, bind)
        return cursor.fetchone()

    def fetchall(self, sql, bind):
        cursor = self.query(sql, bind)
        return cursor.fetchall()