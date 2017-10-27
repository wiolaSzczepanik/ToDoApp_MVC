from model import Model
from view import View


class Controller:

    def __init__(self, model):
        self.model = model

    def add_item_to_app(self):

        while True:
            name_task = input("Write name for a task: ").lower()
            if len(name_task) > 20:
                print("Too long name. Write again")
                continue
            else:
                break

        while True:
            description = input("Write description for a task: ").lower()
            if len(description) > 150:
                print("Too long descriptopn. Write again")
                continue
            else:
                break

        """obiekty k,urwa"""
        # item = TodoItem(description)
        # self.model.todo_items.update({name_task:item.description})
        # print(self.model.todo_items)

        """wersja ze słownikiami"""
        item = {}
        is_done = False
        item.update({"description":description, "is_done":is_done})
        self.model.todo_items.update({name_task:item})
        print(self.model.todo_items)
        return self.model.todo_items

        """ Stara wersja"""
        # self.model.todo_items.update({name_task:description_for_task})
        # # print(self.model.todo_items)
        # return self.model.todo_items

    def modify_item(self):
        item_data = self.model.todo_items
        chosen_name_to_change = input("Choose name: ").lower()
        mode = input("Press N to change NAME, press D to change DESCRIPTION: ").upper()
        if mode == "N" and chosen_name_to_change in item_data:
            new_name_for_task = input("Write new name: ")
            item_data[new_name_for_task] = item_data[chosen_name_to_change]
            del item_data[chosen_name_to_change]
        if mode == "D" and chosen_name_to_change in item_data:
            new_description = input("Write new description: ")
            item_data[chosen_name_to_change] = new_description
            print(item_data[chosen_name_to_change])

    def delete_item(self):
        item_data = self.model.todo_items
        while True:
            task_name_to_del = input("Write task name which you want to delete: ")
            if task_name_to_del not in item_data:
                print("Try again")
                continue
            else:
                del item_data[task_name_to_del]
                break

    def mark_item(self):
        data = self.model.todo_items
        print(data)
        name_task = input("Write name task: ")
        if name_task in data:
            data[name_task]["is_done"] = True
