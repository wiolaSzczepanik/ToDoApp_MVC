from model import Model
from view import View


class Controller:

    def __init__(self):
        # self.name = name
        # self.description = description
        self.is_done = False

    def add_item_to_app(self):
        """ Method adds new task to dictionary"""

        while True:
            name_for_task = input("Write name for a task: ")
            if len(name_for_task) > 20:
                print("Too long name. Write again")
                continue
            else:
                break

        while True:
            description_for_task = input("Write description for a task: ")
            if len(description_for_task) > 150:
                print("Too long descriptopn. Write again")
                continue
            else:
                break

        item_data = Model.todo_items
        item_data.update({name_for_task:description_for_task})
#  do testów
        # item_data.update({"ksiazka":"przeczytać książke do końca tygodnia"})
        # item_data.update({"kwiaty":"podlać wszytskie kwiaty"})
        # item_data.update({"zakupy":"przygotować liste zakupów"})
        return item_data

    def modify_item(self):
        # View.display_item_details(table)
        # item_data = Model.todo_items
        # while True:
        #     chosen_element_to_modify = input("If you want modify NAME press N, to modify DESCRIPTION press D: ")
        #     if chosen_element_to_modify == "N":
        #         name_to_change = input("Write name task which you want to change: ")

        pass


    def delete_item(self):
        item_data = Model.todo_items
        while True:
            task_name_to_del = input("Write task name which you want to delete: ")
            if task_name_to_del not in item_data:
                print("Try again")
                continue
            else:
                del item_data[task_name_to_del]
                break



    def mark_item_as_done(self):
        pass
# x = Controller()
# x.add_item_to_app()
# print(x)

# task = Controller.add_item_to_app("lalal", "dhashdjashd")
