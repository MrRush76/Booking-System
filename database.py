import sqlite3
from hashing import hash
class Database():
    databaseRef: str

    def __init__(self, givenDatabaseRef: str):
        self.databaseRef = givenDatabaseRef

    def read_all(self, tableName: str):
        db = sqlite3.connect(self.databaseRef)
        data = db.execute("SELECT * FROM " + tableName)
        result = data.fetchall()
        db.close()
        return result

def create_table_user(db):
    db.execute(
        "CREATE TABLE IF NOT EXISTS Users ( User_ID INTEGER PRIMARY KEY, Email TEXT NOT NULL, Username TEXT , Password TEXT NOT NULL, Admin BOOLEAN NOT NULL DEFAULT false )"
    )
def create_table_bookings(db):
    db.execute(
        "CREATE TABLE IF NOT EXISTS Bookings ( Booking_ID INTEGER PRIMARY KEY, User_ID INTEGER REFERENCES Users(User_ID), DATE TEXT NOT NULL, TIME TEXT NOT NULL )"
    )

class user_table(Database):
    def __init__(self, db_path):
        super().__init__(db_path)
        self.connection = sqlite3.connect(db_path)
        self.cursor = self.connection.cursor()
        self.create_table()

    def execute(self, query, params=()):
        self.cursor.execute(query, params)
        return self.cursor

    def check_account(self,email, username, password):
        db = sqlite3.connect(self.databaseRef)
        data = db.execute("SELECT User_ID FROM Users WHERE Email = ? AND Username = ? AND Password = ?", (email, username, hash(password)))
        result = data.fetchall()
        print(result)
        db.close()
        if result:
            return result[0][0]
        return False

    def create_table(self):
        create_table_user(self)

    def check_admin(self, email, username, password):
        db = sqlite3.connect(self.databaseRef)
        data = db.execute("SELECT Admin FROM Users WHERE Email = ? AND Username = ? AND Password = ?", (email, username, hash(password)))
        return data
    def add_user(self,email, username, password, admin=False):
        if not self.check_account(email, username, password):
            db = sqlite3.connect(self.databaseRef)
            data = db.execute("SELECT MAX(User_ID) FROM Users")
            result = data.fetchone()[0]
            if result is not None:
                user_id = result + 1
            else:
                user_id = 1
            db.execute(
                "INSERT INTO Users(user_id,Email,  Username, Password,admin) VALUES (?,?, ?, ?, ?)",
                (user_id,email, username, hash(password),admin))
            db.commit()
            db.close()

class booking_database:
    def __init__(self, db_path):
        super().__init__(db_path)
        self.connection = sqlite3.connect(db_path)
        self.cursor = self.connection.cursor()
        self.create_tables()

    def execute(self, query, params=()):
        self.cursor.execute(query, params)
        return self.cursor

    def create_tables(self):
        create_table_bookings(self)

    def get_available_bookings(self, date, opening_times):
        bookings = self.execute("SELECT Date AND Time FROM Bookings WHERE Date = ?", (date,)).fetchall()
        available_bookings = 
