import psycopg2
import psycopg2.extras


# декоратор для сериализации ответа в словарь
def toDict(func):
    def wrapper(*args, **kwargs):
        rows = func(*args, **kwargs)
        arr = []
        for row in rows:
            d = {}
            for key in row:
                d[key] = row[key]
            arr.append(d)
        return arr

    return wrapper


class DB:
    def __init__(self):
        try:
            self.connect = psycopg2.connect(
                database="vm31-db",
                user="vm31-user",
                password="comp61",
                host="127.0.0.1",
                port="5433"
            )
            self.cursor = self.connect.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
            print('Connected!!!!!!')
        except ValueError as err:
            print(err)

    def __del__(self):
        self.cursor.close()
        self.connect.close()

    @toDict
    def getAllUsers(self):
        self.cursor.execute("SELECT id, name, login FROM users")
        return self.cursor.fetchall()

    @toDict
    def getAllTestResults(self):
        query = "SELECT id, name, result, date_time FROM test_results ORDER BY date_time"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def insertTestResult(self, name, result):
        self.cursor.execute(
            "INSERT INTO test_results (name, result, date_time) VALUES (%s, %s, now())",
            (name, result)
        )
        self.connect.commit()
        return True
