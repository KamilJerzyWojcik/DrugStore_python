from Infrastructure.Console import Console
from Infrastructure.Manger import ManageMedicineHandler


def decision(command):
    if command == "med":
        ManageMedicineHandler.manage_medicine()


def manager():
    while True:
        Console.clear()
        print("")
        print(".................")
        print("Manage medicined: Med")
        print("Manage orders: Ord")
        print("Manage prescription: Pre")
        print("Exit: Exit")
        print(".................")
        print("")
        command = input("command: ").lower()
        if command == 'exit':
            break

        decision(command)