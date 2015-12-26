from .base_recipe import BaseRecipe
from .github import *


def get_all_recipe_names():
    recipes = []
    for cls in BaseRecipe.__subclasses__():
        # name = cls.__name__
        # module = cls.__module__.split('.')[-1]
        # recipes.append(("%s.%s" % (module, name), cls.description))
        recipes.append((cls.get_name(), cls.description))
    return recipes
