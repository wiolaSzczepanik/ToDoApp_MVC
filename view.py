from model import Model
from prettytable import PrettyTable

class View:

    def display_item_list(self):
        data_to_display = Model.todo_items

        task_table = PrettyTable([" id ", " Name"])
        index = 0
        for key, value in data_to_display.items():
            task_table.add_row([index, key])
            index += 1

        print(task_table)

    def display_item_details(self):
        pass

tab = View()
tab.display_item_list()
