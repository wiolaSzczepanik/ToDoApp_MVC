from model import Model
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

        task_table = PrettyTable([" id ", " Name", "Description"])
        index = 0
        for key, value in data_to_display.items():
            task_table.add_row([index, key, value])

            index += 1

        print(task_table)

# tab = View()
# tab.display_item_list()
