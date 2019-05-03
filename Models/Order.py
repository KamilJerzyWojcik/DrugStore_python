import sqlite3


class Order:
    def __init__(self, medicine_id=None, prescription_id=None, order_date=None, amount=None, order_id=0):
        self.medicine_id = medicine_id
        self.prescription_id = prescription_id
        self.order_date = order_date
        self.amount = amount
        self.order_id = order_id

    def save(self):
        params = (self.medicine_id, self.prescription_id, self.order_date, self.amount)
        with sqlite3.connect("db.sqlite3") as conn:
            command = f"INSERT INTO Orders(MedicineId, PrescriptionId, OrderDate, Amount) " \
                f"VALUES(?, ?, ?, ?);"
            conn.execute(command, params)

    def load(self):
        if self.order_id <= 0:
            print("Error, Id cant be lower than 1")
            return None
        with sqlite3.connect("db.sqlite3") as conn:
            command = f"SELECT * FROM Orders WHERE Id = {self.order_id}"
            cursor = conn.execute(command)
            db_order = cursor.fetchone()
        self.__get_order(db_order)

    def remove(self):
        if self.order_id <= 0:
            print("Error, Id cant be lower than 1")
            return None
        with sqlite3.connect("db.sqlite3") as conn:
            command = f"DELETE FROM Orders WHERE Id = {self.order_id}"
            conn.execute(command)

    def __get_order(self, db_order):
        self.medicine_id = db_order[1]
        self.prescription_id = db_order[2]
        self.order_date = db_order[3]
        self.amount = db_order[4]
        self.order_id = db_order[0]

