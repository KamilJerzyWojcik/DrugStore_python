from Models.Medicine import Medicine


def remove_medicine_menu():
    id_medicine = input("Id medicine: ")

    while not (str.isdigit(id_medicine) and int(id_medicine) > 0):
        print("Incorrect Id medicine")
        id_medicine = input("Id medicine: ")

    medicine = Medicine(id_medicine=int(id_medicine))
    try:
        medicine.remove()
    except:
        remove_medicine_menu()
