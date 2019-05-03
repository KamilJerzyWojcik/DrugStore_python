import sqlite3


class Medicine:
    def __init__(self, name=None, manufacturer=None, price=None, amount=None, with_prescription=None, id_medicine=0):
        self.name = name
        self.manufacturer = manufacturer
        self.price = price
        self.amount = amount
        self.with_prescription = with_prescription
        self.id_medicine = id_medicine

    def save(self):

        params = (self.name, self.manufacturer, self.price, self.amount, self.with_prescription)

        with sqlite3.connect("db.sqlite3") as conn:
            command = f"INSERT INTO Medicines(Name, Manufacturer, Price, Amount, WithPrescription) " \
                f"VALUES(?, ?, ?, ?, ?);"
            conn.execute(command, params)

    def load(self):
        if self.id_medicine <= 0:
            print("Error, Id cant be lower than 1")
            return None
        with sqlite3.connect("db.sqlite3") as conn:
            command = f"SELECT * FROM Medicines WHERE Id = {self.id_medicine}"
            cursor = conn.execute(command)
            db_medicine = cursor.fetchone()
        self.__get_medicine(db_medicine)

    def remove(self):
        if self.id_medicine <= 0:
            print("Error, Id cant be lower than 1")
            return None
        with sqlite3.connect("db.sqlite3") as conn:
            command = f"DELETE FROM Medicines WHERE Id = {self.id_medicine}"
            conn.execute(command)

    def __get_medicine(self, db_medicine):
        self.name = db_medicine[1]
        self.manufacturer = db_medicine[2]
        self.price = db_medicine[3]
        self.amount = db_medicine[4]
        self.with_prescription = db_medicine[5]
        self.id_medicine = db_medicine[0]
