from model import Model


class Controller:

    def __init__(self):
        # self.name = name
        # self.description = description
        self.is_done = False

    def add_item_to_app(self):
        """ Method adds new task to dictionary"""

        name_for_task = input("Write name for a task: ")
        description_for_task = input("Write description for a task: ")
        item_data = Model.todo_items
        item_data.update({name_for_task:description_for_task})

        print(item_data)

    def modify_item():
        pass

    def delete_item_from_app():
        pass

    def mark_item_as_done():
        pass



# task = Controller.add_item_to_app("lalal", "dhashdjashd")
