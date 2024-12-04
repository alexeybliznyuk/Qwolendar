import sqlite3
from config import db_name


class db_work:
    def __init__(self, ddb_file_name):
        self.db_file_name = ddb_file_name

    def get_tasks(self):
        conn = sqlite3.connect(self.db_file_name)

        curs = conn.cursor()

        query_str = """SELECT * FROM Tasks;"""

        quers = []

        query = curs.execute(query_str)

        for row in query:
            quers.append(list(row))

        conn.close()
        # print(quers)
        return quers

        # INSERT INTO имя_таблицы(названия_полей*) VALUES(значения)

    def insert_task(self, dates, timee, labell):
        conn = sqlite3.connect(self.db_file_name)

        curs = conn.cursor()

        query_str = f"""INSERT INTO Tasks(datee, timee, labell) VALUES("{dates}", "{timee}", "{labell}") ;"""

        query = curs.execute(query_str)

        # for row in query:
        #     print(row)
        # print("added")
        conn.commit()
        conn.close()

    #def delete_task(self, dates, timee, labell):
    def delete_task(self, id):

        conn = sqlite3.connect(self.db_file_name)

        curs = conn.cursor()

        # query_str = f"""DELETE FROM Tasks WHERE datee = "{dates}" AND timee = "{timee}" AND labell = "{labell}";"""
        query_str = f"""DELETE FROM Tasks WHERE id = {id};"""
        # DELETE FROM Tasks WHERE datee = "2.2.2022" AND timee = "12:57" AND labell = "label_test_insert";
        query = curs.execute(query_str)
        print("deleted")
        conn.commit()
        conn.close()

    def get_day_tasks(self, datee):
        conn = sqlite3.connect(self.db_file_name)

        curs = conn.cursor()

        query_str = f"""SELECT * FROM Tasks WHERE datee = "{datee}";"""

        quers = []

        query = curs.execute(query_str)

        for row in query:
            quers.append(list(row))

        conn.close()
        #print(quers)
        return quers
    
    

if __name__ == "__main__":
    dbb = db_work(db_name)
    dbb.get_tasks()
    print("------------------")
    #dbb.insert_task("2.2.2022", "12:57", "label_test_insert")
    #dbb.delete_task("22.2.2022", "12:57", "label_test_insert")
    dbb.get_tasks()
