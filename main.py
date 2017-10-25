from controller import Controller
from view import View
from model import Model
import os
def main():

    while True:
        print("""
    === MENU ===
    (1) Add item to app
    (2) Modify item
    (3) Delete item
    (4) Mark item as done
    (5) Display item's list
    (6) Display specific item's details
    (7) Exit
     """)

        option = input("Select an option: ")
        if option == "1":
            os.system("clear")
            add_item()
        elif option == "2":
            os.system("clear")
            modify_item()
        elif option == "3":
            os.system("clear")
            delete_item_from_app()
        elif option == "4":
            os.system("clear")
            mark_item_as_done()
        elif option == "5":
            os.system("clear")
            display_table_id_and_name()
        elif option == "6":
            os.system("clear")
            display_table_with_details()
        else:
            break


def add_item():
    task = Controller()
    task.add_item_to_app()

def modify_item():
    table = View()
    print(table.display_item_details())
    # task = Controller()
    # task.modify_item()

def display_table_id_and_name():
    table = View()
    print(table.display_item_list())

def display_table_with_details():
    table = View()
    print(table.display_item_details())


main()
