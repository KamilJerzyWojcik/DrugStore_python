from Models.Medicine import Medicine
from Models.Prescription import Prescription
from Models.Order import Order
from datetime import datetime


def add_order():
    id_medicine = input("Select Medicine Id: ")
    medicine = Medicine(id_medicine=int(id_medicine))
    medicine.load()
    amount = input("amount medicine: ")
    prescription = __import_prescription(medicine)
    if prescription == None:
        prescription = __add_new_prescription()
    date = datetime.now()
    order = Order(medicine_id=medicine.id_medicine,
                  prescription_id=prescription.id_prescription,
                  order_date=f"{date.day}-{date.month}-{date.year}",
                  amount=amount)
    order.save()


def __import_prescription(medicine):
    prescription = None
    if medicine.with_prescription == 1:
        print("Prescription is necessarily")
        while True:
            id_presciption = input("id prescription or press enter: ")
            if id_presciption == "":
                break
            if id_presciption.isdigit() and int(id_presciption) > 0:
                prescription = Prescription(id_prescription=int(id_presciption))
                try:
                    prescription.load()
                    break
                except:
                    print("Incorrect Id prescription")
    return prescription


def __add_new_prescription():
    customer_name = input("Customer name: ")
    pesel = input("PESEL: ")
    prescription_number = input("prescription number: ")
    prescription = Prescription(customer_name=customer_name,
                                pesel=pesel,
                                prescription_number=prescription_number)
    prescription.save()
    return prescription
