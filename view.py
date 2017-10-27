from model import *
from prettytable import PrettyTable


class View:

    def __init__(self, model):
        self.model = model

    def display_item_list(self):
        data_to_display = self.model.todo_items

        task_table = PrettyTable([" id ", " Name"])
        index = 0
        for key, value in data_to_display.items():
            task_table.add_row([index, key])
            index += 1

        print(task_table)

    def display_item_details(self):
        data_to_display = self.model.todo_items
        name_task = input("Name task: ")
        if name_task in data_to_display:
            index = 0
            task_table = PrettyTable(
                                [" id ", " Name", "Description", "Item done"])
            task_table.add_row([index, name_task,
                                data_to_display[name_task].description,
                                data_to_display[name_task].is_done])
            print(task_table)
        else:
            print("Wrong name. Try again: ")
