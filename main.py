from Models import ShoesModel, RecipeModel
from Controller import ShoesController, RecipeController
from View import View

shoes_model = ShoesModel()
shoes_controller = ShoesController(shoes_model)
shoes_view = View(shoes_controller)
recipe_model = RecipeModel()
recipe_controller = RecipeController(recipe_model)
recipe_view = View(recipe_controller)

shoes_controller.add_data("мужские", "кроссовки", "черные", 5000, "adidas", 40, "shoes_data")
recipe_controller.add_data("Сырный суп с курицей и грибами",
                           "Елена Петрова",
                           "первое блюдо",
                           "Этот сырный суп получается очень нежным и ароматным благодаря сочетанию курицы, "
                           "грибов и плавленого сыра. Он идеально подходит для холодных зимних дней, когда хочется "
                           "чего-то теплого и уютного.",
                           ["400 г куриного филе",
                            "200 г шампиньонов",
                            "1 луковица",
                            "1 морковь",
                            "2 картофелины",
                            "100 г плавленого сыра",
                            "1 ст.л. растительного масла",
                            "соль, перец по вкусу",
                            "зелень для украшения"],
                           "русская кухня",
                           "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
                           "recipes_data")

shoes_view.print_data_list()
recipe_view.print_data_list()
