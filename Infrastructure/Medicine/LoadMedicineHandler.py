import sqlite3
from Models.Medicine import Medicine
from Infrastructure.Console import Console

def load_medicines():
    with sqlite3.connect("db.sqlite3") as conn:
        command = f"SELECT id From Medicines"
        cursor = conn.execute(command)
        db_id_medicines = cursor.fetchall()
        medicines = []
        for id_medicine in db_id_medicines:
            medicine = Medicine(id_medicine=id_medicine[0])
            medicine.load()
            medicines.append(medicine)
        __show_medicines(medicines)


def __show_medicines(medicines):
    Console.clear()
    for medicine in medicines:
        print(f"{medicine.id_medicine}| "
              f"{medicine.name}|"
              f"{medicine.price}|"
              f"{medicine.amount}|"
              f"{medicine.with_prescription}")
    print("")
    input("Press Enter")
