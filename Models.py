import json


class ShoesModel:
    def __init__(self):
        self.shoes = []

    def add_data(self, gender_type, type_of_shoes, color, price, brand, size, filename):
        self.shoes.append({
            "gender_type": gender_type,
            "type_of_shoes": type_of_shoes,
            "color": color,
            "price": price,
            "brand": brand,
            "size": size
        })
        self.update_json(filename)

    def get_data(self):
        return self.shoes

    def update_json(self, filename):
        with open(f"{filename}.json", "w", encoding="utf-8") as fh:
            json.dump(self.shoes, fh, ensure_ascii=False, indent=2)


class RecipeModel:
    def __init__(self):
        self.recipes = []

    def add_data(self, title, author, type_of_recipe, description, ingredients: list, kitchen, link, filename):
        self.recipes.append({
            "title": title,
            "author": author,
            "type_of_recipe": type_of_recipe,
            "description": description,
            "ingredients": ingredients,
            "kitchen": kitchen,
            "link": link
        })
        self.update_json(filename)

    def get_data(self):
        return self.recipes

    def update_json(self, filename):
        with open(f"{filename}.json", "w", encoding="utf-8") as fh:
            json.dump(self.recipes, fh, ensure_ascii=False, indent=2)
