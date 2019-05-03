import sqlite3


class Prescription:
    def __init__(self, customer_name=None, pesel=None, prescription_number=None, id_prescription=0):
        self.customer_name = customer_name
        self.pesel = pesel
        self.prescription_number = prescription_number
        self.id_prescription = id_prescription

    def save(self):

        params = (self.customer_name, self.pesel, self.prescription_number)

        with sqlite3.connect("db.sqlite3") as conn:
            command = f"INSERT INTO Prescription(CustomerName, PESEL, PrescriptionNumber) " \
                f"VALUES(?, ?, ?);"
            new_id = conn.execute(command, params)
        self.id_prescription = new_id.lastrowid

    def load(self):
        if self.id_prescription <= 0:
            print("Error, Id cant be lower than 1")
            return None
        with sqlite3.connect("db.sqlite3") as conn:
            command = f"SELECT * FROM Prescription WHERE Id = {self.id_prescription}"
            cursor = conn.execute(command)
            db_prescription = cursor.fetchone()
        self.__get_medicine(db_prescription)

    def remove(self):
        if self.id_prescription <= 0:
            print("Error, Id cant be lower than 1")
            return None
        with sqlite3.connect("db.sqlite3") as conn:
            command = f"DELETE FROM Prescription WHERE Id = {self.id_prescription}"
            conn.execute(command)

    def __get_medicine(self, db_prescription):
        self.customer_name = db_prescription[1]
        self.pesel = db_prescription[2]
        self.prescription_number = db_prescription[3]
        self.id_prescription = db_prescription[0]
