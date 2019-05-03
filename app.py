from Infrastructure.Medicine import AddMedicineHandler
from Infrastructure.Medicine import RemoveMedicineHandler
from Infrastructure.Medicine import LoadMedicineHandler
from Infrastructure.Order import AddOrderHandler
from Infrastructure.Manger import MangerApp
from Infrastructure.Console import Console


def decision(command):
    if command == "add":
        AddMedicineHandler.add_medicine_menu()
    if command == "del":
        RemoveMedicineHandler.remove_medicine_menu()
    if command == "show":
        LoadMedicineHandler.load_medicines()
    if command == "new":
        AddOrderHandler.add_order()
    if command == "man":
        MangerApp.manager()


command = ""

while True:
    Console.clear()
    print("")
    print(".................")
    print("Add medicine: Add")
    print("Remove medicine: Del")
    print("Show all medicines: Show")
    print("Add Order: New")
    print("Manager: Man")
    print("Exit: Exit")
    print(".................")
    print("")
    command = input("command: ").lower()
    if command == 'exit':
        break

    decision(command)

Console.clear()





