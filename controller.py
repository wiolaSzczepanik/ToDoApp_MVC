from model import Model


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
        print(item_data)


    def delete_item_from_app(self):
        pass

    def mark_item_as_done(self):
        pass
# x = Controller()
# x.add_item_to_app()
# print(x)

# task = Controller.add_item_to_app("lalal", "dhashdjashd")
