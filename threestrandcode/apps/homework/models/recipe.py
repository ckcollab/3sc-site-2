from django.conf import settings
from django.db import models
from django.utils import timezone
from markupfield.fields import MarkupField

from ..recipes import get_all_recipe_names


RECIPES = get_all_recipe_names()


class Recipe(models.Model):
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="recipes")
    created = models.DateTimeField(default=timezone.now)
    point_min = models.IntegerField(default=0)
    point_max = models.IntegerField(default=0)
    instructions = MarkupField(markup_type='markdown')
    module = models.CharField(choices=RECIPES, max_length=128, unique=True)






    # TODO! Assignments should could some kind of deliverable...!?
    # TODO! Assignments should have some markdown instructions

    def get_class(self):
        module_name, class_name = self.module.split('.')
        return getattr(__import__('homework.recipes.%s' % module_name, fromlist=(class_name,)), class_name)

    def __str__(self):
        return self.module


    # @classmethod
    # def check_user_has_completed(cls, user):
    #     try:
    #         return cls.objects.get(user=user, completed=True)
    #     except cls.DoesNotExist:
    #         return False
    #
    # def get_missing_pre_reqs(self):
    #     """Returns a list of missing pre reqs OR a message describing the problem"""
    #     if hasattr(self, "pre_reqs"):
    #         # pre_reqs are classes, like MakeGHPage
    #         missing_pre_reqs = list(filter(lambda x: not x.check_user_has_completed(self.user), self.pre_reqs))
    #     else:
    #         missing_pre_reqs = None
    #     self.pre_reqs_completed = not missing_pre_reqs
    #     self.save()
    #     return missing_pre_reqs
    #
    # @abc.abstractclassmethod
    # def do_completed_check(self):
    #     raise NotImplementedError()
