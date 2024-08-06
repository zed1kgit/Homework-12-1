class ShoesController:
    def __init__(self, model):
        self.model = model

    def show_model_as_list(self):
        return self.model.get_data()

    def add_data(self, gender_type, type_of_shoes, color, price, brand, size, filename):
        self.model.add_data(gender_type, type_of_shoes, color, price, brand, size, filename)


class RecipeController:
    def __init__(self, model):
        self.model = model

    def show_model_as_list(self):
        return self.model.get_data()

    def add_data(self, title, author, type_of_recipe, description, ingredients: list, kitchen, link, filename):
        self.model.add_data(title, author, type_of_recipe, description, ingredients, kitchen, link, filename)
