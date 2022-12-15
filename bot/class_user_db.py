import sqlite3
import config


class shawarma:
    def connect_to_db(self):
        self.connect = sqlite3.connect('data/db_shawarma.db')
        self.cursor = self.connect.cursor()

    def close(self):
        self.connect.close()

    def get_field(self, shawarma_name, field):
        self.connect_to_db()
        request = f"SELECT {field} FROM shawarma WHERE name_shawarma=?"
        result = self.cursor.execute(request, (shawarma_name,)).fetchone()
        self.close()

        return result[0]


class User:
    def connect_to_db(self):
        self.connect = sqlite3.connect('data/db_shawarma.db')
        self.cursor = self.connect.cursor()

    def close(self):
        self.connect.close()

    def get_all_id(self):
        self.connect_to_db()
        request = "SELECT id FROM user"
        result = self.cursor.execute(request).fetchall()
        self.close()

        return [i[0] for i in result]

    def add_id_to_db(self, user_id):
        self.connect_to_db()
        request = "INSERT INTO user(id, stat) VALUES(?, ?)"
        self.cursor.execute(request, (user_id, "start"))
        self.connect.commit()
        self.close()

    def get_field(self, user_id, field):
        self.connect_to_db()
        request = f"SELECT {field} FROM user WHERE id=?"
        result = self.cursor.execute(request, (user_id,)).fetchone()
        self.close()
        return result[0]

    def set_field(self, user_id, field, value):
        self.connect_to_db()
        request = f"UPDATE user SET {field}=? WHERE id=?"
        self.cursor.execute(request, (value, user_id))
        self.connect.commit()
        self.close()