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
        return item_data

    def modify_item(self):
        item_data = Model.todo_items
        name = input("Write name to change: ")
        if name in item_data:
            new_name = input("write new name: ")
            item_data[new_name] = item_data[name]
            del item_data[name]

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

    def mark_item(self):
        self.is_done = True
