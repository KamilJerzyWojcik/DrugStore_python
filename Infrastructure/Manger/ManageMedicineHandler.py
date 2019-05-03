from Models.Medicine import Medicine
from Infrastructure.Console import Console
from Infrastructure.Medicine import LoadMedicineHandler


def manage_medicine():
    while True:
        Console.clear()
        LoadMedicineHandler.load_medicines()
        print("")
        command = input("id to delete, or exit: ")
        if command.isdigit() and  int(command) > 0:
            medicine = Medicine(id_medicine=int(command))
            medicine.remove()
        if command.lower() == "exit":
            break

