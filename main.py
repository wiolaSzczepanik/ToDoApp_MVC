from controller import Controller
from view import View
from model import Model
import os


def clear_screen():
    os.system("clear")


def main():
    model = Model()
    controller = Controller(model) #przekazuje referencje do modelu
    view = View(model)

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
        clear_screen()
        if option == "1":
            controller.add_item_to_app()
        elif option == "2":
            controller.modify_item()
        elif option == "3":
            controller.delete_item()
        elif option == "4":
            controller.mark_item()
        elif option == "5":
            view.display_item_list()
        elif option == "6":
            view.display_item_details()
        else:
            break


main()
