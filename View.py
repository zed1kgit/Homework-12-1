class View:
    def __init__(self, controller):
        self.controller = controller

    def print_data_list(self):
        for i in self.controller.show_model_as_list():
            for key, value in i.items():
                print(f"{key} - {value}")
        print()
