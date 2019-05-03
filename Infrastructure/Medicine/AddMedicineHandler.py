from Models.Medicine import Medicine


def add_medicine_menu():
    name = input("Name: ")
    manufacturer = input("Manufacturer: ")
    price = input("Price: ")
    amount = input("Amount: ")
    with_prescription = input("With prescription (y/n): ")
    while not (with_prescription == "y" or with_prescription == "n"):
        print("incorrect value, insert y or n")
        with_prescription = input("With prescription (y/n): ")
    with_prescription = 1 if with_prescription == "y" else 0
    medicine = Medicine(name=name,
                        manufacturer=manufacturer,
                        price=price, amount=amount,
                        with_prescription=with_prescription)
    medicine.save()
